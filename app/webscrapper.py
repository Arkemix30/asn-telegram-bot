import json
import requests
import logging
from .file_writer import write_file, read_file



headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
# url = "https://www.meteosolana.net/terremotos-recientes/mapa-de-terremotos-recientes-en-nicaragua/"
url = "https://www.meteosolana.net/cache-headers/earthquakes-group/mapa-de-terremotos-recientes-en-nicaragua/50"

def get_current_earthquake_info():
    logging.info("ℹ Getting current earthquake info")
    try:
        req = requests.get(url, headers)
    except Exception as err:
        logging.error(f"🛑 Error when getting data from API, error: {err}")
        return None
    data = req.json()
    if not data:
        logging.info("🛑 No data from json body")
        return None
    infile_data = read_file()
    
    if not data[0]["datetime"] == infile_data["datetime"]:
        logging.info("ℹ💾 New data detected, writing file")
        try:
            write_file(data[0])
        except Exception as err:
            logging.info(f"🛑 Error when writing file, error: {err}")
        return data[0]
    else:
        logging.info("🚨 No earthquakes detected")
        return None
    