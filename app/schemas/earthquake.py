from datetime import datetime as dt
from typing import Optional

from pydantic import BaseModel, ValidationError, validator, condecimal


class EarthquakeBaseSchema(BaseModel):
    datetime: Optional[dt]
    latitude: Optional[condecimal(max_digits=6, decimal_places=2)]
    longitude: Optional[condecimal(max_digits=6, decimal_places=2)]
    magnitude: Optional[condecimal(max_digits=6, decimal_places=2)]
    depth: Optional[condecimal(max_digits=6, decimal_places=2)]
    region: Optional[str]
    country: Optional[str]
    city: Optional[str]
    distance: Optional[condecimal(max_digits=6, decimal_places=2)]


class EarthquakeCreateSchema(EarthquakeBaseSchema):
    magnitude: condecimal(max_digits=6, decimal_places=2)
    depth: condecimal(max_digits=6, decimal_places=2)
    region: str
    country: str
    city: str
    distance: condecimal(max_digits=6, decimal_places=2)
