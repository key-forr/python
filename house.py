name: str = input("What's your name? ")

match name:
    case "Denys" | "Mark":
        print("Kiev")
    case "Diana" | "Lara":
        print("Lviv")
    case _:
        print("Berlin")
    

age: int = int(input("How old are you? "))

person: dict = {
    "name": name,
    "age": age
}

match person:
    case { "name": "Denys", "age": age} if age < 18:
        print("Cool")
    case {"name": "Denys", "age": 24} if age == 23:
        print("It's difficult")
    case {"name": "Denys", "age": 24} if age == 24:
        print("It's so difficult")
    case _:
        print('I don\'t know')