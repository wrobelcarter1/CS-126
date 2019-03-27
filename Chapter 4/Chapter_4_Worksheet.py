                                                        # Carter Wrobel
                                                        # //17
                                                        # CS #186
                                                        # Section 1
'''
    This program will work through all of the probelms on the Chapter 4
    Worksheet.
'''

# Problem 1
a = "apricot"
# The len() function will tell you how many letters there are and then *2
x = len(a)*2
print(x)
# x = 14


# Problem 2
a = "     arizona     "
# The a.strip() command wll strip the extra space and then the .capitalize()
# function will capitalize the first letter of the word
x = a.strip().capitalize()
print(x)
# x = Arizona


# Problem 3
a = True
b= False
# The "and" expression multiplies the two booleans and the "or" function adds
# them, the answer will be true or false based on whether the sides are a 1 or 0
x = b and a or a and b
print(x)
# x = False


# Problem 4
cats = 2
dogs = 13
# The += operator is a faster way to type code if you wanted to add whatever the
# value of cats was to dogs and reassigns the value to the first variable
# cats += dogs
x = cats
print(x)
# x = 15


# Problem 5
x = 16 - 4 * 3
# python uses order of operations like PEMDAS
print(x)
# x = 4


# Problem 6
x = 10 + 2 * 5 + 3 / 2
# Python uses order of operations like PEMDAS
print(x)
# x = 21.5


# Problem 7
x = "here" or "there"
# The "or" boolean will add the two 1s and produce the first true so "here"
print(x)
# x = here


# Problem 8
x = 2
y = 8
# Python uses the "**=" operator to shorten the code which means x^y
x **= y
print(x)
# x = 256

# Problem 9
x = 24 and 3600
# the "and" expression will and the two answers and print the higher one
print(x)
# x = 3600

# Problem 10
fahrenheit = float(90)
celsius = (fahrenheit - 32.0) * 5.0 / 9.0
x = celsius
# We assigned a value to fahrenheit and celsius and then reassigned one to a new # value
print(x)
# x = 32.22222...


# Problem 11
a = True
b = False
# We are setting the boolean expressions true and false with a the "or" command
x = a or b
print(x)
# x = True


# Problem 12
x = "{2}{1}{0}".format(False , "s" , 37)
# The .format command will take whatever is in the parentheses and put it in the # order assigned at the beginning, False = {0}, "s" = {1}, 37 = {2}
print(x)
# x = 37sFalse


# Problem 13
a = "hello THERE     "
x = a[0:5].upper()
# The .upper() command will capitalize the whole value assigned so in this case # it is [0:5] which corresponds to the whole word "hello" and then the .lower() 
# command will lower the letters in "THERE" and strip the extra space.
x += a [5:].lower().strip()
print(x)
# x = HELLO there

# Problem 14
a = 3.141567
x = round(a,2)
# The round(,) command rounds the value stored in the varible to however many 
# places you tell it to and then the %0.2f command prints the value to 2 decimal # places, while the %i just prints the integer and the %g just prints the whole # value.
print("%0.2f %i %g" %(a, a, x))
# x = 3.14 3 3.14


# Problem 15
y = [True, False, True, True]
x = y[1] and y[3]
# You are saving the list under "y" and then you are recalling the values of 
# y[1] and y[3] and using the "and" boolean to get a True or False
print(x)
# x = False


# Problem 16
x = len("snails"*3)
# The len() function tells you how many characters the variable is taking up and # then it is multiplying it by 3
print(x)
# x = 18


# Problem 17
y = 8
if y%2:
    x = "even"
else:
    x = "odd"
# We are using an if stement to test is 8 is divisable by 2 and if it is then we # print "even" and if not using the else statement it is "odd"
print(x)
# x = odd





# Problem 18                            ????????
x = "Disney Land" or 1776 and 34
#
print(x)
# x = Disney Land


# Problem 19
x = 7
y = 2
# We are using order of operations to find 7/2 which is 3 without the remainder  # then we add 4 to get 7
x = x // y + 4
print(x)
# = 7


# Problem 20
y = 13
x = y % 2 + 5 // 2
# We are using the Modulous operator to divide 13/2 to get the remainder which  # is 1, then we are adding 5 // 2 which is 2 so the answer is 3
print(x)
# x = 3




