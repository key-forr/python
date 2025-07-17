with open("students.csv") as file:
    for line in file:
        name, city, phone = line.rstrip().split(",")
        print(f"{name} is in {city}, phone number: {phone}")
