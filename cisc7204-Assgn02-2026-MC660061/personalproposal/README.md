# Assignment 02 — College Tuition and Graduate Earnings

This folder preserves the Pair 14 revised project proposal and its working data files in the same `personalproposal` layout used for Assignment 01.

## Research question

Is annual undergraduate tuition associated with the median earnings of students who are working and not enrolled 10 years after entering U.S. four-year colleges, and does this relationship differ between public and private institutions?

## Files

- `CISC7204-Assgn02-Pair14-RevisedProjectProposal.docx` — revised proposal, scope, success criteria, task plan, and collaboration plan.
- `CISC7204-Assgn02-Pair14-CollegeTuition-Earnings-Analysis.ipynb` — executable notebook with data selection, cleaning, summary statistics, and planned visualizations.
- `Most-Recent-Cohorts-Institution.csv` — unchanged source extract supplied with the proposal archive.
- `cleaned_data.csv` — notebook output after restricting to predominantly four-year institutions and removing missing, suppressed, and invalid analysis values.

## Data provenance and responsible use

The raw file is an extract from the U.S. Department of Education College Scorecard institution-level data. The official data page is <https://collegescorecard.ed.gov/data/>. The analysis uses institution-level aggregate measures, including tuition and median earnings ten years after entry; it does not contain passwords, API keys, or direct individual records. The source's current data-use notice should be checked before redistributing the raw extract outside this coursework archive.

## Reproduce the notebook

Keep the notebook, `Most-Recent-Cohorts-Institution.csv`, and `cleaned_data.csv` in this folder. Install the packages listed in the repository-level [`requirements.txt`](../../requirements.txt), open the notebook in Jupyter, and run the cells from top to bottom. The notebook reads the raw CSV, writes `cleaned_data.csv`, and produces the tuition, regression, radar, and violin visualizations.

The notebook is a proposal-stage implementation sample. It demonstrates the planned analysis and chart construction; a final submission should add a findings discussion, a clear limitation statement, and a check that every conclusion matches the executed outputs.
