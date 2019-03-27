# Carter Wrobel
# CS126
# 9/7/17
'''
This is all of the problems for the Chapter 3 worksheet
'''

# Problem 1
a = 27
b = 23
# 27 is stored as the variable "a" and 23 is stored as the varible "b"
# We use the "-" operator to subtract the to and store that value as "x"
x = a - b
print(x)

# Problem 2
a = 27
b = 23
# the variable "b" is reassigned to the value of "a" so it is "a - a" which is 0
b = a
x = a - b
print(x)

# Problem 3
a = 2**8
b = 2
# The "**" operator is the ^ operator so it really means 2^8 
x = a * b
print(x)

# Problem 4
a = 2*8
b = 8**2
# The difference between the two variables is a = 2 x 8 and b = 8^2
x = a-b
print(x)

# Problem 5
a = 13
b = 10
# The % in python give the reminder after divison of the two variables 
x = a % b
print(x)

# Problem 6
mike = 11
bob = 10
# Same situation as problem 5, 11/10 should give a remanider of 1, just different variables
x = mike % bob
print(x)



# Problem 7
a = 5
b = 8
# The operator ">+" means if the left is greater than or equal to the right. It will display a true or false.
x = ( a>= b)
print(x)
# Problem 8
a = 5
b = 5
# The "==" is testing if the variable on the left is equivalent to the one on the right
x = ( a == b)
print(x)
# Problem 9
x = 12
y = 2
# The "/" operator divides the two variables. the answer should be 6 
x = x / y
print(x)

# Problem 10
x = 3
y = 3
# The "!=" means is not equal to so it will compare both sides and put out a true or false statement
x = ( x != y)
print(x)

# Problem 11
name = "Peter Parker"
# The words "Peter Parker" is assigned to the variable "name", when you assign letters to a variable
# each letter gets a number value and since this problem says [0:5] "Peter" should print
x = name[0:5]
print(x)

# Problem 12
name = "Norman Osborn"
# We are using the [0:5] to print the name "Norman" and then [5:] to print "Osborn" and joinging
# them with a plus sign
x = name[0:5] + name[5:]
print(x)

# Problem 13
greeting = "Hello there! "
greeting = greeting *3
# The * command will times the variable by 3 so it will print "Hello there!" 3 consecutive times
x = greeting
print(x)

# Problem 14
a = "Hey"
yelling = a.upper()
# The "variable.upper()" command takes whatever the variable is and makes everything uppcase letters.
x = yelling
print(x)

# Problem 15
a = "hey"
# The "variable.capitalize()" command takes the first letter of the word and capitalizes it
x = a.capitalize()
print(x)

# Problem 16
a = "    Hello there.    "
print(a.strip())
# The "variable.strip()" command will take the unecessary spaces out of the string
x=a
print(x)

# Problem 17
y = 13
# The "<" command is if the variable on the left is less than the one on the right and it will show true or false
x = y < 22
print(x)

# Problem 18
y = 13
# The ">" and "<" will test is the variable is greater than or less than the given values and based on the results it will and them
x = y < 22 and y > 10
print(x)

# Problem 19
x = "race"
# The "+" operation will combine the two string since they are not integers and it will make one word, "racecar"
x = "car" + "race"
print(x)

# Problem 20
x = True and False
# this will and the value of true and false will be false (Boolean Expression)
print(x)

