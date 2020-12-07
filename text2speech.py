digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

pnum = input()

for i in pnum:
    cast = int(i)
    print(digits[cast])