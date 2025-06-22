cols: int = int(input("How many columns? "))
rows: int = int(input("How many rows? "))

for i in range(rows):
    for j in range(cols):
        print("#", end="")
    print()  

print("--------------")

for i in range(rows):
    print("#" * cols)