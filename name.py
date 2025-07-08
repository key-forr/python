import sys

if len(sys.argv) < 2:
    sys.exit("too few arg")
elif len(sys.argv) > 2:
    sys.exit("too many arg")

print("My name is ", sys.argv[1])

# try:
#     print("My name is ", sys.argv[1])
# except IndexError:
#     sys.exit("too few arguments")

# for argument in sys.argv[1:-1]:
#     print(argument, end=" ")

# print()

# for argument in sys.argv[1:]:
#     print(argument, end=" ")

# print()

# print("too few arguments") if len(sys.argv) < 2 else print("too many arguments") if len(sys.argv) > 2 else print("My name is ", sys.argv[1])


