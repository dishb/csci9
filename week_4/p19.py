"""
Week 4: program 19
A program that asks the user to input a sentence.
Python 3.14.2
Dishant Bhandula
"""

sentence = input("Please enter a sentence: ")
letter_1 = input("\nPlease enter the first letter to be counted: ")
letter_2 = input("\nPlease enter the second letter to be counted: ")

letter_1_count = 0
letter_2_count = 0

for letter in sentence:
    if letter_1 == letter:
        letter_1_count += 1

    if letter_2 == letter:
        letter_2_count += 1

print(f"\nIn the sentence {sentence}, the letter \"{letter_1}\" occurs {letter_1_count} times and the letter \"{letter_2}\" occurs {letter_2_count} times.")

"""
Sample run:

>>>
===================== RESTART: /Users/dishb/Documents/csci9/week_4/p19.py ====================
Please enter a sentence: HELLO WORLD

Please enter the first letter to be counted: O

Please enter the second letter to be counted: L

In the sentence HELLO WORLD, the letter "O" occurs 2 times and the letter "L" occurs 3 times.
>>>
"""
