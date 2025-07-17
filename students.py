import csv

students = []


with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home, phone in reader:
        students.append({"name": name, "house": home, "phone": phone})


def get_name(student):
    return student["name"]


for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}, phone number is {student['phone']}")
