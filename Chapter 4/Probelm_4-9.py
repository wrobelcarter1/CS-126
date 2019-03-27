                                                        # Carter Wrobel
                                                        # 9/19/17
                                                        # CS #186
                                                        # Section 1
'''
    This program will ask the user for the amount of cents they have and
    that should be dispensed to the customer (in cents).
'''
# Function Example 
def make_change(amount):
    dollars = amount // 100
    quarters = (amount % 100) // 25
    dimes = (amount % 25) // 10
    nickels = (amount % 10) // 5
    pennies = (amount % 5) // 1
    print("Dollars: " + str(dollars))
    print("Quarters: " + str(quarters))
    print("Dimes: " + str(dimes))
    print("Nickels: " + str(nickels))
    print("Pennies: " + str(pennies))


print("Change Calculator")
print("                 ")
cents = int(input("Please enter the amount in cents: "))
make_change(cents) # Execute FUnction with user data


'''
dollars = amount // 100
quarters = (amount % 100) // 25
dimes = (amount % 25) // 10
nickels = (amount % 10) // 5
pennies = (amount % 5) // 1
print("Dollars: " + str(dollars))
print("Quarters: " + str(quarters))
print("Dimes: " + str(dimes))
print("Nickels: " + str(nickels))
print("Pennies: " + str(pennies))
'''
