for i in range(1,11):
    with open(f'file{i}.txt', 'w') as file:
        file.write(str(i))

#The file salary.txt contains a monthly salary of all employees in the company. Assume that the monthly salary is fixed and each employee is mentioned once. So, each number (an integer) written on a separate line corresponds to a particular employee:

#3500
#4780
#6666
#...

#According to the example, the first worker gets 3,500 per month, the second one 4,780 and the third 6,666, etc.

#Calculate how much each employee earns per year and save their yearly income to a file salary_year.txt. Similarly to the original file, each income should be on a separate line. Preserve the order as it helps identify an employee.

# write your code here
with open('salary.txt') as permth, open('salary_year.txt', 'w') as peryr:
    for line in permth:
        peryr.write(str(int(line) * 12) + '\n')
