                                                        # Carter Wrobel
                                                        # 9/19/17
                                                        # CS #186
                                                        # Section 1
'''
    This program will take the date format entered and it will change it
    into a differnet format
'''
print("Date Formatter")
print("              ")
date = input("Enter a date (yyyy,mm,dd): ")
date_list = date.split(",")
month = int(date_list[2])
year = int(date_list[0])
day = int(date_list[2])

if month == "01":
    month = str("January")
elif date == "02":
    month =  "February"
elif date == "03":
    month = "March"
elif date == "04":
    month = "Aril"
elif date == "05":
    month = "May"
elif date == "06":
    month = "June"
elif date == "07":
    month = "July"
elif date == "08":
    month = "Augvust"
elif date == "09":
    month = "September"
elif date == "10":
    month = "October"
elif date == "11":
    month = "November"
elif date == "12":
    month == "December"

print(str(month) + " " + str(day) + ", " + str(year))
