"""
Week 5: program 21
A function which given two integer parameters returns their sum, unless the two values are the same,
then the function returns their doubled sum.
Python 3.14.2
Dishant Bhandula
"""

def sum_double(a, b):
    if a == b:
        return 4 * a

    return a + b

print (sum_double(1, 2))
print (sum_double(2, 2))

"""
Sample run:

>>>
===================== RESTART: /Users/dishb/Documents/csci9/week_5/p21.py ====================
3
8
>>>
"""
