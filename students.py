import csv

name = input("What's your name? ")
home = input("Where's your home? ")
phone = input("What's your phone number? ")


with open("students.csv", "a") as file:
    write = csv.DictWriter(file, fieldnames=["name", "home", "phone"])
    write.writerow({ "name": name, "home": home, "phone": phone})

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)
        #students.append({ "name": row["name"], "home": row["home"], "phone": row["phone"] })

for student in students:
    print(f"hello, {student['name']}, you live in {student['home']}, and your phone number is {student['phone']}")