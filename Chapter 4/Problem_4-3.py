                                                        # Carter Wrobel
                                                        # 9/19/17
                                                        # CS #186
                                                        # Section 1
'''
    This program will ask the user for the coordinates of a point and
    y - intercept and then caclulates the slope.
'''

print("This is a Slope calculator!")
print("                           ")
x = int(input("Enter the x value: "))           
y = int(input("Enter the y valiue: "))           
y_intercept = int(input("Enther the y-intercept: "))

slope = int((y - y_intercept) / x)
print("The slope of this equation is " + str(slope) + ".")
