from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.helpers import escape_markdown
from telegram.ext import ContextTypes
from corrector import check_message
from formatter import format_result
from resources import BOOKS, WEBSITES, VIDEOS
from dictionary import define
from tests import QUESTIONS, LEVEL_LABELS, get_results

REPLY_KEYBOARD = ReplyKeyboardMarkup(
    [["📖 Help", "📝 Example"], ["📚 Resources", "🔍 Define"], ["📝 Tests"]],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hey👋, Welcome to *Grammeon Bot*\n\nSend me any English sentence to fix it! Use the buttons below to explore.",
        parse_mode='Markdown',
        reply_markup=REPLY_KEYBOARD
    )

def _help_text() -> str:
    return "📖 Just send English text.\n📝 Example — see a sample\n📚 Resources — grammar learning books, websites & videos\n🔍 Define — Press the button and send any word to see its definition\n📝 Tests — Take a level test (A1–C1) to check your English"

def _resources_text() -> str:
    msg = "📚 *Grammar Learning Resources*\n\n"
    msg += "━ *📖 Books* ━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    for b in BOOKS:
        msg += f"\n*{b['title']}* — {b['author']}\n"
        msg += f"▸ Level: {b['level']}\n"
        msg += f"▸ {b['description']}\n"
    msg += "\n━ *🌐 Websites* ━━━━━━━━━━━━━━━━━━━━━━━\n"
    for w in WEBSITES:
        msg += f"\n*{w['name']}*\n"
        msg += f"▸ `{w['url']}`\n"
        msg += f"▸ {w['description']}\n"
    msg += "\n━ *🎬 Videos* ━━━━━━━━━━━━━━━━━━━━━━━━\n"
    for v in VIDEOS:
        msg += f"\n*{v['title']}* ({v['channel']})\n"
        msg += f"▸ `{v['url']}`\n"
        msg += f"▸ {v['description']}\n"
    return msg

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        _help_text(),
        parse_mode='Markdown',
        reply_markup=REPLY_KEYBOARD
    )

async def resources_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        _resources_text(),
        parse_mode='Markdown',
        disable_web_page_preview=True
    )

async def example_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = await update.message.reply_text("🔍 Analyzing...")
    result = check_message("I goed to school and learned many informations.")
    await msg.edit_text(format_result(result), parse_mode='Markdown')

async def define_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["awaiting_definition"] = True
    await update.message.reply_text(
        "🔍 Send me any English word and I'll look it up for you."
    )

async def tests_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keys = [[InlineKeyboardButton(lv, callback_data=f"test_level_{lv}") for lv in ["A1", "A2", "B1", "B2", "C1"]]]
    await update.message.reply_text(
        "📝 *Choose a level:*",
        parse_mode='Markdown',
        reply_markup=InlineKeyboardMarkup(keys)
    )

async def test_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data.startswith("test_level_"):
        level = data.replace("test_level_", "")
        context.user_data["test_level"] = level
        context.user_data["test_questions"] = QUESTIONS[level]
        context.user_data["test_index"] = 0
        context.user_data["test_answers"] = []
        await _send_question(query, context)
    elif data.startswith("test_answer_"):
        await _handle_answer(query, context)

async def _send_question(query, context):
    level = context.user_data["test_level"]
    idx = context.user_data["test_index"]
    questions = context.user_data["test_questions"]
    q = questions[idx]
    text = f"📝 *{level} — Question {idx + 1}/{len(questions)}*\n\n{escape_markdown(q['question'], version=2)}"
    keys = [[InlineKeyboardButton(f"{chr(65 + i)}) {opt}", callback_data=f"test_answer_{i}")]
            for i, opt in enumerate(q["options"])]
    await query.edit_message_text(text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup(keys))

async def _handle_answer(query, context):
    answer = int(query.data.replace("test_answer_", ""))
    context.user_data["test_answers"].append(answer)
    context.user_data["test_index"] += 1

    if context.user_data["test_index"] >= len(context.user_data["test_questions"]):
        await _show_results(query, context)
    else:
        await _send_question(query, context)

async def _show_results(query, context):
    level = context.user_data["test_level"]
    answers = context.user_data["test_answers"]
    results = get_results(level, answers)

    msg = f"📊 *Test Results — {level} ({LEVEL_LABELS[level]})*\n"
    msg += f"Score: {results['score']}/{results['total']} ({results['percent']}%)\n\n"

    for i, d in enumerate(results["details"]):
        icon = "✅" if d["is_correct"] else "❌"
        correct_opt = chr(65 + d["correct"])
        user_opt = chr(65 + d["user_answer"]) if d["user_answer"] >= 0 else "?"
        msg += f"{icon} *Q{i + 1}:* "
        if d["is_correct"]:
            msg += f"Correct! {escape_markdown(d['explanation'], version=2)}\n"
        else:
            msg += f"Wrong. You chose _{user_opt}_, correct answer is *{correct_opt}*. {escape_markdown(d['explanation'], version=2)}\n"

    msg += f"\n💬 *Feedback:* {results['feedback']}"

    await query.edit_message_text(msg, parse_mode='Markdown')

    for key in ["test_level", "test_questions", "test_index", "test_answers"]:
        context.user_data.pop(key, None)

BUTTON_ROUTES = {
    "📖 Help": help_command,
    "📝 Example": example_command,
    "📚 Resources": resources_command,
    "🔍 Define": define_command,
    "📝 Tests": tests_command,
}

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    
    if text in BUTTON_ROUTES:
        await BUTTON_ROUTES[text](update, context)
        return
    
    if context.user_data.pop("awaiting_definition", False):
        await update.message.reply_text("🔍 Looking up...")
        result = await define(text)
        await update.message.reply_text(result, parse_mode='Markdown')
        return
    
    if len(text) < 3:
        await update.message.reply_text("⚠️ Please send a longer sentence.")
        return
    
    thinking = await update.message.reply_text("🤔 Checking...")
    result = check_message(text)
    await thinking.edit_text(format_result(result), parse_mode='Markdown')