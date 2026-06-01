# input.py
# Dishant Bhandula
# 5/30/26
# Python 3.14.2
# Description: Program to take input in Python

name = input ("Please enter Your Name: ") # this is a string
weightLbs = float(input ("Please enter Your weight in lbs: ")) # a float
age = int (input ("Please enter your age (whole number): " )) # an integer
weightKg= weightLbs*0.453592
title = "Human"

print ("Hello", title, name, "your weight is")
print ( weightLbs, "lbs")
print ("which equals = %.2f" %weightKg, end=' ') # end=' ' prevents new line
print ("kilograms ")

'''
>>>
===================== RESTART: /Users/dishb/Downloads/p3.py ====================
Please enter Your Name: Dishant Bhandula
Please enter Your weight in lbs: 160
Please enter your age (whole number): 17
Hello Human Dishant Bhandula your weight is
160.0 lbs
which equals = 72.57 kilograms
>>>
'''
