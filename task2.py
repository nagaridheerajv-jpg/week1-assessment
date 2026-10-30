# Task - 2
# Files, APIs and Environment
# Requirements
# • Create a virtual environment and requirements.txt (requests, python-dotenv, pandas,
# matplotlib, numpy)
# • Read employees.csv with csv.DictReader and write employees.json and
# high_earners.csv (salary above 50000)
# • Store API_KEY in .env, load it with python-dotenv and add .env to .gitignore
# • GET https://jsonplaceholder.typicode.com/users with timeout=5, print id,
# name and email of the first 3 users and handle Timeout, ConnectionError and a 404 on
# /users/9999
# • Parse a nested JSON field with .get() and save the result to users.json


import csv
import json

employees = []
with open("employees.csv","r",newline = "",encoding = "utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["id"] = int(row["id"])
        row["salary"] = int(row["salary"])
        employees.append(row)

print("Total employees:", len(employees))


# Write all employees to employees.json
with open("employees.json", "w", encoding="utf-8") as file:
    json.dump(employees, file, indent=4)

print("employees.json created successfully!")

# Filter employees with salary above 50000
high_earners = [
    employee for employee in employees
    if employee["salary"] > 50000
]

# Write high earners to high_earners.csv
with open("high_earners.csv", "w", newline="", encoding="utf-8") as file:
    field_names = ["id", "name", "department", "salary", "city"]
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(high_earners)

print("high_earners.csv created successfully!")
print("High earners:", [employee["name"] for employee in high_earners])

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
if api_key:
    print("API key loaded successfully!")
else:
    print("API_KEY not found. Check your .env file.")


#GET https://jsonplaceholder.typicode.com/users with timeout=5, print id, name and email of the first 3 users and handle Timeout, ConnectionError and a 404 on
# /users/9999 

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

try:
    response = requests.get(
        f"{BASE_URL}/users",
        timeout=5
    )

    response.raise_for_status()
    users = response.json()

    print("First 3 Users:")

    for user in users[:3]:
        print("ID:", user["id"])
        print("Name:", user["name"])
        print("Email:", user["email"])
        print("-" * 30)

    parsed_users = [
        {
            "id": user.get("id"),
            "name": user.get("name"),
            "email": user.get("email"),
            "city": (user.get("address") or {}).get("city"),
            "latitude": ((user.get("address") or {}).get("geo") or {}).get("lat"),
            "longitude": ((user.get("address") or {}).get("geo") or {}).get("lng"),
        }
        for user in users
    ]
    with open("users.json", "w", encoding="utf-8") as file:
        json.dump(parsed_users, file, indent=4)
    print("users.json created successfully!")

except requests.exceptions.Timeout:
       print("Error: Request timed out!")

except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the API!")

except requests.exceptions.HTTPError as error:
    print("HTTP Error:", error)

# Handle 404 for /users/9999
try:
    response = requests.get(
        f"{BASE_URL}/users/9999",
        timeout=5
    )

    if response.status_code == 404:
        print("Error 404: User not found!")

    else:
        response.raise_for_status()
        print("User data:", response.json())

except requests.exceptions.Timeout:
    print("Error: Request timed out!")

except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the API!")

except requests.exceptions.HTTPError as error:
    print("HTTP Error:", error)        

# Parse a nested JSON field with .get() and save the result to users.json

import requests
import json

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    users = response.json()

    # Parse nested JSON fields using .get()
    parsed_users = []

    for user in users[:3]:
        parsed_user = {
            "id": user.get("id"),
            "name": user.get("name"),
            "email": user.get("email"),

            # Nested fields
            "city": user.get("address", {}).get("city"),
            "company_name": user.get("company", {}).get("name")
        }

        parsed_users.append(parsed_user)

    # Save result to users.json
    with open("users.json", "w", encoding="utf-8") as file:
        json.dump(parsed_users, file, indent=4)

    print("Nested JSON parsed successfully!")
    print("Data saved to users.json")

except requests.exceptions.Timeout:
    print("Error: Request timed out!")

except requests.exceptions.ConnectionError:
    print("Error: Connection failed!")

except requests.exceptions.HTTPError as error:
    print("HTTP Error:", error)

except (ValueError, json.JSONDecodeError) as error:
    print("Invalid JSON:", error)
