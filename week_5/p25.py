"""
Week 5: program 25
A function named is_triangle(a, b, c) that has three sides a, b, c as parameters.
Python 3.14.2
Dishant Bhandula
"""

def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True

    return False

print("Three sticks with length 3, 4, 5 can form a triangle:",is_triangle(3, 4, 5))
print("Three sticks with length 3, 5, 4 can form a triangle:",is_triangle(3, 5, 4))
print("Three sticks with length 4, 3, 5 can form a triangle:",is_triangle(4, 3, 5))
print("Three sticks with length 4, 5, 3 can form a triangle:",is_triangle(4, 5, 3))
print("Three sticks with length 5, 4, 3 can form a triangle:",is_triangle(5, 4, 3))
print("Three sticks with length 5, 3, 4 can form a triangle:",is_triangle(5, 3, 4))
print("Three sticks with length 20, 3, 4 can form a triangle:",is_triangle(20, 3, 4))
print("Three sticks with length 3, 20, 4 can form a triangle:",is_triangle(3, 20, 4))
print("Three sticks with length 3, 4, 20 can form a triangle:",is_triangle(3, 4, 20))

"""
Sample run:

>>>
===================== RESTART: /Users/dishb/Documents/csci9/week_5/p25.py ====================
Three sticks with length 3, 4, 5 can form a triangle: True
Three sticks with length 3, 5, 4 can form a triangle: True
Three sticks with length 4, 3, 5 can form a triangle: True
Three sticks with length 4, 5, 3 can form a triangle: True
Three sticks with length 5, 4, 3 can form a triangle: True
Three sticks with length 5, 3, 4 can form a triangle: True
Three sticks with length 20, 3, 4 can form a triangle: False
Three sticks with length 3, 20, 4 can form a triangle: False
Three sticks with length 3, 4, 20 can form a triangle: False
>>>
"""
