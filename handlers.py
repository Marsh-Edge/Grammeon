import time
import random
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.helpers import escape_markdown
from telegram.ext import ContextTypes
from corrector import check_message
from formatter import format_result
from resources import BOOKS, WEBSITES, VIDEOS
from dictionary import define
from synonyms_antonyms import synonyms
from tests import QUESTIONS, LEVEL_LABELS, get_results
from exams import EXAM_QUESTIONS, EXAM_NAMES, EXAM_CONDITIONS, get_exam_results

# Rate limiting: {user_id: [timestamp1, timestamp2, ...]}
_rate_limits = {}
RATE_LIMIT = 10
RATE_WINDOW = 60

# Input length limits
MAX_GRAMMAR_LENGTH = 1000
MAX_LOOKUP_LENGTH = 100

REPLY_KEYBOARD = ReplyKeyboardMarkup(
    [["✏️ Fix Grammar", "📖 Help"], ["📚 Resources", "📖 Dictionary"], ["🔄 Synonyms", "📝 Tests"], ["📋 Exams"]],
    resize_keyboard=True
)


def _check_rate_limit(user_id: int) -> bool:
    now = time.time()
    if user_id not in _rate_limits:
        _rate_limits[user_id] = []
    _rate_limits[user_id] = [t for t in _rate_limits[user_id] if now - t < RATE_WINDOW]
    if len(_rate_limits[user_id]) >= RATE_LIMIT:
        return False
    _rate_limits[user_id].append(now)
    return True


MENU_BUTTON = InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")


def _with_menu(reply_markup=None):
    if reply_markup:
        rows = list(reply_markup.inline_keyboard)
        rows.append([MENU_BUTTON])
        return InlineKeyboardMarkup(rows)
    return InlineKeyboardMarkup([[MENU_BUTTON]])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hey👋, Welcome to *Grammeon Bot*\n\nSend me any English sentence to fix it! Use the buttons below to explore.",
        parse_mode='Markdown',
        reply_markup=REPLY_KEYBOARD
    )


def _help_text() -> str:
    return (
        "✏️ *Fix Grammar* — Send a sentence to check its grammar\n"
        "📖 *Help* — See what the bot can do\n"
        "📚 *Resources* — Books, websites & videos for learning\n"
        "📖 *Dictionary* — Look up word definitions\n"
        "🔄 *Synonyms* — Find synonyms and antonyms\n"
        "📝 *Tests* — Take a level test (A1–C1)\n"
        "📋 *Exams* — Practice international English exams (IELTS, TOEFL, CERT)"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        _help_text(),
        parse_mode='Markdown',
        reply_markup=_with_menu()
    )


async def fix_grammar_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["awaiting_correction"] = True
    await update.message.reply_text(
        "✏️ Send me an English sentence and I'll check its grammar.",
        reply_markup=_with_menu()
    )


async def resources_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keys = [
        [InlineKeyboardButton("📖 Books", callback_data="resources_books")],
        [InlineKeyboardButton("🌐 Websites", callback_data="resources_websites")],
        [InlineKeyboardButton("🎬 Videos", callback_data="resources_videos")],
    ]
    await update.message.reply_text(
        "📚 *Choose a category:*",
        parse_mode='Markdown',
        reply_markup=_with_menu(InlineKeyboardMarkup(keys))
    )


async def resources_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "resources_books":
        msg = "📖 *Books*\n\n"
        for b in BOOKS:
            msg += f"*{b['title']}* — {b['author']}\n"
            msg += f"▸ Level: {b['level']}\n"
            msg += f"▸ {b['description']}\n\n"
    elif data == "resources_websites":
        msg = "🌐 *Websites*\n\n"
        for w in WEBSITES:
            msg += f"*{w['name']}*\n"
            msg += f"▸ `{w['url']}`\n"
            msg += f"▸ {w['description']}\n\n"
    elif data == "resources_videos":
        msg = "🎬 *Videos*\n\n"
        for v in VIDEOS:
            msg += f"*{v['title']}* ({v['channel']})\n"
            msg += f"▸ `{v['url']}`\n"
            msg += f"▸ {v['description']}\n\n"

    await query.edit_message_text(msg, parse_mode='Markdown', reply_markup=_with_menu())


async def define_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["awaiting_definition"] = True
    await update.message.reply_text(
        "📖 Send me any English word and I'll look it up for you.",
        reply_markup=_with_menu()
    )


async def synonyms_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["awaiting_synonyms"] = True
    await update.message.reply_text(
        "🔄 Send me any English word and I'll find its synonyms and antonyms.",
        reply_markup=_with_menu()
    )


async def tests_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keys = [[InlineKeyboardButton(lv, callback_data=f"test_level_{lv}") for lv in ["A1", "A2", "B1", "B2", "C1"]]]
    await update.message.reply_text(
        "📝 *Choose a level:*",
        parse_mode='Markdown',
        reply_markup=_with_menu(InlineKeyboardMarkup(keys))
    )


async def test_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data.startswith("test_level_"):
        level = data.replace("test_level_", "")
        if level not in QUESTIONS:
            return
        context.user_data["test_level"] = level
        context.user_data["test_questions"] = random.sample(QUESTIONS[level], 5)
        context.user_data["test_index"] = 0
        context.user_data["test_answers"] = []
        await _send_question(query, context)
    elif data.startswith("test_answer_"):
        try:
            answer = int(data.replace("test_answer_", ""))
            if answer < 0 or answer > 3:
                return
        except ValueError:
            return
        await _handle_answer(query, context)


async def _send_question(query, context):
    level = context.user_data["test_level"]
    idx = context.user_data["test_index"]
    questions = context.user_data["test_questions"]
    q = questions[idx]
    text = "📝 *" + level + " — Question " + str(idx + 1) + "/" + str(len(questions)) + "*\n\n" + escape_markdown(q['question'], version=2)
    buttons = []
    for i, opt in enumerate(q["options"]):
        label = chr(65 + i) + ") " + opt
        buttons.append([InlineKeyboardButton(label, callback_data="test_answer_" + str(i))])
    await query.edit_message_text(text, parse_mode='Markdown', reply_markup=_with_menu(InlineKeyboardMarkup(buttons)))


async def _handle_answer(query, context):
    try:
        answer = int(query.data.replace("test_answer_", ""))
    except ValueError:
        return
    if answer < 0 or answer > 3:
        return
    context.user_data["test_answers"].append(answer)
    context.user_data["test_index"] += 1

    if context.user_data["test_index"] >= len(context.user_data["test_questions"]):
        await _show_results(query, context)
    else:
        await _send_question(query, context)


async def _show_results(query, context):
    level = context.user_data["test_level"]
    answers = context.user_data["test_answers"]
    questions = context.user_data["test_questions"]
    results = get_results(level, answers, questions)

    msg = "📊 *Test Results — " + level + " (" + LEVEL_LABELS[level] + ")*\n"
    score_icon = "✅" if results["percent"] >= 60 else "⚠️"
    msg += score_icon + " Score: " + str(results['score']) + "/" + str(results['total']) + " (" + str(results['percent']) + "%)\n\n"

    for i, d in enumerate(results["details"]):
        q_num = i + 1
        status_icon = "🟢" if d["is_correct"] else "🔴"
        status_label = "Correct" if d["is_correct"] else "Incorrect"
        correct_idx = d["correct"]
        user_idx = d["user_answer"]
        options = d["options"]

        msg += "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
        msg += status_icon + " *Q" + str(q_num) + "* — " + status_label + "\n\n"
        msg += escape_markdown(d['question'], version=2) + "\n\n"

        for opt_i, opt_text in enumerate(options):
            prefix = chr(65 + opt_i) + ")"
            escaped_opt = escape_markdown(opt_text, version=2)
            if opt_i == correct_idx:
                msg += prefix + " " + escaped_opt + " ← ✅\n"
            elif opt_i == user_idx:
                msg += prefix + " " + escaped_opt + " ← ❌\n"
            else:
                msg += prefix + " " + escaped_opt + "\n"

        msg += "\n💡 " + escape_markdown(d['explanation'], version=2) + "\n"

    msg += "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
    msg += "\n💬 *Feedback:* " + escape_markdown(results['feedback'], version=2)

    await query.edit_message_text(msg, parse_mode='Markdown', reply_markup=_with_menu())

    for key in ["test_level", "test_questions", "test_index", "test_answers"]:
        context.user_data.pop(key, None)


# ── Exams ──────────────────────────────────────────────────────────

async def exams_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    accept_button = InlineKeyboardButton("✅ I Accept", callback_data="exam_accept")
    await update.message.reply_text(
        EXAM_CONDITIONS,
        parse_mode='Markdown',
        reply_markup=_with_menu(InlineKeyboardMarkup([[accept_button]]))
    )


async def exam_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "exam_accept":
        keys = [
            [InlineKeyboardButton("📘 IELTS", callback_data="exam_select_IELTS")],
            [InlineKeyboardButton("📗 TOEFL", callback_data="exam_select_TOEFL")],
            [InlineKeyboardButton("📕 CERT", callback_data="exam_select_CERT")],
        ]
        await query.edit_message_text(
            "📋 *Please select your exam:*",
            parse_mode='Markdown',
            reply_markup=_with_menu(InlineKeyboardMarkup(keys))
        )

    elif data.startswith("exam_select_"):
        exam_type = data.replace("exam_select_", "")
        if exam_type not in EXAM_QUESTIONS:
            return
        context.user_data["exam_type"] = exam_type
        context.user_data["exam_questions"] = random.sample(EXAM_QUESTIONS[exam_type], 15)
        context.user_data["exam_index"] = 0
        context.user_data["exam_answers"] = []
        await _send_exam_question(query, context)

    elif data.startswith("exam_answer_"):
        try:
            answer = int(data.replace("exam_answer_", ""))
            if answer < 0 or answer > 3:
                return
        except ValueError:
            return
        await _handle_exam_answer(query, context)


async def _send_exam_question(query, context):
    exam_type = context.user_data["exam_type"]
    idx = context.user_data["exam_index"]
    questions = context.user_data["exam_questions"]
    q = questions[idx]

    section_label = {"reading": "📖 Reading", "grammar": "📝 Grammar", "vocabulary": "📚 Vocabulary"}
    section = section_label.get(q["type"], q["type"].title())

    text = "📋 *" + EXAM_NAMES[exam_type] + "*\n"
    text += section + " — Question " + str(idx + 1) + "/" + str(len(questions)) + "\n\n"

    if q["type"] == "reading" and q.get("passage"):
        text += "_Passage:_\n" + escape_markdown(q["passage"], version=2) + "\n\n"

    text += escape_markdown(q["question"], version=2)

    buttons = []
    for i, opt in enumerate(q["options"]):
        label = chr(65 + i) + ") " + opt
        buttons.append([InlineKeyboardButton(label, callback_data="exam_answer_" + str(i))])

    await query.edit_message_text(text, parse_mode='Markdown', reply_markup=_with_menu(InlineKeyboardMarkup(buttons)))


async def _handle_exam_answer(query, context):
    try:
        answer = int(query.data.replace("exam_answer_", ""))
    except ValueError:
        return
    if answer < 0 or answer > 3:
        return
    context.user_data["exam_answers"].append(answer)
    context.user_data["exam_index"] += 1

    if context.user_data["exam_index"] >= len(context.user_data["exam_questions"]):
        await _show_exam_results(query, context)
    else:
        await _send_exam_question(query, context)


async def _show_exam_results(query, context):
    exam_type = context.user_data["exam_type"]
    questions = context.user_data["exam_questions"]
    answers = context.user_data["exam_answers"]
    results = get_exam_results(exam_type, questions, answers)

    section_label = {"reading": "📖 Reading", "grammar": "📝 Grammar", "vocabulary": "📚 Vocabulary"}

    # Summary message (edited in place)
    summary = "📋 *" + EXAM_NAMES[exam_type] + " — Results*\n"
    score_icon = "✅" if results["percent"] >= 60 else "⚠️"
    summary += score_icon + " Score: " + str(results['score']) + "/" + str(results['total']) + " (" + str(results['percent']) + "%)\n\n"
    summary += "💬 *Feedback:* " + escape_markdown(results['feedback'], version=2)
    summary += "\n\n📊 Detailed results sent below ↓"

    await query.edit_message_text(summary, parse_mode='Markdown', reply_markup=_with_menu())

    # Detailed results (new message to avoid 4096 char limit)
    detail_msg = "📋 *Detailed Results — " + EXAM_NAMES[exam_type] + "*\n\n"

    for i, d in enumerate(results["details"]):
        q_num = i + 1
        status_icon = "🟢" if d["is_correct"] else "🔴"
        status_label = "Correct" if d["is_correct"] else "Incorrect"
        correct_idx = d["correct"]
        user_idx = d["user_answer"]
        options = d["options"]
        sec = section_label.get(d["type"], d["type"].title())

        block = "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
        block += status_icon + " *" + sec + " — Q" + str(q_num) + "* — " + status_label + "\n\n"

        if d["type"] == "reading" and d.get("passage"):
            block += "_" + escape_markdown(d["passage"][:100] + "...", version=2) + "_\n\n"

        block += escape_markdown(d['question'], version=2) + "\n\n"

        for opt_i, opt_text in enumerate(options):
            prefix = chr(65 + opt_i) + ")"
            escaped_opt = escape_markdown(opt_text, version=2)
            if opt_i == correct_idx:
                block += prefix + " " + escaped_opt + " ← ✅\n"
            elif opt_i == user_idx:
                block += prefix + " " + escaped_opt + " ← ❌\n"
            else:
                block += prefix + " " + escaped_opt + "\n"

        block += "\n💡 " + escape_markdown(d['explanation'], version=2) + "\n"

        # Telegram limit is 4096; if adding this block would exceed, send current and start new
        if len(detail_msg) + len(block) > 3800:
            await query.message.reply_text(detail_msg, parse_mode='Markdown')
            detail_msg = block
        else:
            detail_msg += block

    if detail_msg:
        await query.message.reply_text(detail_msg, parse_mode='Markdown')

    for key in ["exam_type", "exam_questions", "exam_index", "exam_answers"]:
        context.user_data.pop(key, None)


async def main_menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text(
        "Hey👋, Welcome to *Grammeon Bot*\n\nSend me any English sentence to fix it! Use the buttons below to explore.",
        parse_mode='Markdown',
        reply_markup=REPLY_KEYBOARD
    )


BUTTON_ROUTES = {
    "✏️ Fix Grammar": fix_grammar_command,
    "📖 Help": help_command,
    "📚 Resources": resources_command,
    "📖 Dictionary": define_command,
    "🔄 Synonyms": synonyms_command,
    "📝 Tests": tests_command,
    "📋 Exams": exams_command,
}


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id

    if not _check_rate_limit(user_id):
        await update.message.reply_text(
            "⏳ You're sending too many messages. Please wait a moment.",
            reply_markup=REPLY_KEYBOARD
        )
        return

    text = update.message.text.strip()

    if text in BUTTON_ROUTES:
        await BUTTON_ROUTES[text](update, context)
        return

    if context.user_data.pop("awaiting_correction", False):
        if len(text) < 3:
            await update.message.reply_text(
                "⚠️ Please send a longer sentence.",
                reply_markup=_with_menu()
            )
            return
        if len(text) > MAX_GRAMMAR_LENGTH:
            await update.message.reply_text(
                f"⚠️ Sentence too long. Maximum {MAX_GRAMMAR_LENGTH} characters.",
                reply_markup=_with_menu()
            )
            return
        try:
            thinking = await update.message.reply_text("🤔 Checking...", reply_markup=_with_menu())
            result = check_message(text)
            await thinking.edit_text(format_result(result), parse_mode='Markdown', reply_markup=_with_menu())
        except Exception:
            await update.message.reply_text(
                "⚠️ Error checking grammar. Please try again.",
                reply_markup=_with_menu()
            )
        return

    if context.user_data.pop("awaiting_definition", False):
        if len(text) > MAX_LOOKUP_LENGTH:
            await update.message.reply_text(
                f"⚠️ Word too long. Maximum {MAX_LOOKUP_LENGTH} characters.",
                reply_markup=_with_menu()
            )
            return
        try:
            await update.message.reply_text("🔍 Looking up...", reply_markup=_with_menu())
            result = await define(text)
            await update.message.reply_text(result, parse_mode='Markdown', reply_markup=_with_menu())
        except Exception:
            await update.message.reply_text(
                "⚠️ Error looking up word. Please try again.",
                reply_markup=_with_menu()
            )
        return

    if context.user_data.pop("awaiting_synonyms", False):
        if len(text) > MAX_LOOKUP_LENGTH:
            await update.message.reply_text(
                f"⚠️ Word too long. Maximum {MAX_LOOKUP_LENGTH} characters.",
                reply_markup=_with_menu()
            )
            return
        try:
            await update.message.reply_text("🔄 Searching...", reply_markup=_with_menu())
            result = await synonyms(text)
            await update.message.reply_text(result, parse_mode='Markdown', reply_markup=_with_menu())
        except Exception:
            await update.message.reply_text(
                "⚠️ Error searching synonyms. Please try again.",
                reply_markup=_with_menu()
            )
        return

    await update.message.reply_text(
        "Please use the buttons below.",
        reply_markup=_with_menu()
    )
