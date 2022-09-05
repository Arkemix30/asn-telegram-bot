from telegram import constants
from telegram.ext import (
    CallbackContext
)
from app.webscrapper import get_current_earthquake_info
from app.utils.general import get_earthquake_message
from app.core.loggin_config import get_logger

logger = get_logger(__name__)

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