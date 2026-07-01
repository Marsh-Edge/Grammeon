from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from corrector import check_message
from formatter import format_result
from resources import BOOKS, WEBSITES, VIDEOS

REPLY_KEYBOARD = ReplyKeyboardMarkup(
    [["📖 Help", "📝 Example"], ["📚 Resources"]],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hey👋, Welcome to *Grammeon Bot*\n\nSend me any English sentence to fix it! Use the buttons below to explore.",
        parse_mode='Markdown',
        reply_markup=REPLY_KEYBOARD
    )

def _help_text() -> str:
    return "📖 Just send English text.\n/example — see a sample\n/resources — grammar learning books, websites & videos"

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

BUTTON_ROUTES = {
    "📖 Help": help_command,
    "📝 Example": example_command,
    "📚 Resources": resources_command,
}

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    
    if text in BUTTON_ROUTES:
        await BUTTON_ROUTES[text](update, context)
        return
    
    if len(text) < 3:
        await update.message.reply_text("⚠️ Please send a longer sentence.")
        return
    
    thinking = await update.message.reply_text("🤔 Checking...")
    result = check_message(text)
    await thinking.edit_text(format_result(result), parse_mode='Markdown')