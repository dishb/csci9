"""
Week 3: program 12
A program that computes the tuition in ten years and displays a table of the years and tuition
costs.
Python 3.14.2
Dishant Bhandula
"""

tuition = 10000
for x in range(1, 11):
    print(f'Year {x} Tuition {tuition:.0f}')
    tuition = 1.05 * tuition

"""
Sample run:

>>>
===================== RESTART: /Users/dishb/Documents/csci9/week_3/p12.py ====================
Year 1 Tuition 10000
Year 2 Tuition 10500
Year 3 Tuition 11025
Year 4 Tuition 11576
Year 5 Tuition 12155
Year 6 Tuition 12763
Year 7 Tuition 13401
Year 8 Tuition 14071
Year 9 Tuition 14775
Year 10 Tuition 15513
>>>
"""
