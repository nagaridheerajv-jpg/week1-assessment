# Week 1 Assessment

## Setup

1. Install Python 3.10 or later.
2. From the project root, create and activate a virtual environment:
   - Windows PowerShell: `python -m venv .venv` then `.\.venv\Scripts\Activate.ps1`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
3. Install dependencies with `python -m pip install -r requirements.txt`.
4. Create a `.env` file in the project root containing `API_KEY=your_api_key`.
5. Run an exercise from the project root, for example `python task1.py`, `python task2.py`, or `python task3.py`.

The CSV inputs are `employees.csv` and `departments.csv`. Generated JSON and CSV
outputs are written to the project root by the scripts. The `data/`, `src/`, and
`reports/` folders also contain organized copies of inputs, scripts, and generated
reports.

## Findings

- The employee dataset contains 8 employees across Sales, HR, IT, and Finance.
- Five employees earn more than 50,000.
- Four employees are based in Chennai.
- The cleaned employee dataset fills two missing salaries with the median and removes one duplicate.
- Marketing is listed as a department with no employees.
