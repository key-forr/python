name: str = input("What's your name? ")

#file = open("names.txt", "w")
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
