from app.core.loggin_config import get_logger
from app.services.earthquake_info import get_earthquake_info
from app.crud.earthquake import earthquake_crud
from app.schemas.earthquake import EarthquakeCreateSchema

logger = get_logger(__name__)


def get_current_earthquake_info():
    data = get_earthquake_info()
    if not data:
        logger.exception("🛑 No data from json body")
        return None

    in_db_data = earthquake_crud.get_last_record()

    if not in_db_data:
        logger.exception("🛑 No data found from db")
        data = earthquake_comparison(data)
        if data:
            return data

    if not data["datetime"] == in_db_data["datetime"].strftime("%Y-%m-%d %H:%M:%S"):
        data = earthquake_comparison(data)
        return data
    else:
        logger.info("🚨 No earthquakes detected")
        return None


def earthquake_comparison(data):
    logger.info("ℹ💾 New data detected, inserting into db...")
    try:
        new_earthquake = EarthquakeCreateSchema(**data)
        db_result = earthquake_crud.insert(new_earthquake)
    except Exception as err:
        logger.exception(f"🛑 Error when inserting into DB, error: {err}")
        return None

    if not db_result:
        logger.exception("🛑 Error when inserting into DB, no data returned")
    return data
