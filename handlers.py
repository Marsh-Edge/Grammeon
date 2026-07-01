from telegram import Update
from telegram.ext import ContextTypes
from corrector import check_message
from formatter import format_result
from resources import BOOKS, WEBSITES, VIDEOS

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hey👋, Welcome to *Grammeon Bot*\n\nSend me any English sentence to fix it! if you don't know how to use me, just type /help or if you wanna see a sample, type /example ",
        parse_mode='Markdown'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 Just send English text.\n/example — see a sample\n/resources — grammar learning books, websites & videos",
        parse_mode='Markdown'
    )

async def resources_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
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

    await update.message.reply_text(msg, parse_mode='Markdown', disable_web_page_preview=True)

async def example_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = await update.message.reply_text("🔍 Analyzing...")
    result = check_message("I goed to school and learned many informations.")
    await msg.edit_text(format_result(result), parse_mode='Markdown')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    
    if len(text) < 3:
        await update.message.reply_text("⚠️ Please send a longer sentence.")
        return
    
    thinking = await update.message.reply_text("🤔 Checking...")
    result = check_message(text)
    await thinking.edit_text(format_result(result), parse_mode='Markdown')