                                                        # Carter Wrobel
                                                        # 9/12/17
                                                        # CS #186
                                                        # Section 1
'''
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

