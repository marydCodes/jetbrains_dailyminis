# input: C C C I C C C C I I C C C C C C C C C Answer: Game over 7
# input: C C I I C C C C C C C C C C C Answer: You won 13

scores = input().split()
# put your python code here
# print(scores)
Is = 0
Cs = 0

for item in scores:
    # check num Is
    if Is < 3:
        if item == "C":
            Cs += 1
        elif item == "I":
            Is += 1
    elif Is == 3:
        print("Game over", Cs, sep="\n")
        break
if Is < 3:
    print("You won", Cs, sep="\n")