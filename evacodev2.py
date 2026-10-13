import json
from datetime import datetime
import matplotlib.pyplot as plt
from collections import Counter, defaultdict
from typing import Literal

with open("eva-data.json", "r", encoding="utf-8") as file:
    eva_data = json.load(file)

records = []

DurCategory = Literal["short", "standard", "long"]
categorized_durations: defaultdict[DurCategory, list[float]] = defaultdict(list)


def classify_duration(duration_hours: float) -> DurCategory:
    """Classify duration: return duration category."""
    if duration_hours < 4:
        return "short"
    if duration_hours < 7:
        return "standard"
    return "long"


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
    categorized_durations[classify_duration(duration_hours)].append(duration_hours)

total_evas = sum(len(durations) for durations in categorized_durations.values())
print("EVA duration by category:")
for category in ("short", "standard", "long"):
    no = len(categorized_durations[category])
    print(f"  {category.capitalize()}:\t{no} EVAs ({no / total_evas:.2%})")

records.sort(key=lambda record: record[0])

dates = []
cumulative_hours = []
total_hours = 0

country_hours = Counter()
for date, duration_hours, country in records:

    total_hours += duration_hours
    dates.append(date)
    cumulative_hours.append(total_hours)
    country_hours[country] += duration_hours #Add the duration to the count for the country in the Counter Data Type



fig, ax = plt.subplots()
ax.bar(country_hours.keys(), country_hours.values())
ax.set_title("EVA duration by country")
ax.set_xlabel("Country")
ax.set_ylabel("EVA duration (hours)")
plt.tight_layout()
plt.savefig("country_duration.png")
plt.show()

plt.figure()
plt.plot(dates, cumulative_hours)
plt.xlabel("Year")
plt.ylabel("Cumulative EVA duration (hours)")
plt.tight_layout()
plt.savefig("cumulative_duration.png")
plt.show()
