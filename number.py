def get_int(prompt: str) -> int:
    while True:
        try: 
            return int(input(prompt))
        except ValueError:
            pass


x: int = get_int("What's x? ")
print(f"x is {x}")    

