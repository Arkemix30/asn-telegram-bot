# Python Imports
from datetime import datetime as dt
from typing import Optional

# Third party libraries
from sqlalchemy.ext.declarative import declared_attr
from sqlmodel import Field
from pydantic import condecimal

# Local Imports
from app.utils.utils_models import class_name_to_lower

from .base import Base

tablename_base = "general_"


class Earthquake(Base, table=True):
    datetime: dt
    latitude: Optional[condecimal(max_digits=6, decimal_places=2)] = Field(default=0)
    longitude: Optional[condecimal(max_digits=6, decimal_places=2)] = Field(default=0)
    magnitude: condecimal(max_digits=6, decimal_places=2) = Field(default=0)
    depth: condecimal(max_digits=6, decimal_places=2) = Field(default=0)
    region: str
    country: str
    city: str
    distance: condecimal(max_digits=6, decimal_places=2) = Field(default=0)

    @declared_attr
    def __tablename__(cls):
        return tablename_base + class_name_to_lower(cls.__name__)
