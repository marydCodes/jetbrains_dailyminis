name = input()

dict_ = {
   "é": "e",
   "ë": "e",
   "á": "a",
   "å": "a",
   "œ": "oe",
   "æ": "ae" 
}

def normalize(name):

    for char in name:
        for k in dict_.keys():
            if char == k:
                new_name = name.replace(char, dict_[k])

    return new_name

print(normalize(name))