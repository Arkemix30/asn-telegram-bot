import requests
from app.core.loggin_config import get_logger

logger = get_logger(__name__)
headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Max-Age": "3600",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
}
# url = "https://www.meteosolana.net/terremotos-recientes/mapa-de-terremotos-recientes-en-nicaragua/"
url = "https://www.meteosolana.net/cache-headers/earthquakes-group/mapa-de-terremotos-recientes-en-nicaragua/50"


def get_earthquake_info():
    logger.info("ℹ Getting current earthquake info")
    try:
        req = requests.get(url, headers)
    except Exception as err:
        logger.exception(f"🛑 Error when getting data from API, error: {err}")
        return None
    data = req.json()
    if not data:
        logger.info("🛑 No data from json body")
        return None
    return data[0]
