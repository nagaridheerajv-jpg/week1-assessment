# Week 1 Assessment — Employee Data Analysis

## Project Overview

This project analyzes employee and department data using Python, Pandas, NumPy and Matplotlib. It includes data cleaning, department-wise salary analysis, data merging and visualizations.

## Project Structure

```text
week1-assessment/
├── data/
│   ├── employees.csv
│   └── departments.csv
├── notebooks/
│   └── week1_analysis.ipynb
├── reports/
│   └── figures/
│       ├── bar_chart.png
│       ├── histogram.png
│       ├── scatter_plot.png
│       └── line_chart.png
├── src/
│   └── week1_analysis.py
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10 or later
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- nbconvert

## Setup Instructions

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd week1-assessment
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Open the Jupyter Notebook

```bash
jupyter notebook
```

Open `notebooks/week1_analysis.ipynb` and run the cells.

### 5. Export the notebook to Python

Run from the project root:

```bash
jupyter nbconvert --to script notebooks/week1_analysis.ipynb --output-dir src
```

### 6. Run the Python script

```bash
python src/week1_analysis.py
```

Note: The exported script may need adjustment if it contains Jupyter-only commands such as `%timeit`.

## Analysis and Visualizations

The project performs:
- Missing-value handling and duplicate removal.
- Department-wise headcount and salary analysis.
- Inner, left and outer joins between employee and department datasets.
- Four visualizations: bar chart, histogram, scatter plot and line chart.
- Performance measurement using `%timeit` in Jupyter.

## Findings Summary

1. Duplicate employee records were removed to avoid counting the same employee twice.
2. Missing salaries were filled using the median salary of the cleaned employee dataset.
3. Department-wise aggregation calculates employee headcount, average salary and maximum salary.
4. The department dataset identifies Marketing as a department with no employees.
5. Four charts visualize salary comparisons and distribution; the line chart uses employee IDs, not dates.

## Limitations

- Missing salaries were estimated using the median, which can affect salary statistics.
- The line chart is based on employee IDs and does not represent a time-based salary trend.
- The analysis is based on the supplied sample datasets.