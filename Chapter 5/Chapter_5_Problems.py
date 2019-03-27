                                                        # Carter Wrobel
                                                        # 9/21/17
                                                        # CS #186
                                                        # Section 1
'''
    This program will go throguh the chapter 5 problems.
'''

# Problem 1
def cube(x):
    return  x*x*x
# We are assigning the cubic function to x and then we are cubing it.
x = cube(3)
print(x)
# x = 27

# Problem 2
def mod(a, b):
    mod = a % b
    return mod
# We are assigning the mod function to do modulus division and
# printing the remainder.
x = mod(32, 3)
print(x)
# x = 2

# Problem 3
def my_func(x):
    return 5*x-8
    x += 2
# We are assigning the my_func to the function we created and
# then plugging in a value to find x.
x = my_func(2)
print(x)
# x = 2

# Problem 4
def evaluate_quad(x, a, b, c):
    return a*x**2 + b * x + c
# We are creating a quadratic calculator for a set of numbers
x = evaluate_quad(2,4,3,1)
print(x)
# x = 23

# Problem 5
def repeat_string(str , times):
    return str * times
# We are assigning a repeat fucntion to repeat the string
# the user inputs
x = repeat_string("hello", 3)
print(x)
# x = hellohellohello

# Problem 6
def eval_quad(x,a=0,b=0, c=0):
    return a*x**2 + b * x + c
# We are creating a quadratic function and then printing it
x = evaluate_quad(2,4,3,1)
print(x)
# x = 23

# Problem 7
# def repeat_str(st="Hi" , num):
#    return st * num
# We are creating a repeat function repeating the str how
# ever many time we are asked to.
# x = repeat_str(3)
# print(x)
# x =

# Problem 8
import random
def pick_shape(n=0):
    if n!= 1 and n!=2:
        n=random.randint(1,2)
    s={1:'square',2:'circle'}
    return s[n]
# We are asking the computer to pick a random number and
# depending which one it picks it will say it is a circle
# or square
x = pick_shape()
print(x)
# x = circle or square

# Problem 9
def factorial(n):
    if n ==1:
        return 1
    return factorial(n-1) * n
# We are finding the factorial of the number input
x = factorial(5)
print(x)
# x = 120

# Problem 10
def sum_to(n):
    if n ==1:
        return 1
    return sum_to(n - 1) + n
# We are creating a sum to function based on what is entered
x = sum_to(5)
print(x)
# x = 15

# Problem 11
def shout(str):
    return str.upper()
# We are capitalizing the whole input
y = 'x'
x = shout(y)
print(x)
# x = X

# Problem 12
def shout():
    x.upper()
# Uppercase the first letter
x = "hey you!"
x = shout()
# It will return None
print(x)
# x = None

# Problem 13
def foo():
    y = "get it?"
    return
# they arent plugging in anything so it will return None
x = foo()
print(x)
# x = None

# Problem 14
def greeting():
    return "Good day sir."
# We are reassigning the variable
hello = greeting
x = hello()
print(x)
# x = Good day sir.

# Problem 15
def get_len(str):
    length = len(str)
    del str
    return length
a = "hello"
x = get_len(a)
print(x)
# x = 5

# Problem 16
def my_age(name, age = 35):
    result = "%s is %d years old" % (name, age)
    return result
# We taking the input and entering it into the line
# of code.
x = my_age(age=22,name= "Joe")
print(x)
# x = Joe is 22 years old

# Problem 17
def find_it(str):
    if "you" in str:
        return "found you"
    return "keep looking"
# We are printing whatever they enter with an if statement
a = "what are you looking for?"
x = find_it(a)
print(x)
# x = found you

# Problem 18
import math
def area_of_cir(radius):
    r = float(radius)
    return math.pi * r**2
# We are finding the area of a circle 
x = area_of_cir(3)
print(x)
# 28.274...

# Problem 19
def triangle_area(b=3,h = 5):
    return b*h/2
# We finding the area of a triangle
x = triangle_area()
print(x)
# x = 7.5
# Problem 20
def average(lst):
    return sum(lst)/len(lst)
# We are taking the sum of the list and dividing by the length
a = [1,3,5,7,9,12]
x = average(a)
print(x)
# x = 6.166...
