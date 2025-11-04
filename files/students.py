# When second argument is omitted, 'r' mode is assumed by default
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})

# Sort the students by their names

# It's important to define a function in the key,
# because this function will be called for each student dictionary
# def get_name(student):
#     return student["name"]

for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} is in {student['house']}")

