# EVA Analysis Application

## Overview

This Python application analyses historical Extravehicular Activity (EVA) data.

It provides:
- EVA duration classification (short, standard and long).
- Total EVA duration by country.
- Cumulative EVA duration over time.
- Graphs showing EVA statistics.
- Comparison of EVA activity between two countries over a selected year range.

## Setup and Running

**Requirements:**
- Python 3
- Matplotlib
- pytest (for automated tests)

Install dependencies:

```text
python -m pip install matplotlib pytest
```

Run the application:

```text
python main.py
```

Ensure `eva-data.json` is in the project directory.

The application displays EVA statistics, generates two graphs and prompts the user to compare two countries.

## Module Structure

| Module | Responsibility |
|---|---|
| main.py | Coordinates application execution |
| inputs.py | Collects user input |
| data_loader.py | Reads EVA data from JSON |
| data_processing.py | Validates and prepares EVA records |
| analysis.py | Performs calculations and country comparisons |
| presentation.py | Displays results and generates graphs |

The modules are separated by responsibility to improve maintainability, reduce coupling and allow independent testing.

## Running Tests

Automated tests are located in the `tests` directory.

Run them using:

```text
python -m pytest -v
```

Tests cover country comparison, duration classification and invalid or boundary inputs.

## Architecture Documentation

- `architecture-assessment.txt` — Assessment of the original application.
- `proposed-architecture.txt` — Proposed module structure and dependencies.
- `ADR-001.txt` — Decision to separate application responsibilities into modules.
- `ADR-002.txt` — Decision to separate user input from analysis and presentation.
- `maintainability-evaluation.txt` — Evaluation of the restructured architecture.

## Output

The application generates:
- `country_duration.png` — Total EVA duration by country.
- `cumulative_duration.png` — Cumulative EVA duration over time.

The country-comparison feature displays the number of EVAs, total duration, average duration and the country with the greater total duration.