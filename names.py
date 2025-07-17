with open("names.txt", "r") as file:
    lines: list = file.readlines()

for line in lines:
    print("Hello,", line.rstrip())