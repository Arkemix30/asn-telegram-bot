from sqlmodel import Session, select

from app.models import Earthquake
from app.schemas.earthquake import EarthquakeCreateSchema
from app.utils.utils_models import row2dict


def query_get_last_record(sessions: Session) -> Earthquake:
    statement = select(Earthquake).order_by(Earthquake.id).limit(1)
    result = sessions.exec(statement).first()
    return result


def query_insert_new_earthquake(sessions: Session, earthquake: EarthquakeCreateSchema):
    sessions.add(earthquake)
    sessions.commit()
    sessions.refresh(earthquake)
    return earthquake
