                                                        # Carter Wrobel
                                                        # 9/19/17
                                                        # CS #186
                                                        # Section 1
'''
    This program will tell you how fast you must run to finish the
    marathon in the average time
'''
print("Marathon Calculator")
print("                   ")

# List example (One line of code getting the input) \/
'''
time_str = input("Enter time (HH:MM:SS): ")
time_list = time_str.split(":")
print(time_str, time_list)
hours = int(time_list[0])
minutes =int(time_list[1])
seconds = int(time_list[2])
'''

hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

minutes = float(minutes / 60)
seconds = float(((seconds / 60)/60))
time = round((hours + minutes + seconds),3)
speed = round((26.2 / time),3)
print("You must run about " + str(speed) + " mph.")
    


