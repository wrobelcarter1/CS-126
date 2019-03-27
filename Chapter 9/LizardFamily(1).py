'''
(1) Design an object of your choice. Start by using UML and planning the functionality of each method. Initialization of an object must require at least one parameter. You must be able to print your object in a meaningful way and you should define what it means for two objects to be equal. Additionally, your object must do one trick (e.g., generate a random number). 

(2) Implement a Class in Python for your newly designed object.

(3) Create three objects: two that are equivalent and one that is not. Show this is the case.
'''

import random

class Lizard:
    ''' 
    Lizards can change color. 
    '''
    # class member variable
    color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
    
    #initlaize lizard witha name and color
    def __init__(self, p_name, p_color):
        self._name = p_name
        self._color = p_color
        #print(p_name)
      
    # returns the name of the Lizard
    def get_name(self):
        # if you try access p_name here, 
        #    you will get an error.
        #print(p_name)
        return self._name
    
    # updates the names of the lizard
    def set_name(self, new_name):
        if new_name[0].upper() =='L':
            self._name = new_name
        else:
            print("New lizard names must start with L.")
    
    # lizards can change color
    # uses class member variables to ensure all lizard have same options
    def do_trick(self):
        self._color = Lizard.color_list[random.randint(0,5)]
        
    def __str__(self):
        result = "Lizard's name is: " + self._name
        result += " and its color is: " + self._color + "\n"
        # result = 1
        return result
    
    def __eq__(self, other):
        # two lizards are equal if they are same color
        if self._color == other._color:
            return True
        else: 
            return False

class LizardFamily:
    '''
    A lizard family is made up of multiple Lizards.
    '''
    
    def __init__(self, size):
        self._list_of_lizards = []
        for i in range(size):
            lizard = self._create_lizard()
            self._list_of_lizards.append(lizard)
            #self._list_of_lizards.append(self._create_lizard())
    
    # helper methods to create lizard for a given size family
    # should only be called from within the LizardFamily class
    def _create_lizard(self):
        name = input("Enter lizards name: ")
        color = input("Enter lizards color: ")
        new_lizard = Lizard(name,color)
        return new_lizard
        
    def change_colors(self, which_lizard):
        self._list_of_lizards[which_lizard].do_trick()
        # can you make all lizards changes colors
        #for lizard in self._list_of_lizards:
        #    lizard.do_trick()
        
    def __str__(self):
        print("This Lizard family contains...")
        result = ""
        for lizard in self._list_of_lizards:
            result += str(lizard)
        return result



# using the Lizard class directly
lenny = Lizard("Leonard", "red")
print(lenny.get_name())
print(lenny)
jenny = Lizard("Jennifer", "green")
lizzy = Lizard("Elizabeth", "red")
print(lenny == lizzy) #
print(lenny == jenny) #
print("Before trick -->", lizzy)
lizzy.do_trick()
print("After trick -->", lizzy)

# using the Lizard Family class, which creates Lizard objects
lazy_lizards = LizardFamily(2)
lazy_lizards.change_colors(1)
print(lazy_lizards)




