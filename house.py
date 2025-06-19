name: str = input("What's your name? ")

match name:
    case "Denys" | "Mark":
        print("Kiev")
    case "Diana" | "Lara":
        print("Lviv")
    case _:
        print("Berlin")
    