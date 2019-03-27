                                                        # Carter Wrobel
                                                        # 9/12/17
                                                        # CS #186
                                                        # Section 1
'''
    Problem 3-2
    This program will ask the user to enter a color, then output the
    complementary color back to the user.
'''

color = input("Enter a color (red, blue or yellow): ")

if color == "blue" :
    print("The complementary color to blue is orange.")
elif color == "red" :
    print("The complementary color to red is green.")
elif color == "yellow" :
    print("The complementary color to yellow is violet.")
else:
    print("You did not enter blue, red or yellow.")
          



'''
    Problem 3-4
    This program will ask the user to enter an integer, then it will tell
    the user if the integer is even or odd.
'''


integer = int(input("Enter an integer to check if it is even or odd: "))

if (integer%2) == 0:
    print("The number " + str(integer) + " is an even number.")
else:
    print("The number " + str(integer) + " is an odd number.")




'''
    Problem 3-5
    This program will ask the user for a numerical value for a grade and
    then tell the user the letter grade they recieved.
'''

grade = int(input("Enter the grade: "))

if 100 >= grade >= 90:
    print("Your grade is an A")
elif 90 > grade >= 80:
    print("Your grade is a B")
elif 80 > grade >= 70:
    print("Your grade is a C")
elif 70 > grade >= 60:
    print("Your grade is a D")
elif 60 > grade:
    print("Your grade is a F")
else:
    print("You did not enter a grade value.")




'''
    Problem 3-18
    This program will calculate the bill based on the value of the service plus
    the total before the tip.
'''

total = float(input("Enter the total bill before tip: "))
tip = input("How was your service? poor, good or excellent?: ")

if tip == "poor":
    tip_amount = 0.15
elif tip == "good":
    tip_amount = 0.2
elif tip == "excellent":
    tip_amount = 0.25
else:
    print("You did not enter a correct answer!")

total_tip = total * tip_amount
total_bill = total_tip + total
total_bill = str(round(total_bill, 2))

print("The total bill with the tip is $" + str(total_bill))

