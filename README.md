# CISC7204 Coursework Archive and Proposal Prerequisite Practice

**Project status:** Coursework archive and preliminary practice supporting later proposal projects.

This repository contains the CISC7204 coursework archive and a reproducible Seattle rent analysis. It is the **preliminary practice project** that supports the later Assignment 01 and Assignment 02 proposal projects.

> How are mixed-income apartment counts associated with median apartment rent per unit across Seattle census tracts from 2001 to 2025? Does the pattern differ for year-over-year rent growth, and how well can year, mixed-income count, and property count predict rent levels?

## Dataset and responsible use

The analysis uses the course-provided apartment-rent file [`data/seattle_rent.csv`](data/seattle_rent.csv), copied from the original proposal folder. The matching public source is the [City of Seattle Apartment Market Rent Prices by Census Tract dataset](https://data.seattle.gov/dataset/Apartment-Market-Rent-Prices-by-Census-Tract/h27p-5k3i), prepared by the Seattle Office of Planning and Community Development from CoStar data. The catalog lists the [Open Data Commons PDDL](https://opendatacommons.org/licenses/pddl/summary) and provides CSV and ArcGIS downloads (checked 2026-10-28). No passwords, API keys, or private individual records are included. The analysis is ecological and uses tract-level aggregates.

## Methods

`src/analyze.py` validates required columns, converts numeric fields, removes missing and non-positive rent rows, and produces five labelled figures: the time trend, mixed-income/rent association, mixed-income/rent-growth association, community comparison, and correlation heatmap. A reproducible linear regression benchmark uses year, mixed-income count, and property count to predict rent. The original exploratory notebook is retained as [`src/seattle_rent_original.ipynb`](src/seattle_rent_original.ipynb).

## Findings

The cleaned file contains 3,931 usable rows covering 2001–2025. Mixed-income count has a moderate positive correlation with median rent per unit (r = 0.464) and a near-zero correlation with year-over-year rent change (r = -0.014). The random 80/20 split linear-regression benchmark has test R² = 0.422 and RMSE = $329.08. Rent also changes over time and differs across communities. These are descriptive associations and prediction metrics, not evidence of causal effects.

## Limitations

The data are repeated tract-level observations, so a random train/test split can be optimistic. Rent is a market measure and is not a complete affordability measure. Important factors such as location, unit mix, income, vacancy, and inflation are not controlled. Mixed-income count may be correlated with tract size and property composition. The source describes rent calculations based on market-rate and mixed-income multifamily properties with at least five rental units, using CoStar data prepared by the City.

## Reproduce the analysis

From the repository root:

```bash
python -m pip install -r requirements.txt
python src/analyze.py
```

The command prints the row count and model metrics and regenerates the PNG files under [`figures/`](figures/). To inspect the notebook, start Jupyter and open `src/seattle_rent_original.ipynb`.

## Repository map

- `data/` — the course-provided CSV used by the final analysis.
- `src/analyze.py` — executable analysis and figure generation script.
- `src/seattle_rent_original.ipynb` — original exploratory notebook from the coursework.
- `figures/` — committed outputs used by the portfolio website.
- `REFLECTION.md` — submission reflection.
- `REFLECTION_SHORT.md` — checklist-length reflection.
- `FEEDBACK.md` — record template; a verified classmate review and response are still needed.
- `cisc7204-Assgn01-*`, `cisc7204-Assgn02-*`, and `cisc7204-BonusAssgn03-*` — retained coursework archive.

The proposal materials are maintained separately from this coursework archive. The Module 01–05 folders and the Seattle analysis here are preliminary exercises; they are not the proposal projects themselves. The proposal project pages are linked from the portfolio website.

Portfolio website: <https://mc66006.github.io/data-science-portfolio/>
