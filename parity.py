def main():
    x: int = int(input("What's x? "))

    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(x) -> bool:
    return x % 2 == 0

if __name__ == "__main__":
    main()