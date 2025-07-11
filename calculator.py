def main() -> None:
    x: int = int(input("What's x? "))
    print(f"x squared is {square(x)}")


def square(x: int) -> int:
    return x * x + 1


def correct_square(x: int) -> int:
    return x * x


if __name__ == "__main__":
    main()
