def main1(): 
    students: list = ["Denys", "Diana", "Ivan"]

    houses: dict = {
        "Denys": "Kiev",
        "Diana": "Lviv",
        "Ivan": "Warsaw"
    }

    for student, house in zip(students, houses.values()):
        print(student, house)

    for student, house in zip(students, houses):
        print(student, houses[house])

    for i in range(len(students)):
        print(i + 1, students[i])

def main2():
    students: list = [
        { "name": "Denys", "city": "Kiev", "age": 19},
        { "name": "Diana", "city": "Lviv", "age": 18},
        { "name": "Ivan", "city": "Warsaw"},
    ]

    for i, student in enumerate(students, start=1):
        age = student.get("age", "-")
        # print(f"{i} {student['name']}, {student['city']}, {age}")
        print(i, student['name'], student['city'], age, sep=", ")

def main3():
    students: list = [
        { "name": "Denys", "city": "Kiev", "age": 19},
        { "name": "Diana", "city": "Lviv", "age": 18, "grade": 11},
        { "name": "Ivan", "city": "Warsaw", "grade": 10},
    ]

    for i, student in enumerate(students, start=1):
        output: str = f"{i} name: {student['name']}, city: {student['city']}"

        if "age" in student:
            output += f", age: {student['age']}"

        if "grade" in student:
            output += f", grade: {student['grade']}"

        print(output)


def main4():
    students: list = [
        { "name": "Denys", "city": "Kiev", "age": 19, "grade": None},
        { "name": "Diana", "city": "Lviv", "age": 18, "grade": 11},
        { "name": "Ivan", "city": "Warsaw", "age": None,"grade": 10},
    ]

    for i, student in enumerate(students, start=1):
        output: str = f"{i} name: {student['name']}, city: {student['city']}, age: {student['age']}, grade: {student['grade']}"

        print(output)

if __name__ == "__main__":
    main2()
