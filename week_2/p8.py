"""
Week 2: program 8
A program to simulate rock-paper-scissors game.
Python 3.14.2
Dishant Bhandula
"""

from random import choice

VALID_CHOICES = ["r", "p", "s"]
computer_choice = choice(VALID_CHOICES)
player_choice = input("Enter your choice (r for rock, p for paper, s for scissors): ").lower()
print(f"Computer chose: {computer_choice}")

if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == "r" and computer_choice == "s":
    print("You win! Rock beats scissors.")
elif player_choice == "p" and computer_choice == "r":
    print("You win! Paper beats rock.")
elif player_choice == "s" and computer_choice == "p":
    print("You win! Scissors beats paper.")
elif computer_choice == "r" and player_choice == "s":
    print("Computer wins! Rock beats scissors.")
elif computer_choice == "p" and player_choice == "r":
    print("Computer wins! Paper beats rock.")
elif computer_choice == "s" and player_choice == "p":
    print("Computer wins! Scissors beats paper.")

"""
Sample run:

===================== RESTART: /Users/dishb/Documents/csci9/week_2/p8.py ====================
>>>
Enter your choice (r for rock, p for paper, s for scissors): p
Computer chose: s
Computer wins! Scissors beats paper.
>>>

===================== RESTART: /Users/dishb/Documents/csci9/week_2/p8.py ====================
>>>
Enter your choice (r for rock, p for paper, s for scissors): s
Computer chose: s
It's a tie!
>>>

===================== RESTART: /Users/dishb/Documents/csci9/week_2/p8.py ====================
>>>
Enter your choice (r for rock, p for paper, s for scissors): r
Computer chose: p
Computer wins! Paper beats rock.

>>>

===================== RESTART: /Users/dishb/Documents/csci9/week_2/p8.py ====================
>>>
Enter your choice (r for rock, p for paper, s for scissors): s
Computer chose: p
You win! Scissors beats paper.
>>>
"""
