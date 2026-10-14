from pathlib import Path
import os

from data_loader import load_eva_data
from data_processing import prepare_records
from inputs import get_comparison_inputs
from analysis import (
    calculate_categories,
    calculate_country_hours,
    calculate_cumulative_hours,
    compare_countries
)
from presentation import (
    print_category_statistics,
    plot_country_hours,
    plot_cumulative_hours,
    display_country_comparison
)

def run_country_comparison(records):
    try:
        inputs = get_comparison_inputs()
        results, winner = compare_countries(records, *inputs)
        display_country_comparison(results, winner)

    except ValueError as error:
        print(f"Invalid input: {error}")


def main():
    #Ensure relative file paths work
    os.chdir(Path(__file__).resolve().parent)

    #Load data
    eva_data = load_eva_data("eva-data.json")

    #Prepare records
    records = prepare_records(eva_data)

    #Perform analysis
    categories = calculate_categories(records)
    country_hours = calculate_country_hours(records)
    dates, cumulative_hours = calculate_cumulative_hours(records)

    #Present results
    print_category_statistics(categories)
    plot_country_hours(country_hours)
    plot_cumulative_hours(dates, cumulative_hours)

    #Compare countries
    run_country_comparison(records)


if __name__ == "__main__":
    main()