def main():
    n = get_number()
    say_meow_count(n)

def say_meow_count(n: int):
    for _ in range(n):
        print("meow")

def get_number():
    while True:
        try:
            n: int = int(input("What's n? "))
            if n > 0:
                return n
        except ValueError as e:
            print("Enter a valid integer!")
    
if __name__ == "__main__":
    main()