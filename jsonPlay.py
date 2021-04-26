import json

colors = {"rainbow": ["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
          "CMYK": ["cyan", "magenta", "yellow", "key color"],
          "RBG": ["red", "blue", "green"]}

# write your code here
with open('colors1.json', 'w') as jsonf1:
    json.dump(colors, jsonf1)

with open('colors2.json', 'w') as jsonf2:
    jsonf2.write(json.dumps(colors))




what = input() #{"greeting_eng" : "Hi!"}

what2 = json.loads(what)
print(type(what2))
print(what2)
