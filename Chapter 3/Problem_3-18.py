                                                        # Carter Wrobel
                                                        # 9/12/17
                                                        # CS #186
                                                        # Section 1
'''
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
