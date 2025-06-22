try: 
    x: int = int(input("What's x? "))
except ValueError:
    print("x expect an integer!")
else:
    print(x)

