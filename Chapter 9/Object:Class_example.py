class Car():
    
    # This method is executed when we create the object
    def __init__(self, price, miles):
        # gives each car a price and # of miles
        self.price = price
        self.odometer_reading = miles

    # This method gives the object behavior - it can drive
    # which impacts the odometer reading, so we update it
    def drive(self, how_far):
        self.odometer_reading += how_far

    # defines how this onject should be printed
    def __str__(self):
        return "The car that costs " + str(self.price) + " dollars" \
               " has "+ str(self.odometer_reading) + \
               " miles on it."

car1 = Car(1000, 100000)
print(car1)
car1.drive(10)
print(car1)
