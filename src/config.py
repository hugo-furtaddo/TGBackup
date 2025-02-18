import os
import sys
import json

CONFIG = json.load(
    open(os.path.join(os.path.dirname(os.path.dirname(sys.argv[0])), "config.json"))
)


def get_verbose():
    return CONFIG["verbose"]


def get_telegram_api_id():
    return CONFIG["telegram_api_id"]


def get_telegram_api_hash():
    return CONFIG["telegram_api_hash"]

def get_phone():
    return CONFIG["phone_number"]

def get_db_file():
    return CONFIG["db_file"]