"""
Week 3: program 14
A program that reads in X whole numbers and outputs (1) the sum of all positive numbers, (2) the sum
of all negative numbers, and (3) the sum of all positive and negative numbers.
Python 3.14.2
Dishant Bhandula
"""

repeat = "y"
amount = int(input("How many numbers do you want to enter? "))
while repeat != "n":
    total_sum = 0
    neg_sum = 0
    pos_sum = 0

    for x in range(1, amount + 1):
        num = int(input(f"\nPlease enter number {x}: "))
        total_sum += num
        if num > 0:
            pos_sum += num
        else:
            neg_sum += num

    print(f"\nThe sum of all positive numbers is: {pos_sum}")
    print(f"The sum of all negative numbers is: {neg_sum}")
    print(f"The total sum of all numbers is: {total_sum}")

    repeat = input("\nDo you want to repeat? (Y/n) ").lower()
    print("")

"""
Sample run:

>>>
===================== RESTART: /Users/dishb/Documents/csci9/week_3/p14.py ====================
How many numbers do you want to enter? 4

Please enter number 1: 3
Please enter number 2: -4
Please enter number 3: -6
Please enter number 4: 5

The sum of all positive numbers is: 8
The sum of all negative numbers is: -10
The total sum of all numbers is: -2

Do you want to repeat? (Y/n) n

>>>
"""
