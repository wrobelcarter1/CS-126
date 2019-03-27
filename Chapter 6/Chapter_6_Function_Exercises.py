                                                        # Carter Wrobel
                                                        # 10/5/17
                                                        # CS #186
                                                        # Section 1

# Problem 1
# This program will ask the user to enter a list of numbers.
# Then it will take the lowest number of the list and return it.

def lowest_value(list1):
    list1.sort()
    z = list1[0]
    print(list1)
    print(z)

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
z = int(input("Enter a number: "))

a = [x, y, z]
lowest_value(a)

# The way the program would change is if you wanted more than
# 3 numbers you would add another variable and add that to the
# list to be sorted and take the lowest one. If you wanted to
# return the highest value of the list you would print list[-1]
# not list1[0] to get the last number not the first one.



# Problem 2
# This function will compare two lists to see if any of the values
# inside the lists are equal.

def equal_lists(list1, list2):
    a = list1[0]
    b = list1[1]
    c = list1[2]
    if a in list2:
        print("True")
    elif b in list2:
        print("True")
    elif c in list2:
        print("True")
    else:
        print("False")

a = int(input("Enter a number for list 1: "))
b = int(input("Enter a number for list 1: "))
c = int(input("Enter a number for list 1: "))

list1 = [a, b, c]

x = int(input("Enter a number for list 2: "))
y = int(input("Enter a number for list 2: "))
z = int(input("Enter a number for list 2: "))

list2 = [x, y, z]

equal_lists(list1, list2)


# Problem 3
# This program will ask the user to input a grade level,
# and it will return how many credits they need for that
# class level

def grade_level(level):
    grade_dic = { 'Freshman' : 0 ,
           'Sophomore' : 30 ,
           'Junior' : 60 ,
           'Senior' : 90 }

    print (grade_dic[level])

level = input("Enter your grade level: ")
level = level.capitalize()

grade_level(level)


















