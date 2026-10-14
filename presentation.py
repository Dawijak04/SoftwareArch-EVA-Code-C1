import matplotlib.pyplot as plt


def print_category_statistics(categories):
    total_evas = sum(categories.values())

    print("EVA duration by category:")

    for category in ("short", "standard", "long"):
        count = categories[category]
        percentage = count / total_evas

        print(f"  {category.capitalize()}: {count} EVAs ({percentage:.2%})")


def plot_country_hours(country_hours):
    fig, ax = plt.subplots()

    ax.bar(country_hours.keys(), country_hours.values())
    ax.set_title("EVA duration by country")
    ax.set_xlabel("Country")
    ax.set_ylabel("EVA duration (hours)")

    plt.tight_layout()
    plt.savefig("country_duration.png")
    plt.show()


def plot_cumulative_hours(dates, cumulative_hours):
    plt.figure()

    plt.plot(dates, cumulative_hours)
    plt.xlabel("Year")
    plt.ylabel("Cumulative EVA duration (hours)")

    plt.tight_layout()
    plt.savefig("cumulative_duration.png")
    plt.show()


def display_country_comparison(results, winner):
    for country, stats in results.items():
        average = (
            f"{stats['average']:.2f}"
            if stats["average"] is not None
            else "Unavailable"
        )

        print(f"\n{country}")
        print(f"EVAs: {stats['count']}")
        print(f"Total hours: {stats['total']:.2f}")
        print(f"Average hours: {average}")

    print(f"\nResult: {winner}")