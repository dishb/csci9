"""
Week 3: program 15
A program that calculates exactly how much more (or less) you can make with the penny on day 30.
Python 3.14.2
Dishant Bhandula
"""

penny_money = 0.01
MILLION = 1000000.0

for x in range(1, 31):
    penny_money = 0.01 * (2 ** (x - 1))

diff_amount = abs(MILLION - penny_money)
diff = "less"
if penny_money > MILLION:
    diff = "greater"

print(f"The amount of money from the penny that doubles each day for 30 days will be {diff_amount} {diff} than $1 million on day 1.")

"""
Sample run:

>>>
===================== RESTART: /Users/dishb/Documents/csci9/week_3/p15.py ====================
The amount of money from the penny that doubles each day for 30 days will be 4368709.12 greater than $1 million on day 1.
>>>
"""
