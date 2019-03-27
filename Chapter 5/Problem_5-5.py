                                                        # Carter Wrobel
                                                        # 9/26/17
                                                        # CS #186
                                                        # Section 1
'''
    This program will take a set of numbers and will
    return true or false based on if the last digit of
    each number is eqaul or not. Problem 5-5.
'''

def last_digit(num1, num2, num3):
    d1 = abs(num1) % 10
    d2 = abs(num2) % 10
    d3 = abs(num3) % 10
    if d1 == d2 == d3:
        return "True"
    else:
        return "False"
print(last_digit(2, 43, 743))


'''
    d1 = str(num1)[-1]
    d2 = str(num2)[-1]
    d3 = str(num3)[-1]
'''

    

