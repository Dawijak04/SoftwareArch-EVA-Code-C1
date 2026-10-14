from datetime import datetime
import pytest

from analysis import compare_countries, classify_duration


#Small dataset with known results
records = [
    (datetime(2020, 1, 1), 4.0, "USA"),
    (datetime(2021, 1, 1), 6.0, "USA"),
    (datetime(2020, 1, 1), 3.0, "Russia"),
    (datetime(2021, 1, 1), 5.0, "Russia"),
    (datetime(2022, 1, 1), 8.0, "USA")
]


#Test 1: Country comparison functionality
def test_country_comparison():
    results, winner = compare_countries(
        records, "USA", "Russia", 2020, 2021
    )

    assert results["USA"]["count"] == 2
    assert results["USA"]["total"] == 10.0
    assert results["USA"]["average"] == 5.0

    assert results["Russia"]["count"] == 2
    assert results["Russia"]["total"] == 8.0
    assert results["Russia"]["average"] == 4.0

    assert winner == "USA"


#Test 2: Existing duration classification
def test_duration_classification():
    assert classify_duration(2.0) == "short"
    assert classify_duration(5.0) == "standard"
    assert classify_duration(8.0) == "long"


#Test 3: Invalid year range
def test_invalid_year_range():
    with pytest.raises(ValueError):
        compare_countries(
            records, "USA", "Russia", 2022, 2020
        )


#Test 4: No EVAs in selected period
def test_no_matching_evas():
    results, winner = compare_countries(
        records, "USA", "Russia", 2010, 2015
    )

    assert results["USA"]["count"] == 0
    assert results["USA"]["total"] == 0
    assert results["USA"]["average"] is None

    assert results["Russia"]["count"] == 0
    assert results["Russia"]["average"] is None
    assert winner == "Tie"


#Test 5: Unknown country
def test_unknown_country():
    with pytest.raises(ValueError):
        compare_countries(
            records, "USA", "France", 2020, 2021
        )