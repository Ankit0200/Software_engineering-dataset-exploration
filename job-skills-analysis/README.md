# job-skills-analysis

Project layout (organized):

```
job-skills-analysis/
│
├── data/
│   ├── raw_jobs.csv                  # raw data (moved from postings2.csv)
│   ├── cleaned_job_postings.csv      # output of cleaning step (if generated)
│   └── skills_matrix_by_role.csv     # matrix of skill counts by role
│
├── notebooks/
│   └── analysis.ipynb                # exploratory notebook (moved from testing.ipynb)
│
├── src/
│   ├── role_normalizer.py            # normalize_job_title helper
│   ├── skill_extractor.py            # helpers to parse job_skills fields
│   └── build_matrix.py               # build skills-by-role matrix
│
├── frontend/
│   ├── app.py                        # Streamlit frontend (moved from streamlit_app.py)
│   └── api.py                        # FastAPI backend (moved from backend.py)
│
├── README.md                         # this file
└── requirements.txt                  # project requirements
```

How to run
-----------
1. Create a virtual environment and install dependencies:

```zsh
cd "./job-skills-analysis"
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -U pip
python3 -m pip install -r requirements.txt
```

2. Start the backend API (in one terminal):

```zsh
cd "./job-skills-analysis/frontend"
python -m uvicorn api:app --reload
```

3. Start the Streamlit frontend (in another terminal):

```zsh
cd "./job-skills-analysis"
streamlit run frontend/app.py
```

Notes
-----
- `raw_jobs.csv` is a copy (moved) of the original raw postings file `postings2.csv`.
- If `cleaned_job_postings.csv` is missing, generate it from the notebook by running the cleaning cells and saving the output.
- The `src/` modules contain small, importable helpers to reuse notebook logic in scripts or tests.

If you want I can:
- Add a `Makefile` with convenience targets (install, run-backend, run-frontend), or
- Add small unit tests for the `src/` functions.
