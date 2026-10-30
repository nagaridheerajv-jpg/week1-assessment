# Task - 3
# NumPy, Pandas and Matplotlib
# Requirements
# • Create the marks NumPy array (4 students x 3 subjects) of your choice; print shape, student
# averages (axis=1), subject averages (axis=0), add 5 grace marks by broadcasting and
# compute weighted scores with np.dot

import numpy as np
marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [88, 92, 79],
    [55, 65, 70]
])

print("Marks Array:")
print(marks)

# 2. Print shape
print("Shape:", marks.shape)

# 3. Student averages (axis=1)
student_averages = np.mean(marks, axis=1)
print("Student averages:", student_averages)

# 4. Subject averages (axis=0)
subject_averages = np.mean(marks, axis=0)
print("Subject averages:", subject_averages)

# 5. Add 5 grace marks using broadcasting
grace_marks = marks + 5
print(grace_marks)

# 6. Weighted scores using np.dot
weights = np.array([0.3, 0.3, 0.4])

weighted_scores = np.dot(marks, weights)
print(weighted_scores)

# • Load employees.csv with Pandas; use info(), describe(), loc, iloc and filtering
import pandas as pd
df = pd.read_csv("employees.csv")
# 2. Display complete data
print(df)

# 3. Dataset information
df.info()

# 4. Statistical summary
print(df.describe())

# 5. Select rows and columns using loc
print(df.loc[0])

print(df.loc[:, ["name", "salary"]])

# 6. Select rows and columns using iloc
print(df.iloc[0])
print(df.iloc[0:3])

# 7. Filtering: salary above 50000
print(df[df["salary"] > 50000])

# 8. Filtering: IT department
print(df[df["department"] == "IT"])

# 9. Filtering: Chennai employees
print(df[df["city"] == "Chennai"])

# 10. Multiple conditions
print("\n--- IT Employees with Salary Above 65000 ---")
print(df[(df["department"] == "IT") & (df["salary"] > 65000)])

# • Create departments.csv (department, head, budget) for Sales, HR, IT, Finance and one extra department with no employees; load the employees with 2 missing salaries and 1
# duplicate row of your own, then clean them (median fill, drop_duplicates, correct types)

import pandas as pd

# 1. Prepare sample data with two missing salaries and one duplicate row
df = pd.read_csv("employees.csv")
df.loc[df.index[:2], "salary"] = np.nan
df = pd.concat([df, df.iloc[[2]]], ignore_index=True)

print("--- Original Data ---")
print(df)

# 2. Check missing values
print("\n--- Missing Values Before Cleaning ---")
print(df.isna().sum())

# 3. Drop duplicate rows
df = df.drop_duplicates()

print("\nDuplicate rows removed.")
print("Rows after removing duplicates:", len(df))

# 4. Correct data types
df["id"] = pd.to_numeric(df["id"], errors="raise").astype(int)
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

# 5. Fill missing salaries with median
median_salary = df["salary"].median()
print("Median salary:", median_salary)

df["salary"] = df["salary"].fillna(median_salary).astype(int)

# 6. Ensure text columns have string type
for column in ["name", "department", "city"]:
    df[column] = df[column].astype("string")

# 7. Check cleaned data
print("\n--- Cleaned Employees Data ---")
print(df)

print("\n--- Data Types ---")
print(df.dtypes)

print("\n--- Missing Values After Cleaning ---")
print(df.isna().sum())

# 8. Save cleaned employees data
df.to_csv("employees_cleaned.csv", index=False)
print("\nemployees_cleaned.csv saved successfully!")

# 9. Create and load department data, including one department without employees
departments = pd.DataFrame(
    [
        {"department": "Sales", "head": "Arun", "budget": 500000},
        {"department": "HR", "head": "Priya", "budget": 300000},
        {"department": "IT", "head": "Rahul", "budget": 800000},
        {"department": "Finance", "head": "Karthik", "budget": 400000},
        {"department": "Marketing", "head": "Divya", "budget": 350000},
    ]
)
departments.to_csv("departments.csv", index=False)
departments = pd.read_csv("departments.csv")

departments["department"] = departments["department"].astype("string")
departments["head"] = departments["head"].astype("string")
departments["budget"] = pd.to_numeric(
    departments["budget"], errors="raise"
).astype(int)

print("\n--- Departments Data ---")
print(departments)

# 10. Find departments with no employees
employee_departments = df["department"].unique()

no_employees = departments[
    ~departments["department"].isin(employee_departments)
]

print("\n--- Departments Without Employees ---")
print(no_employees)

# Save departments without employees
no_employees.to_csv("departments_without_employees.csv", index=False)
print("\ndepartments_without_employees.csv saved successfully!")


# • Use groupby().agg() for headcount, average and maximum salary per department and
# pd.merge (inner, left, outer) with departments.csv; list the department with no employees

import pandas as pd

# 1. Load CSV files
employees = pd.read_csv("employees.csv")
departments = pd.read_csv("departments.csv")

# 2. Clean employee data
employees = employees.drop_duplicates()

employees["salary"] = pd.to_numeric(
    employees["salary"], errors="coerce"
)

median_salary = employees["salary"].median()
employees["salary"] = employees["salary"].fillna(median_salary)

employees["salary"] = employees["salary"].astype(int)

print("CLEANED EMPLOYEES:")
print(employees)

# 3. groupby().agg()
# Department-wise headcount, average salary, maximum salary
summary = employees.groupby("department").agg(
    headcount=("id", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max")
).reset_index()

print("\nDEPARTMENT SUMMARY:")
print(summary.round(2))

# 4. INNER MERGE
inner_merge = pd.merge(
    summary, departments,
    on="department", how="inner"
)

print("\nINNER MERGE:")
print(inner_merge)

# 5. LEFT MERGE
left_merge = pd.merge(
    departments, summary,
    on="department", how="left"
)

print("\nLEFT MERGE:")
print(left_merge)

# 6. OUTER MERGE
outer_merge = pd.merge(
    departments, summary,
    on="department", how="outer"
)

print("\nOUTER MERGE:")
print(outer_merge)

# 7. Find departments with no employees
no_employees = left_merge[
    left_merge["headcount"].isna()
]

print("\nDEPARTMENTS WITHOUT EMPLOYEES:")
print(no_employees[["department", "head", "budget"]])


# • Create 4 charts (bar, histogram, scatter, line) with title, axis labels and legend; save as PNG
# and add one sentence of insight for each

import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load and clean data
df = pd.read_csv("employees.csv")
df = df.drop_duplicates()

df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
df["salary"] = df["salary"].fillna(df["salary"].median())

# 2. Create output folder
os.makedirs("reports/figures", exist_ok=True)


# CHART 1: BAR CHART
# Average salary by department
avg_salary = df.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))
avg_salary.plot(kind="bar", label="Average salary")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary (INR)")
plt.legend()
plt.tight_layout()
plt.savefig("reports/figures/bar_chart.png", dpi=300)
plt.close()

print("BAR CHART INSIGHT: The bar chart compares average salaries across departments.")


# CHART 2: HISTOGRAM
# Salary distribution
plt.figure(figsize=(8, 5))
plt.hist(df["salary"], bins=5, edgecolor="black", label="Employees")

plt.title("Employee Salary Distribution")
plt.xlabel("Salary (INR)")
plt.ylabel("Number of Employees")
plt.legend()
plt.tight_layout()
plt.savefig("reports/figures/histogram.png", dpi=300)
plt.close()

print("HISTOGRAM INSIGHT: The histogram shows how employee salaries are distributed across salary ranges.")


# CHART 3: SCATTER PLOT
# Employee ID vs Salary
plt.figure(figsize=(8, 5))
plt.scatter(
    df["id"],
    df["salary"],
    label="Employee salary"
)

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary (INR)")
plt.legend()
plt.tight_layout()
plt.savefig("reports/figures/scatter_plot.png", dpi=300)
plt.close()

print("SCATTER INSIGHT: The scatter plot shows how salaries vary across employee IDs; ID itself does not imply a relationship with salary.")


# CHART 4: LINE CHART
# Salary by employee ID
sorted_df = df.sort_values("id")

plt.figure(figsize=(8, 5))
plt.plot(
    sorted_df["id"],
    sorted_df["salary"],
    marker="o",
    label="Employee salary"
)

plt.title("Employee Salary by ID")
plt.xlabel("Employee ID")
plt.ylabel("Salary (INR)")
plt.legend()
plt.tight_layout()
plt.savefig("reports/figures/line_chart.png", dpi=300)
plt.close()

print("LINE CHART INSIGHT: The line chart shows salary variation across employee IDs, not a time-based trend.")

print("\nAll 4 charts saved successfully in reports/figures/")
