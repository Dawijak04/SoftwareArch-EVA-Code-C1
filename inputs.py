def get_comparison_inputs():
    print("\n--- EVA Country Comparison ---")

    country_a = input("Country A: ").strip()
    country_b = input("Country B: ").strip()
    start_year = int(input("Start year: "))
    end_year = int(input("End year: "))

    return country_a, country_b, start_year, end_year