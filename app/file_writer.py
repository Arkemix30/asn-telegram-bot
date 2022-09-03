import json
import logging

def write_file(data):
    with open('data.json', 'w', encoding='utf-8') as f:
        try:
            json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as err:
            logging.info(f"🛑 Error while writing into file, error {err}")

        logging.info("✅💾 Writed into file successfully")

def read_file() -> dict:
    logging.info("Reading file...")
    f = open('data.json')
    try:
        data = json.load(f)
    except Exception as err:
        logging.info(f"🛑 Error while reading from file, error {err}")
    return data

