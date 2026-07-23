import csv

# Read the CSV file into a list of lists
employees = []

with open("../csv/employees.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        employees.append(row)

# Create a list of employee names (skip the header)
employee_names = [
    row[1] + " " + row[2]
    for row in employees[1:]
]

print(employee_names)

# Create a new list with only names containing "e"
names_with_e = [
    name
    for name in employee_names
    if "e" in name.lower()
]

print(names_with_e)