                                                        # Carter Wrobel
                                                        # 9/26/17
                                                        # CS #186
                                                        # Section 1
'''
    This program will create a function that returns the
    second highest number of 3 numbers. Problem 5-6.
'''

def second_highest(num1,num2,num3): # Default arguments
    
    x = max(num1,num2,num3) # get the max, then find second max
    if x == num1:
        second_max = max(num2,num3) # if 1 is the max then the max is this
    elif x == num2:
        secomd_max = max(num1,num3) # if 2 is the max then the max is this
    else:
        second_max = max(num1,num2) # if 3 is the max then the max is this
    return second_max

print(second_highest(45,324,54))
'''
my_list = [num1, num2, num3]
my_list.sort()
return my_list[1] # Second highest after rearranged
'''


