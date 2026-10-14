from collections import Counter


def classify_duration(duration_hours):
    if duration_hours < 4:
        return "short"
    if duration_hours < 7:
        return "standard"
    return "long"


def calculate_categories(records):
    categories = Counter()

    for date, duration, country in records:
        category = classify_duration(duration)
        categories[category] += 1

    return categories


def calculate_country_hours(records):
    country_hours = Counter()

    for date, duration, country in records:
        country_hours[country] += duration

    return country_hours


def calculate_cumulative_hours(records):
    sorted_records = sorted(records, key=lambda record: record[0])

    dates = []
    cumulative_hours = []
    total_hours = 0

    for date, duration, country in sorted_records:
        total_hours += duration
        dates.append(date)
        cumulative_hours.append(total_hours)

    return dates, cumulative_hours