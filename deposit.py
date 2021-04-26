deposit = int(input())
year = 0
rate = 0.071
while deposit < 700000:
    year += 1
    deposit = deposit + (deposit * rate)
print(year)