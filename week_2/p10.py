"""
Week 2: program 10
A program that asks the user for day and month of a birthday.
Python 3.14.2
Dishant Bhandula
"""

month = int(input("Enter your birth month as a number (1-12): ").strip())
day = int(input("Enter your birth day as a number: ").strip())
zodiac = "Unknown"

if (month == 3 and day >= 21) or (month == 4 and day <= 19):
    zodiac = "Aries"
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    zodiac = "Taurus"
elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
    zodiac = "Gemini"
elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
    zodiac = "Cancer"
elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    zodiac = "Leo"
elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    zodiac = "Virgo"
elif (month == 9 and day >= 23) or (month == 10 and day <= 23):
    zodiac = "Libra"
elif (month == 10 and day >= 24) or (month == 11 and day <= 21):
    zodiac = "Scorpio"
elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
    zodiac = "Sagittarius"
elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
    zodiac = "Capricorn"
elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
    zodiac = "Aquarius"
elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
    zodiac = "Pisces"

print(f"Your zodiac sign is: {zodiac}")

"""
Sample run:

>>>
===================== RESTART: /Users/dishb/Documents/csci9/week_2/p10.py ====================
Enter your birth month as a number (1-12): 5 
Enter your birth day as a number: 18
Your zodiac sign is: Taurus
>>>
"""
