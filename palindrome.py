def palindrome(word):
    if word[::1] == word[::-1]:
        print("Palindrome")
    else:
        print("Not palindrome")

word = input()
palindrome(word)