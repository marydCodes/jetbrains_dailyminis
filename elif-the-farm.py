import math

animals = {"Chicken": 23,
"Goat": 678,
"Pig": 1296,
"Cow": 3848,
"Sheep": 6769}

money = int(input())

if money >= animals["Sheep"]:
    nsheep = math.floor(money // animals["Sheep"])
    print(f"{nsheep} sheep")
elif money >= animals["Cow"]:
    ncow = math.floor(money // animals["Cow"])
    if ncow > 1:
        print(f"{ncow} cows")
    else:
        print("1 cow")
elif money >= animals["Pig"]:
    npig = math.floor(money // animals["Pig"])
    if npig > 1:
        print(f"{npig} pigs")
    else:
        print("1 pig")
elif money >= animals["Goat"]:
    ngoat = math.floor(money // animals["Goat"])
    if ngoat > 1:
        print(f"{ngoat} goats")
    else:
        print("1 goat")
elif money >= animals["Chicken"]:
    nchickn = math.floor(money // animals["Chicken"])
    if nchickn > 1:
        print(f"{nchickn} chickens")
    else:
        print("1 chicken")
else:
    print("None")