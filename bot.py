import os
import logging
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from handlers import start, help_command, resources_command, test_callback, resources_callback, main_menu_callback, handle_message

load_dotenv()

logging.basicConfig(
    level=logging.WARNING,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logging.getLogger('telegram').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)


def main():
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise ValueError("TELEGRAM_TOKEN not found in environment variables.")

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("resources", resources_command))
    app.add_handler(CallbackQueryHandler(test_callback, pattern="^test_"))
    app.add_handler(CallbackQueryHandler(resources_callback, pattern="^resources_"))
    app.add_handler(CallbackQueryHandler(main_menu_callback, pattern="^main_menu$"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logging.info("🤖 Grammeon Bot is starting...")
    app.run_polling()
    logging.info("✅ Bot is running...")


if __name__ == "__main__":
    main()
