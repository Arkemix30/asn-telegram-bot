import json
from app.core.loggin_config import get_logger
from app.services.earthquake_info import get_earthquake_info
from app.crud.earthquake import earthquake_crud
from app.schemas.earthquake import EarthquakeCreateSchema

logger = get_logger(__name__)


def get_current_earthquake_info():
    data = get_earthquake_info()
    if not data:
        logger.error("🛑 No data from json body")
        return None

    in_db_data = earthquake_crud.get_last_record()

    if in_db_data.get('error'):
        logger.error("🛑 Error when getting last record")
        return None

    if not in_db_data['data']:
        logger.error("🛑 No data found from db")
        data = earthquake_comparison(data)
        if data:
            return data

    if not data["datetime"] == in_db_data['data']["datetime"].strftime("%Y-%m-%d %H:%M:%S"):
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
        logger.error(f"🛑 Error when inserting into DB, error: {err}")
        return None

    if not db_result:
        logger.error("🛑 Error when inserting into DB, no data returned")
    return data
