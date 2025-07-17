names: list = []

for _ in range(3):
    name: str = input("What's your name? ")
    names.append(name)

for name in sorted(names):
    print(name, end=" ")