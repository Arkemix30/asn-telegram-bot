import os

# Third Party Libraries
from telegram.ext import ApplicationBuilder
from dotenv import load_dotenv

# Local Imports
from app.core.loggin_config import get_logger
from app.commands import info_handler, chat_id_handler, logs_handler, callback_get_info

logger = get_logger(__name__)
load_dotenv(override=True)

token = os.environ.get("TELEGRAM_BOT_TOKEN")


def main():
    logger.info("🤖 Intializing Bot...")
    application = ApplicationBuilder().token(token).build()
    job_queue = application.job_queue

    application.add_handler(info_handler)
    application.add_handler(chat_id_handler)
    application.add_handler(logs_handler)

    logger.info("🤖 Bot Initialized!")
    job_minute = job_queue.run_repeating(callback_get_info, interval=120, first=10)
    application.run_polling()


if __name__ == "__main__":
    main()
