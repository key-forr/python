def main():
    name: str = input("What's your name? ")
    hello(name)


def get_greeting(to = "world"):
    return f"Hello, {to}"


def hello(to = "world"):
    print(get_greeting(to))


if __name__ == "__main__": 
    main()