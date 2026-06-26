"""
Week 4: program 17
A program that lets a child practice arithmetic skills.
Python 3.14.2
Dishant Bhandula
"""

from random import randint

try_again = 1

while try_again != 2:
    num_1 = randint(0, 9)
    num_2 = randint(0, 9)

    operation = int(input("\nWould you like to add (1), subtract (2) or multiply (3): "))
    if operation == 1:
        result = num_1 + num_2
        guess = int(input(f"\nWhat is {num_1} + {num_2} equal to? "))
        while guess != result:
            guess = int(input(f"\nThat is incorrect, what is {num_1} + {num_2} equal to? "))
    elif operation == 2:
        result = num_1 - num_2
        guess = int(input(f"\nWhat is {num_1} - {num_2} equal to? "))
        while guess != result:
            guess = int(input(f"\nThat is incorrect, what is {num_1} - {num_2} equal to? "))
    elif operation == 3:
        result = num_1 * num_2
        guess = int(input(f"\nWhat is {num_1} * {num_2} equal to? "))
        while guess != result:
            guess = int(input(f"\nThat is incorrect, what is {num_1} * {num_2} equal to? "))

    try_again = int(input("\nCorrect! Would you like to try again? (1 for Yes, 2 for No): "))

"""
Sample run:

>>>
===================== RESTART: /Users/dishb/Documents/csci9/week_4/p17.py ====================

Would you like to add (1), subtract (2) or multiply (3): 1 

What is 3 + 4 equal to? 6

That is incorrect, what is 3 + 4 equal to? 5

That is incorrect, what is 3 + 4 equal to? 7

Correct! Would you like to try again? (1 for Yes, 2 for No): 1

Would you like to add (1), subtract (2) or multiply (3): 3

What is 3 * 2 equal to? 5

That is incorrect, what is 3 * 2 equal to? 6

Correct! Would you like to try again? (1 for Yes, 2 for No): 1

Would you like to add (1), subtract (2) or multiply (3): 2

What is 4 - 8 equal to? -4

Correct! Would you like to try again? (1 for Yes, 2 for No): 2
>>>
"""
