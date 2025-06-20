import os
import msvcrt

def pause_and_clear():
    msvcrt.getch()
    os.system('cls')


myList: list = ["Denys", 2, 3, True, 10]
names: enumerate = ["Denys", "Diana"]
ages: list = [19, 18]

person: dict = {
    "name": "Denys",
    "age": ages[0]
}

takeNum: int = None

os.system('cls')

while True:
    print(  " 1 - for _ in range(3):\n",
            "2 - for i in range(1, 6):\n",
            "3 - for i in range(5):\n",
            "4 - for i in range(2, 20, 2):\n",
            "5 - for i in range(20, 0, -4):\n",
            "6 - for i in myList:\n",
            "7 - for index, name in enumerate(names):\n",
            "8 - for name, age in zip(enumerate(name), ages):\n",
            "9 - for key in person:\n",
            "10 - for key, value in person.items():\n",
            "11 - for value in person.values():\n",
            f"12 - print('meow\\n' * 3)\n",
            "0 - to leave")
    
    try:
        takeNum: int = int(input("Select a menu item: "))
    except ValueError as e:
        print(e)
        break

    match takeNum:
        case 0:
            break
        case 1:
            for _ in range(3):
                print("meow", end=" ", flush=True)
        case 2:
            for i in range(1, 6):
                print(i, end=" ", flush=True)
        case 3:
            for i in range(5):
                print(i, end=" ", flush=True)
        case 4:
            for i in range(2, 20, 2):
                print(i, end=" ", flush=True)
        case 5:
            for i in range(20, 0, -4):
                print(i, end=" ", flush=True)
        case 6:
            for i in myList:
                print(i, end=" ", flush=True)
        case 7:
            for index, name in enumerate(names):
                print(index, name, end=" ", flush=True)
        case 8:
            for (index, name), age in zip(enumerate(names), ages):
                print(index, name, age, end=" ", flush=True)
        case 9:
            for key in person:
                print(key, end=" ", flush=True)
        case 10:
            for key, value in person.items():
                print(key, value, end=" ", flush=True)
        case 11:
            for value in person.values():
                print(value, end=" ", flush=True)
        case 12:
            print('meow\n' * 3, end=" ", flush=True)
        case _:
            break

    pause_and_clear()
            


