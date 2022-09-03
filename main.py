import os
import logging
from telegram import Update, constants
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    CallbackContext,
)
from dotenv import load_dotenv
from app.webscrapper import get_current_earthquake_info
from app.utils import format_datettime
load_dotenv(override=True)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

token = os.environ.get("TELEGRAM_BOT_TOKEN")


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info(f"ℹ User: {update.effective_user.username} has said Hello!")
    await update.message.reply_text(f"Hello {update.effective_user.first_name}")


async def chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info(f"ℹ User: {update.effective_user.username} has requested chat id")
    await update.message.reply_text(f"Chat ID: {update.effective_chat.id}")


async def callback_get_info(context: CallbackContext) -> None:
    logging.info("ℹ Executng Callback Getting info")
    result = get_current_earthquake_info()
    if result:
        logging.info("📩 Sending data to group")
        datetime = result.get("datetime")
        datetime = format_datettime(datetime)
        magnitude = result.get("magnitude")
        depth = result.get("depth")
        city = result.get("city")
        distance = result.get("distance")
        text = (
            f"🚨 NUEVO TERREMOTO 🚨"
            f"\n🕣 Fecha: {datetime}\n📈 Magnitud: {magnitude}"
            f"\n⏬ Profundidad: {depth}km\n🌎Localización: A {distance}km de {city}"
        )

        await context.bot.send_message(
            chat_id="-1001613000876", text=text, parse_mode=constants.ParseMode.MARKDOWN
        )
    logging.info("✅ℹ Callbak Get Info Finished")


if __name__ == "__main__":
    logging.info("Intializing Bot...")
    application = ApplicationBuilder().token(token).build()
    job_queue = application.job_queue

    start_handler = CommandHandler("hello", hello)
    chat_id_handler = CommandHandler("chat_id", chat_id)

    application.add_handler(start_handler)
    application.add_handler(chat_id_handler)
    logging.info("Bot Initialized!")
    job_minute = job_queue.run_repeating(callback_get_info, interval=60, first=10)
    application.run_polling()
