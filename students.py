import csv

name = input("What's your name? ")
home = input("Where's your home? ")
phone = input("What's your phone number? ")


with open("students.csv", "a") as file:
    write = csv.writer(file)
    write.writerow([name, home, phone])