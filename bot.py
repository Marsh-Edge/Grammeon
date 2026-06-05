import os
import logging
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from handlers import start, example_command, help_command, handle_message

load_dotenv()
logging.basicConfig(level=logging.INFO)

def main():
  token = os.getenv("TELEGRAM_TOKEN")
  if not token:
    raise logging.error("TELEGRAM_TOKEN not found in environment variables.")
  
  app = Application.builder().token(token).build()
  app.add_handler(CommandHandler("start", start))
  app.add_handler(CommandHandler("help", help_command))
  app.add_handler(CommandHandler("example", example_command))
  app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
  
  print("Bot is running...")
  app.run_polling()
  
  if __name__ == "__main__":
    main()