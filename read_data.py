import json
from config import JSON_DATA_PATH


def read_all_data():
    with open(JSON_DATA_PATH, 'r', encoding="utf8") as json_data:
        all_discounts_data = dict(json.load(json_data))
        # TODO: add log
    return all_discounts_data
