import random

suits = ["heart", "diamond", "spade", "club"]
colors = ["red", "black"]


def play1():
    cpu_move = random.choice(suits)
    print("""Now you guess it's symbol:
    heart
    diamond
    spade
    club""")
    play_move = str(input())

    if play_move == cpu_move:
        print("You win, I'll move in to your island.")
    else:
        print("Sorry roadie.")

def play2():
    cpu_move = random.choice(colors)
    print("""Now you guess it's symbol:
    red
    black""")
    play_move = str(input())

    if play_move == cpu_move:
        print("You win, I'll move in to your island.")
    else:
        print("Sorry roadie.")

play1()
# play2()