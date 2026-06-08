"""
Week 2: program 9
A program to determine if the user can vote
Python 3.14.2
Dishant Bhandula
"""

age = int(input("Enter your age: "))
citizenship = input("Are you a citizen of the country? (Y/n): ").strip().lower()
registered = input("Are you registered to vote? (Y/n): ").strip().lower()

if age >= 18 and citizenship == 'y' and registered == 'y':
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote. Reason(s):")
    if age < 18:
        print(" - Not 18 or above.")
    if citizenship != 'y':
        print(" - Not a citizen.")
    if registered != 'y':
        print(" - Not registered to vote.")

"""
Sample run:

>>>
===================== RESTART: /Users/dishb/Documents/csci9/week_2/p9.py ====================
Enter your age: 19
Are you a citizen of the country? (Y/n): y
Are you registered to vote? (Y/n): y
You are eligible to vote.
>>>

>>>
===================== RESTART: /Users/dishb/Documents/csci9/week_2/p9.py ====================
Enter your age: 17
Are you a citizen of the country? (Y/n): y
Are you registered to vote? (Y/n): y
You are not eligible to vote. Reason(s):
 - Not 18 or above.
>>>

>>>
===================== RESTART: /Users/dishb/Documents/csci9/week_2/p9.py ====================
Enter your age: 17
Are you a citizen of the country? (Y/n): n
Are you registered to vote? (Y/n): y
You are not eligible to vote. Reason(s):
 - Not 18 or above.
 - Not a citizen.
>>>

>>>
===================== RESTART: /Users/dishb/Documents/csci9/week_2/p9.py ====================
Enter your age: 17
Are you a citizen of the country? (Y/n): n
Are you registered to vote? (Y/n): n
You are not eligible to vote. Reason(s):
 - Not 18 or above.
 - Not a citizen.
 - Not registered to vote.
>>>
"""
