from datetime import datetime


def prepare_records(eva_data):
    records = []

    for eva in eva_data:
        date_text = eva.get("date")
        duration_text = eva.get("duration")
        country = eva.get("country")

        if not date_text or not duration_text:
            continue

        date = datetime.fromisoformat(date_text)

        hours, minutes = map(int, duration_text.split(":"))
        duration_hours = hours + minutes / 60

        records.append((date, duration_hours, country))

    return records