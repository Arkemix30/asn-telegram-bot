import os
from telegram import Update, constants
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    CallbackContext,
)
from dotenv import load_dotenv
from app.webscrapper import get_current_earthquake_info
from app.utils.general import get_earthquake_message
from app.core.loggin_config import get_logger

logger = get_logger(__name__)
load_dotenv(override=True)

token = os.environ.get("TELEGRAM_BOT_TOKEN")


async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info(f"ℹ User: {update.effective_user.username} has requested bot info")
    text = (
        f"Este es un bot no oficial de Alerta Sísmica Nicaragua"
        f"\nEl propósito de este bot es para poder informar acerca de los sismos en Nicaragua"
        f"\nBot creado por: Enmanuel Silva Laguna"
        f"\nUsuario de Telegram: @ARKEMIX"
    )
    await update.message.reply_text(text)


async def chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info(f"ℹ User: {update.effective_user.username} has requested chat id")
    await update.message.reply_text(f"Chat ID: {update.effective_chat.id}")


async def callback_get_info(context: CallbackContext) -> None:
    logger.info("ℹ Executng Callback Getting info")
    result = get_current_earthquake_info()
    if result:
        logger.info("📩 Sending data to group")
        text = get_earthquake_message(result)
        await context.bot.send_message(
            chat_id="-1001613000876", text=text, parse_mode=constants.ParseMode.MARKDOWN
        )
    logger.info("✅ℹ Callbak Get Info Finished")


def main():
    logger.info("🤖 Intializing Bot...")
    application = ApplicationBuilder().token(token).build()
    job_queue = application.job_queue

    info_handler = CommandHandler("info", info)
    chat_id_handler = CommandHandler("chat_id", chat_id)

    application.add_handler(info_handler)
    application.add_handler(chat_id_handler)
    logger.info("🤖 Bot Initialized!")
    job_minute = job_queue.run_repeating(callback_get_info, interval=120, first=10)
    application.run_polling()


if __name__ == "__main__":
    main()
