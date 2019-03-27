                                                        # Carter Wrobel
                                                        # 9/19/17
                                                        # CS #186
                                                        # Section 1
'''
    This program will take the total amount of all of the items
    purchased and then calculate the tip based on the service.
    Also the function will take the tax rate and find the total
    with tax.
'''

def main():
    print(total_with_tip(total_cost, tip_amount))
    print(total_with_tax(total_cost))
    print(complete_cost(total_cost, tip_amount))


def total_with_tip(total_cost, tip_amount):
    total_tip = round((total_cost * tip_amount),2)
    return "The total tip is : $"+ str(total_tip)

def total_with_tax(total_cost):
    total = round((total_cost * 0.08),2)
    return "The tax amount is: $" + str(total)

def complete_cost(total_cost, tip_amount):
    tip = round((total_cost * tip_amount),2)
    tax = round((total_cost * 0.08),2)
    total = total_cost + tip + tax
    return "The total cost with tip and tax is: $" + str(total)








total_list = [ 7.99, 5.99, 2.35, 14.99, 2.99]
total_cost = sum(total_list)
tip = input("How was your service? poor, good or excellent?: ")

if tip == "poor":
    tip_amount = 0.15
elif tip == "good":
    tip_amount = 0.2
elif tip == "excellent":
    tip_amount = 0.25
else:
    print("You did not enter a correct answer!")

main()
