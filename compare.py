x: int = None
y: int = None

while True:
    try:
        x = int(input("What's x? "))
        y = int(input("What's y? "))

        if type(x) == int and type(y) == int:
            break
    except ValueError:
        print("Enter number please")
    
if x < y:
    print("x is less than y")
elif x == y: 
    print("x is equal to y")
else:
    print("x is greatest than y")

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

print("x is not equal to y" if x != y else "x is equal to y")

xValue: str = "x is greatest" if x > y else "x is less" if x < y else "x is equal"

print(xValue)
