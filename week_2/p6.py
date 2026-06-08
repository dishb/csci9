"""
Week 2: program 6
Computes a person's height and prints out a message.
Python 3.14.2
Dishant Bhandula
"""

print("Enter your height. First the number of feet, hit enter, and then the number of inches.")
feet = int(input("Feet: "))
inches = float(input("Inches: "))

total_inches = feet * 12 + inches
size = "average"
if total_inches > 72:
    size = "tall"
elif total_inches < 60:
    size = "vertically challenged"

print(f"Your height is {total_inches} inches. You are {size}.")

"""
Sample run:

>>>
===================== RESTART: /Users/dishb/Documents/csci9/week_2/p6.py ====================
Enter your height. First the number of feet, hit enter, and then the number of inches.
Feet: 5
Inches: 11
Your height is 71.0 inches. You are average.
>>>
"""
