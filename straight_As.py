#Write a program that calculates the proportion of students who received grade A.

#A five-point rating system with grades A, B, C, D, F is used.

#Input format:
#A string with students' marks separated by space. At least one mark will be present.

#Output format:
#A fractional number with exactly two decimal places.

def straight_A():
    grades = str(input()).split()
    num_grades = len(grades)
    num_As = grades.count("A")
    return round(num_As / num_grades, 2)

print(straight_A())
