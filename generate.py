import random

my_list: list = [1,2,3,4,5,6,7,8,9]

coin: str = random.choice(["heads", "tails"])
value: int = random.randint(0, 100)
random.shuffle(my_list)

print(coin, value, my_list, sep="\n")