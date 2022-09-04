from datetime import datetime as dt
import logging
from pytz import utc, timezone


def format_datettime(datetime: str) -> str:
    try:
        date = dt.strptime(datetime, "%Y-%m-%d %H:%M:%S")
    except Exception as err:
        logging.info(f"🛑 Error when converting datetime, error: {err} ")
    new_date = utc.localize(date, is_dst=None).astimezone(timezone("America/Managua"))
    return new_date.strftime("%d-%m-%Y %I:%M:%S %p")


def get_earthquake_message(result):
    datetime = format_datettime(result.get("datetime"))
    magnitude = result.get("magnitude")
    depth = result.get("depth")
    city = result.get("city")
    distance = result.get("distance")
    earthquake_type = "SISMO" if magnitude < 7 else "TERREMOTO"
    text = (
        f"🚨 NUEVO {earthquake_type} DETECTADO 🚨"
        f"\n🕣 Fecha: {datetime}\n📈 Magnitud: {magnitude}"
        f"\n⏬ Profundidad: {depth}km\n🌎Localización: A {distance}km de {city}"
    )
    return text
