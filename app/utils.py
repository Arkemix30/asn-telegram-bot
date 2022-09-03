from datetime import datetime as dt
import logging
def format_datettime(datetime:str) -> str:
    try:
        date = dt.strptime(datetime,"%Y-%m-%d %H:%M:%S")
    except Exception as err:
        logging.info(f"🛑 Error when converting datetime, error: {err} ")

    return date.strftime("%d-%m-%Y %I:%M:%S %p")

