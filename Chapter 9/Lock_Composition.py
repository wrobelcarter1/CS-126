__author__ = "Dr. Vanderberg"

'''
Plan for a single lock digit
(1) Draw the UML
(2) Constructor (__init__) sets locked_value
    - how do we initialize the locked value?
    - remember it should only be 0-9
(3) Method that changes the self.locked_value --> updateValue(self,newValue)
   - only update self._value if self._is_locked == False
(4) Method that opens the lock. how?
    - open(self, value) returns True if value==self._value, else: False
(5) Any additional attribute or methods that might be helpful?
    - is_locked
    - how do we relock it?
    - print info about the locked value and locked/unlocked state
'''


# Comments show the plan for a single lock digit
'''
(1) Draw the UML diagram to represent the design before you implement it.
'''
class LockDigit:
    # (2) Constructor (__init__) sets locked_value
    #   how do we initialize the locked value? save it as an instance variable
    #   remember it must be between be 0-9, if it's not default the value to 5
    def __init__(self, digit):
        digit = int(digit)
        if 0 <= digit < 10:
            self._locked_value = digit
        else: # if digit is incorrect set value to 5
            self._locked_value = 5
        self._is_locked = True

    # (3) Method to change the locked_value --> updateValue(self,new_val)
    #    Only works if the lock is open
    #    new_val must be a digit between 0 and 9
    def updateValue(self, new_val):
        # if the lock is open, then you may update the locked_value
        # assuming the new_val is appropriate (0-9)
        new_val = int(new_val) 
        if self._is_locked==False and 0<= new_val <10:
            old_value = self._locked_value
            self._locked_value = new_val
            return "The old value is: " + str(old_value) + "\nThe new value is: " + str(self._locked_value)
        else:
            # print("Lock must be open & new value must be a single digit.")
            return False
        # TO DO: Refactor the code above so that it not only returns True or False
        #        but it returns the old lock digit (incase we need to "roll back" the change.)
            
    # (4) Method that open the lock.
    #    Opens lock digit (i.e., sets is_locked to False) if the correct value is passed in 
    def open(self, value_to_test):
         # returns True if value_to_test == self.locked_Value, else: False
        if self._locked_value == value_to_test:
            self._is_locked = False
            return True
        else: return False

    # (5) Any additional attribute or methods that might be helpful?
    #    is_locked: boolean that keeps track of whether the lock is open or closed
    #    how do we relock it? --> close()
    def close(self):
        self._is_locked = True

    # Defines what it means to convert the LockDigit to a string, which 
    # allows us to print info about the locked_value and locked/unlocked state
    def __str__(self):
        return "Lock info: the lock digit is " + str(self._locked_value) + " \nLocked?: " + str(self._is_locked) + "\n"


'''
 9-4: High level Plan for Lock composition (i.e, ThreeDigitLock)
 (1) How do we make a Lock? need three lockDigits
 (2) Constructor should take in a three digit code
 (3) Method to update the combo (i.e. three digit code)
 (4) Method that open the lock
 (5) Anything else?
'''
class ThreeDigitLock():
    # (1) Each lock needs three LockDigits
    #  need 3 attributes, each of type LockDigit
    #  instance or class member? each ThreeDigitLock has it's own individal code
    #  do we need any other attributes? --> is_open? 
    
    # (2) Constructor needs to create 3 LockDigits.
    #  need a varaiable for each that is initialize to a LockDigit object
    #  lockDigit objects need a value for initialization
    #  get this value from the 3 digit input code (code[0],code[1],code[2])
    #  set variable to newly created LockDigit object for each
    def __init__(self, three_digit_code):
        # initialize three lock digit objects, code should be a string
        self._lock_digit_one = LockDigit(three_digit_code[0])
        self._lock_digit_two = LockDigit(three_digit_code[1])
        self._lock_digit_three = LockDigit(three_digit_code[2])
        
        # TO DO: Refactor this class so that it has a method called is_open() (instead of 
        #       the boolean) that checks if each LockDigit is open. If so, it should return True
        self.is_open = False # assume lock is locked when created
        
    def is_open(self):
        if self.is_open == True:
            return True
        else:
            return False
    
    # (3) To update the combo of the 3 digit lock we need to update each lockDigit's value
    #   (e.g., lockDigit1.updateValue(some_value)). We should update each lockDigit using the
    #   three digit code passed in.
    def updateCombo(self, three_digit_code):
        # TO DO: Can you check to make sure input is 3 digits long? Add the code to do so
        #       If not, call another function that promotes user to input the code again.
        # Update the value of each lock digit using updateValue method
        if self.is_open == True:
                result1 = self._lock_digit_one.updateValue(int(three_digit_code[0]))
                result2 = self._lock_digit_two.updateValue(int(three_digit_code[1]))
                result3 = self._lock_digit_three.updateValue(int(three_digit_code[2]))
                if result1 and result2 and result3:
                    print("all lock digits have been updated")
                else:
                    print("not all digits have been updated - lock may be partially opened")
                    # TO DO: Refactor so that if any LockDigit doesn't open we rollback the attempt
        else:
                print("Lock must be open to change the combo")
                
    # (4) To open three digit lock each LockDigit must open
    #  use three digit code like in __init__ and updateCombo
    #  check if LockDigit1.open(code[0]) then check other two
    #  the lock only open if they ALL open (i.e., return True)
    #  Tries to open each lock digit. If unsuccessful close all digits. 
    def open(self, three_digit_code):
        # try to open each lock digit
        if self._lock_digit_one.open(int(three_digit_code[0])) \
        and self._lock_digit_two.open(int(three_digit_code[1])) \
        and self._lock_digit_three.open(int(three_digit_code[2])):
            self.is_open=True
            print("The lock is open.")
        else:  # if digits don't all open make sure they are all closed
            self.close() #calls another function in this class (i.e., the ThreeDigitLock class)
            print("Wrong combo entered.")
           
    # Closes each lock digit by using LockDigit close() method 
    def close(self):
        self._lock_digit_one.close()
        self._lock_digit_two.close()
        self._lock_digit_three.close()

    # print lock info using str(lock_digit)  
    def __str__(self):
        result = str(self._lock_digit_one) + str(self._lock_digit_two)
        result += str(self._lock_digit_three)
        return result


# You may also like to play with the NdigitLock class
'''
 9-5: High level Plan for Lock composition (i.e, NdigitLock)
 (1) How do we make a Lock? need multiple lockDigits
 (2) Constructor should take in a code and create one LockDigit for each digit in the code
 (3) Method to update the combo (i.e. need n digit code)
 (4) Method that open the lock
 (5) Anything else?
'''
class NdigitLock:
    def __init__(self, combo):
        self._size = len(combo) #store the length of the code
        self._n_digit_lock = [] #to hold lockDigits
        # initialize lock digits
        for i in combo:
            current_lock_digit = LockDigit(int(i)) # create the object
            self._n_digit_lock.append(current_lock_digit)  # add the object to the list

        
    def setCombo(self, new_code):
        # new combo must have same numer of digits
        if len(new_code) != self._size:
            print("Wrong number of digits.")
        else:
            index = 0
            for lock_digit in self._n_digit_lock:
                lock_digit.updateValue(int(new_code[index]))
                index+=1
                # TO DO: Refactor this to avoid paritially updating the combo
                
    def __str__(self):
        result=""
        for i in range(self._size):
            result+= str(self._n_digit_lock[i])
        return result

    def openLock(self):
        for i in range(self._size):
            d = int(input("Enter a digit: "))
            if self._n_digit_lock[i].open(d):
                pass
            else:
                print("Incorrect Combo")
                # TO DO: Refactor this to avoid paritially open locks
                return False
        return True
                    

def main():

    # test LockDigit class
    lock_one = LockDigit(3)
    print(lock_one)
    print(lock_one.open(5)) # False
    print(lock_one.updateValue(7))# shouldn't update wrong value and lock is locked so False
    print(lock_one.open(3)) # True
    print(lock_one.updateValue(7))# should update True
    lock_one.close()
    print(lock_one)

    # test ThreeDigitLock class
    myLock = ThreeDigitLock("123")
    print(myLock)
    myLock.open("125")
    
    myLock.open("253")
    print(myLock)
    myLock.open("123")
    myLock.updateCombo("1235")
    print(myLock)
'''
    # test NdigitLock class
'''
main()
