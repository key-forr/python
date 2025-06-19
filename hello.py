def main():
    name: str = input("What's your name? ")
    print(hello(name))
    sayHi: str = hello()
    print(sayHi)

def hello(name: str = "world"):
    return f"Hello, {name}"

if __name__ == "__main__":
    main()