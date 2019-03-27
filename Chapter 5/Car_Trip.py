                                                        # Carter Wrobel
                                                        # 9/19/17
                                                        # CS #186
                                                        # Section 1
'''
    This program will calculate a trip cost based on a numerous
    amount of variables.
'''

def trip_cost(gas_tank, miles_travel, gas_cost, miles):
    mpg = miles // gas_tank
    gas_cost = gas_tank * gas_cost
    total_cost = (miles // miles_travel) * gas_cost
    return total_cost

a = int(input("What is the size of the gas tank: "))
b = float(input("What is the the number of miles that can be traveled: "))
c = float(input("What is the cost of gas per gallon: "))
d = float(input("What is the number of miles for the trip: "))

print(trip_cost(a, b, c, d))
