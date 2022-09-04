import os
from dotenv import load_dotenv
from app.core.loggin_config import get_logger

logger = get_logger(__name__)
load_dotenv(override=True)

DATABASE_URL = os.environ.get("DATABASE_URL")


def get_db_uri():
    return DATABASE_URL
