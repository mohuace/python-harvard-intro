import csv

# Take a look at the csv file, it has Mulund,Mumbai as extra value in one of the rows
# To handle such complex csv files, we can use the csv module to detect and parse the values correctly
students = []
with open("students_complex.csv") as file:
    reader = csv.reader(file)
    for name, house in reader:
        students.append({"name": name, "house": house})

for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} is in {student['house']}")