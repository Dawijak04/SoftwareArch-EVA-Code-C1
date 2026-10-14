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

def compare_countries(records, country_a, country_b, start_year, end_year):

    if start_year > end_year:
        raise ValueError("Start year cannot be greater than end year.")
    
    if country_a == country_b:
        raise ValueError("Please select two different countries.")

    countries = {country for date, duration, country in records}

    if country_a not in countries or country_b not in countries:
        raise ValueError("One or both countries are not recognised.")

    results = {}

    for country in (country_a, country_b):

        matching_records = [
            duration
            for date, duration, record_country in records
            if record_country == country
            and start_year <= date.year <= end_year
        ]

        count = len(matching_records)
        total = sum(matching_records)
        average = total / count if count > 0 else None

        results[country] = {
            "count": count,
            "total": total,
            "average": average
        }

    total_a = results[country_a]["total"]
    total_b = results[country_b]["total"]

    if total_a > total_b:
        winner = country_a
    elif total_b > total_a:
        winner = country_b
    else:
        winner = "Tie"

    return results, winner