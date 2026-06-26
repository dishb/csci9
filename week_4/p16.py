"""
Week 4: program 16
A program that generates two random dice values between 1 and 6 for you, and 2 for the computer.
Python 3.14.2
Dishant Bhandula
"""

from random import randint

print("Beat the computer!\n")

answer = "n"
while answer.lower() != "y":
    user_num1 = randint(1, 6)
    user_num2 = randint(1, 6)
    user_sum = user_num1 + user_num2
    print(f"You rolled a {user_num1} and a {user_num2} (total = {user_sum})")
    answer = input("Do you want to keep those? Y/n:  ")
    if answer.lower() == "n":
        print("\nRolling again...\n")

computer_num1 = randint(1, 6)
computer_num2 = randint(1, 6)
computer_sum = computer_num1 + computer_num2

print(f"\nThe computer rolled a {computer_num1} and a {computer_num2} (total = {computer_sum})")

if user_sum > computer_sum:
    print("You win!")
elif user_sum < computer_sum:
    print("So sorry. You lose.")
else:
    print("Tie!")

"""
Sample runs:

>>>
===================== RESTART: /Users/dishb/Documents/csci9/week_4/p16.py ====================
Beat the computer!

You rolled a 6 and a 1 (total = 7)
Do you want to keep those? Y/n:  n

Rolling again...

You rolled a 5 and a 3 (total = 8)
Do you want to keep those? Y/n:  y

The computer rolled a 4 and a 2 (total = 6)
You win!
>>>

>>>
===================== RESTART: /Users/dishb/Documents/csci9/week_4/p16.py ====================
Beat the computer!

You rolled a 6 and a 2 (total = 8)
Do you want to keep those? Y/n:  y

The computer rolled a 5 and a 6 (total = 11)
So sorry. You lose.
>>>

>>>
===================== RESTART: /Users/dishb/Documents/csci9/week_4/p16.py ====================
Beat the computer!

You rolled a 3 and a 3 (total = 6)
Do you want to keep those? Y/n:  y

The computer rolled a 4 and a 2 (total = 6)
Tie!
>>>
"""
