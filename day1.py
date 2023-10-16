"""
AN INTRODUCTION TO PYTHON

Python started in 1991.
- Python is used for software dev, web dev, data analysis. 
- It can be used on a server to create web applications. 
- It can also to be used on a software to create workflow.
- It can create database system.
- For handling big data.
- For production software development.

Why Python?
- compared to other prog langs, its very easy to use.
- its cross platform - windows,  linux, apple.
- It runs on an interpreter system
- its used for object oriented programming

Version?
most recent version is python 3

Download and installation - 

Comments
#
'''
'''
- it makes code more readable
- It can be a text that explains your code
- it can also be a code that you dont want to run

Variables - are containers for storing data
- They are case sensitive
- they can only contain Alphanumeric Characters and special symbol _
- it cannot be any of the python keywords
- you cant start with a number

Pascal Case = this is variable naming when dealing with class
MyName

Camel case - myNameHere

Snake Case - my_name_here

***DATA TYPES***
String
Int
float
Bool
complex
list
tuple

**Operators**
> Arithmetic Operators: 
+, -, /, *, %, **, //

> Python Assignment Operators
=, +=, -=, *=, !=, <, >, <=, >=, ==

*=, != are also called python comparism operator

> Logical Operators
and, or, not

> List in Python
list are ordered, changeable and allow duplicate items


"""
# this is a comment

"""
this is also another form of comment
"""

'''
this is also another comment
'''
# print("call 911")


# DATA TYPES
#STRING
greet = "hello world"
#print(greet)

#INTEGER
a = 22
#print(a)

#FLOAT
ab = 1.567
# print(ab)

#BOOL
my_decision = True
# print(my_decision)

# PYTHON LISTS
shopping_list = ["rice", "books", "pen"]
# print(shopping_list)
shopping_list2 = ["rice", 200, "pen", False]
# print(shopping_list2)

#TUPLES
cordinates = (1.228888, 1.999999, "east")
# print(cordinates)

greet = "Good morning"
# print(greet)

a = 1
# print(a)

#STRING FORMATTING
print(greet, a)
# print(greet + a) # NOTE THAT THIS DOES NOT WORK WHEN COMBINING STRINGS AND INTEGERS TOGETHER
greetings = f"Hello {greet} {a}, How was your night?"
print(greetings)