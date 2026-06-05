from telegram import Update
from telegram.ext import contexttypes
from corrector import check_message
from formatter import format_result

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text(
      "👋 *Grammar Bot*\n\nSend me any English sentence!",
      parse_mode='Markdown'
  )
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text(
      "📖 Just send English text.\n/example — see a sample",
      parse_mode='Markdown'
  )
  
async def example_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = await update.message.reply_text("🔍 Analyzing...")
    result = check_text("I goed to school and learned many informations.")
    await msg.edit_text(format_result(result), parse_mode='Markdown')
    
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
  text = update.message.text.strip()
  
  if len(text) < 3:
    await update.message.reply_text("⚠️ Please send a longer sentence.")
    return
  
  thinking = await update.message.reply_text("🤔 Checking...")
  result = check_message(text)
  await thinking.edit_text(format_result(result), parse_mode='Markdown')