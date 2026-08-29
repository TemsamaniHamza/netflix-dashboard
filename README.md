# Netflix Catalog Intelligence

An editorial-style Streamlit dashboard for exploring a historical snapshot of the Netflix catalog. It focuses on catalog growth, content mix, production geography, genre concentration, and the lag between a title's release and its addition to Netflix.

[Live dashboard](https://netflix-dashboard-pix.streamlit.app/)

## What it does

- Filters the complete dashboard by format, addition year, country, rating, or title search
- Calculates live takeaways from the active selection instead of showing static “insights”
- Visualizes annual catalog velocity, leading countries, genres, and release recency
- Provides a title-level explorer with synopsis, cast, director, and catalog metadata
- Exports the current filtered selection as CSV
- Documents the dataset's limitations directly in the interface

## Design

The interface uses a restrained dark system inspired by editorial analytics products—not a clone of Netflix's consumer UI. The visual hierarchy is intentionally simple:

1. Select a catalog slice in the sidebar.
2. Read the headline metrics and computed signals.
3. Explore portfolio composition and recency.
4. Inspect or export individual records.

The layout is responsive and uses native Streamlit controls with a custom presentation layer. Plotly's interaction toolbar is hidden to keep the reading experience focused; hover details remain available.

## Run locally

Requires Python 3.10 or newer.

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

On Windows, activate the environment with `venv\Scripts\activate`.

## Project structure

```text
.
├── .streamlit/config.toml
├── netflix_data/netflix_titles.csv
├── streamlit_app.py
├── requirements.txt
└── README.md
```

## Data notes

This repository uses a public historical Netflix titles dataset. It is not a live availability feed.

- Records without a valid `date_added` value are excluded from time analysis.
- The first listed country is treated as the primary production country.
- Genre counts are multi-label, so one title may contribute to several genres.
- “Catalog lag” is calculated as `year_added - release_year`.
- A title appearing in the dataset does not mean it is currently available on Netflix.

## Stack

- Streamlit
- Pandas
- Plotly

Netflix is a trademark of Netflix, Inc. This independent project is for exploratory data analysis.
