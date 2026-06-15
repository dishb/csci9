"""
Week 3: program 13
A program that displays the characters in the ASCII character table from ! to ~.
Python 3.14.2
Dishant Bhandula
"""

count = 0
for x in range(33, 127):
    print(chr(x), end = " ")
    count += 1
    if count == 10:
        print()
        count = 0

print()

"""
Sample run:

>>>
===================== RESTART: /Users/dishb/Documents/csci9/week_3/p13.py ====================
! " # $ % & ' ( ) * 
+ , - . / 0 1 2 3 4 
5 6 7 8 9 : ; < = > 
? @ A B C D E F G H 
I J K L M N O P Q R 
S T U V W X Y Z [ \ 
] ^ _ ` a b c d e f 
g h i j k l m n o p 
q r s t u v w x y z 
{ | } ~ 
>>>
"""
