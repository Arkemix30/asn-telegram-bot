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

def tail(f, lines=20):
    total_lines_wanted = lines

    BLOCK_SIZE = 1024
    f.seek(0, 2)
    block_end_byte = f.tell()
    lines_to_go = total_lines_wanted
    block_number = -1
    blocks = []
    while lines_to_go > 0 and block_end_byte > 0:
        if block_end_byte - BLOCK_SIZE > 0:
            f.seek(block_number * BLOCK_SIZE, 2)
            blocks.append(f.read(BLOCK_SIZE))
        else:
            f.seek(0, 0)
            blocks.append(f.read(block_end_byte))
        lines_found = blocks[-1].count(b"\n")
        lines_to_go -= lines_found
        block_end_byte -= BLOCK_SIZE
        block_number -= 1
    all_read_text = b"".join(reversed(blocks))
    return b"\n".join(all_read_text.splitlines()[-total_lines_wanted:])

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


def get_logs_info(lines:int=20):
    with open("./logs.log", "r", encoding="utf-8") as f:
        logs = f.readlines()
        data_logs = " ".join(logs)
        data_logs = data_logs.split("\n")
        data_logs = data_logs[-lines::]
    text = ""
    for line in data_logs:
        inline_words = line.split(" ")
        inline_words = inline_words[4::]
        inline_text = " ".join(inline_words)
        text = text + "\n" + inline_text
    return text
        