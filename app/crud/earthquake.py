from app.core.db import get_session
from app.core.loggin_config import get_logger
from app.models.earthquake import Earthquake
from app.schemas.earthquake import EarthquakeCreateSchema
from app.utils.queries.earthquake_queries import (
    query_get_last_record,
    query_insert_new_earthquake,
)
import pytz

logger = get_logger(__name__)


class CRUDEarthquake:
    def __init__(self):
        self.db = get_session()

    def insert(self, obj_in: EarthquakeCreateSchema) -> Earthquake:
        logger.info("Inserting new earthquake into database")
        try:
            db_obj = Earthquake(**obj_in.dict())
            obj_out = query_insert_new_earthquake(self.db, db_obj)
        except Exception as err:
            logger.error(f"Error when inserting into database, error: {err}")
            return None
        return obj_out

    def get_last_record(self):
        try:
            db_record: Earthquake = query_get_last_record(self.db)
            if db_record:
                db_record = db_record.dict()
        except Exception as err:
            msg_error = "Error when getting last record"
            logger.error(f"{msg_error}, error: {err}")
            return {"error": msg_error}
        return {'data': db_record}


earthquake_crud = CRUDEarthquake()
