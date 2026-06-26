"""
Week 4: program 18
A program that generates X random integers Num.
Python 3.14.2
Dishant Bhandula
"""

from random import randint

x = randint(10, 15)
nums = []
smallest = 51
largest = 19
nums_sum = 0

print(f"Generating {x} numbers between 20 and 50...")

for i in range(0, x):
    num = randint(20, 50)
    nums.append(str(num))
    nums_sum += num
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print(f"\n...{x} numbers between 20 and 50: " + ", ".join(nums))
print(f"\nSum = {nums_sum}")
print(f"\nAverage = {nums_sum} / {x} = {nums_sum / x}")
print(f"\nSmallest = {smallest}")
print(f"\nLargest = {largest}")

"""
Sample run:

>>>
===================== RESTART: /Users/dishb/Documents/csci9/week_4/p18.py ====================
Generating 10 numbers between 20 and 50...

...10 numbers between 20 and 50: 48, 46, 39, 22, 35, 40, 24, 36, 29, 25

Sum = 344

Average = 344 / 10 = 34.4

Smallest = 22

Largest = 48
>>>
"""
