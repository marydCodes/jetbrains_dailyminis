# There is a text and also an integer in the input. You need to split the text into sentences. Use a number (the second line in the input) as an index for choosing a sentence from the list. Tokenize this sentence using the pattern "[A-z']+" and print it.


import nltk

# sent = input()
# idx = int(input())

sent = "Meet the Greens! They've got a big house on the outskirts of Leeds. There are 15 rooms in it."
idx = 2

# split the input into sentences
split_sent = nltk.sent_tokenize(sent)

# use the index to choose a sentence from the list
# split_sent[2]

# tokenize idx sentence
result = nltk.regexp_tokenize(split_sent[idx], "[A-z']+")

print(result)
