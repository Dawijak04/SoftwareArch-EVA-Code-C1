import json


def load_eva_data(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)