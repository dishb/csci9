"""
Week 2: program 7
A program which asks the user for a student's grade as a percent, and then returns their letter grade.
Python 3.14.2
Dishant Bhandula
"""

percent_grade = float(input("Enter the student's grade as a percent: "))
if percent_grade > 100 or percent_grade < 0:
    print("ERROR: Invalid grade. Please enter a value between 0 and 100.")
    percent_grade = float(input("Enter the student's grade as a percent: "))

if percent_grade >= 90:
    print("The student's letter grade is: A")
elif percent_grade >= 80:
    print("The student's letter grade is: B")
elif percent_grade >= 70:
    print("The student's letter grade is: C")
elif percent_grade >= 60:
    print("The student's letter grade is: D")
else:
    print("The student's letter grade is: F")


"""
Sample run:

>>>
===================== RESTART: /Users/dishb/Documents/csci9/week_2/p7.py ====================
Enter the student's grade as a percent: -1
ERROR: Invalid grade. Please enter a value between 0 and 100.
Enter the student's grade as a percent: 75
The student's letter grade is: C
>>>
"""