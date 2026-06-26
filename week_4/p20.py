"""
Week 4: program 20
A program that generates a random list of numbers.
Python 3.14.2
Dishant Bhandula
"""

from random import randint

list_length = randint(15, 20)
print(f"Generating a list of {list_length} numbers.")

random_list = []
for i in range(list_length):
    random_list.append(randint(2, 5))

print(random_list)

count_of_3 = 0
for number in random_list:
    if number == 3:
        count_of_3 += 1

print(f"The number 3 occurs {count_of_3} times.")


"""
Sample run:

>>>
===================== RESTART: /Users/dishb/Documents/csci9/week_4/p20.py ====================
Generating a list of 18 numbers.
[5, 5, 4, 2, 3, 5, 4, 3, 2, 5, 3, 2, 5, 3, 5, 3, 2, 2]
The number 3 occurs 5 times.
>>>
"""
