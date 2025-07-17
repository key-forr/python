students = []


with open("students.csv") as file:
    for line in file:
        name, house, phone = line.rstrip().split(",")
        students.append({"name": name, "house": house, "phone": phone})


def get_name(student):
    return student["name"]


for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}, phone number is {student['phone']}")
