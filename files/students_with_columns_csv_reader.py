import csv
from unicodedata import name


students = []
with open("students_with_columns.csv") as file:
    # DictReader reads the first row in CSV as column names and then creates a dictionary for each subsequent row
    # The keys of the dictionary are the column names
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "house": row["house"]})

for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} is in {student['house']}")