# Task - 1
# Python Core, OOP and Errors
# Use this data (employees.csv):
# id,name,department,salary,city
# 1,Arun,Sales,30000,Chennai
# 2,Priya,HR,45000,Chennai
# 3,Rahul,IT,60000,Bangalore
# 4,Divya,IT,75000,Chennai
# 5,Karthik,Finance,90000,Mumbai
# 6,Meena,Sales,52000,Bangalore
# 7,Suresh,IT,68000,Chennai
# 8,Anitha,HR,48000,Mumbai
# Requirements
# • Write bonus(salary, rate=0.1, *extras, **options) that returns salary * rate plus
# the extras; if options has cap, the result must not exceed it
# • Create the class Employee(name, salary) with annual_salary() and
# Manager(Employee) with team_size that overrides get_details() and uses
# super().__init__()

# • Create the custom exception InvalidSalaryError and raise it from Employee when the
# salary is negative; catch it with try/except/finally
# • Using the data below, build with a list comprehension the list of names with salary above
# 50000, use map and lambda to add a 10% raise, and use filter to keep Chennai
# employees
# • Use a for loop with continue (skip salary 0) and break (stop after the first salary above
# 85000)
# Expected Output
# Above 50000: ['Rahul', 'Divya', 'Karthik', 'Meena', 'Suresh']
# Chennai: ['Arun', 'Priya', 'Divya', 'Suresh']
# Error: Invalid salary: -500
# Transaction finished
# Concepts: functions, *args, **kwargs, lambda, comprehensions, OOP, inheritance, custom
# exceptions, loops

class InvalidSalaryError(Exception):
    pass

def bonus(salary,rate=0.1,*extras,**options):
    result = salary * rate + sum(extras)

    if "cap" in options:
        result = min(result,options["cap"])
    return result

class Employee:
    def __init__(self,name,salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")

        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return self.name,self.salary
class Manager(Employee):
    def __init__(self,name,salary,team_size):
        super().__init__(name,salary)
        self.team_size =team_size

    def get_details(self):
        return (
            f"Name: {self.name}, Salary: {self.salary}, "
            f"Team Size: {self.team_size}"
        )

employees = [
    {"id": 1, "name": "Arun", "department": "Sales",
     "salary": 30000, "city": "Chennai"},
    {"id": 2, "name": "Priya", "department": "HR",
     "salary": 45000, "city": "Chennai"},
    {"id": 3, "name": "Rahul", "department": "IT",
     "salary": 60000, "city": "Bangalore"},
    {"id": 4, "name": "Divya", "department": "IT",
     "salary": 75000, "city": "Chennai"},
    {"id": 5, "name": "Karthik", "department": "Finance",
     "salary": 90000, "city": "Mumbai"},
    {"id": 6, "name": "Meena", "department": "Sales",
     "salary": 52000, "city": "Bangalore"},
    {"id": 7, "name": "Suresh", "department": "IT",
     "salary": 68000, "city": "Chennai"},
    {"id": 8, "name": "Anitha", "department": "HR",
     "salary": 48000, "city": "Mumbai"},
]

above_50000 = [
    emp["name"] for emp in employees
    if emp["salary"] > 50000
]
print("Above 50000:", above_50000)

raised_salaries = list(
    map(lambda emp: emp["salary"] * 1.10,employees)
)
print(raised_salaries)

chennai_employees = list(
    filter(lambda emp: emp["city"] == "Chennai",employees)
)
print("Chennai:", [emp["name"] for emp in chennai_employees])

for emp in employees:
    salary = emp["salary"]

    if salary == 0:
        continue
    if salary > 85000:
        break
    print(emp["name"],salary)

try:
    employee1 = Employee("Dheeraj",-500)
except InvalidSalaryError as error:
        print(f"Error: {error}")
finally:
     print("Transaction finished")


print("Bonus:", bonus(30000))
print("Bonus with extras:", bonus(30000, 0.1, 500, 200))
print("Bonus with cap:", bonus(30000, 0.1, 500, cap=2000))



employee2 = Employee("Rahul", 60000)
print(employee2.get_details())
print("Annual salary:", employee2.annual_salary())

manager1 = Manager("Divya", 75000, 5)
print(manager1.get_details())
