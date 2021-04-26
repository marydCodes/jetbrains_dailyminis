# Write a program that reads an integer value n from the standard input and prints the result of the expression:
# ((n + 1) * n + 2) * n + 3

# FUNCTIONAL
def evaluate():
    n = int(input())
    print(((n + 1) * n + 2) * n + 3)
    
evaluate()

def evaluate_alt():
    n = int(input())
    return ((n + 1) * n + 2) * n + 3
    
print(evaluate_alt())
