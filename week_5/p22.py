"""
Week 5: program 22
A function that calculates the absolute value and returns the absolute value of a number.
Python 3.14.2
Dishant Bhandula
"""

def absolute(a):
    if a >= 0:
        return a

    return a * -1

b = float(input("Enter a positive or negative value: "))
print(f"The absolute value of {b} is {absolute(b)}")

"""
Sample runs:

>>>
===================== RESTART: /Users/dishb/Documents/csci9/week_5/p22.py ====================
Enter a positive or negative value: -53.023 
The absolute value of -53.023 is 53.023
>>>

>>>
===================== RESTART: /Users/dishb/Documents/csci9/week_5/p22.py ====================
Enter a positive or negative value: 8
The absolute value of 8.0 is 8.0
>>>
"""
