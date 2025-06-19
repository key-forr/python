def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(x):
    x = pow(x, 2)
    return x

if __name__ == "__main__":
    main()