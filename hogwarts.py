students: list = ["Denys", "Diana", "Ivan"]

houses: dict = {
    "Denys": "Kiev",
    "Diana": "Lviv",
    "Ivan": "Warsaw"
}

for student, house in zip(students, houses.values()):
    print(student, house)

for i in range(len(students)):
    print(i + 1, students[i])