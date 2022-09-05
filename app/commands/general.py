from telegram import Update
from telegram.ext import (
    ContextTypes,
    CommandHandler,
)
from app.core.loggin_config import get_logger
from app.utils.general import get_logs_info

logger = get_logger(__name__)

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info(f"ℹ User: {update.effective_user.username} has requested bot info")
    text = (
        f"Este es un bot no oficial de Alerta Sísmica Nicaragua."
        f"\nEl propósito de este bot es para poder informar acerca de los sismos en Nicaragua."
        f"\nBot creado por: Enmanuel Silva Laguna"
        f"\nUsuario de Telegram: @ARKEMIX"
    )
    await update.message.reply_text(text)

async def logs(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info(f"ℹ User: {update.effective_user.username} has requested logs")
    if not update.effective_user.username == "ARKEMIX":
        await update.message.reply_text(f"You are not allowed to perform this action")
        return
    lines = 20
    if len(context.args) > 0:
        lines = context.args[0]
    try:
        result = get_logs_info(lines)
        text = result
    except Exception as err:
        text = "🛑 Error when getting logs"
        logger.error(f"Error when getting logs, error: {str(err)}")
    await update.message.reply_text(text)

async def chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info(f"ℹ User: {update.effective_user.username} has requested chat id")
    await update.message.reply_text(f"Chat ID: {update.effective_chat.id}")


info_handler = CommandHandler("info", info)
chat_id_handler = CommandHandler("chat_id", chat_id)
logs_handler = CommandHandler("logs", logs)