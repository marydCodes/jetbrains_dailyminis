def check_email(string):
    if " " not in string:
        if "@" in string:
            if "@." not in string:
                z = string.index("@")
                if "." in string[z:]:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

######################

def check_email(string):
    a = ' ' not in string
    b = '@.' not in string
    c = '@' in string
    index = string.find('@')
    d = '.' in string[index:]
    return all([a, b, c, d])