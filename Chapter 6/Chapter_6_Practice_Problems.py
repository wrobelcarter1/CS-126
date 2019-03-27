                                                        # Carter Wrobel
                                                        # 9/19/17
                                                        # CS #186
                                                        # Section 1
'''
    This program will go through the chapter 6 problems.
''' 

# Problem 1
def access (alist, index ):
    return alist[index]
# We will take the list and first value of the list
print(access([1,2,3], 0))
# 1

# Problem 2
def insert(alist, i, value):
    newlist = alist
    newlist.insert(2,11)
    return newlist
# This function will take the list generated an insert the number
# 11 in the 2 position
print(insert([1,10,14],2,11))
# [1, 10, 11, 14]

# Problem 3
def two_d(strs, n1, n2, n3):
    return strs[n1][n2:n3]
# This problem will takew the word inputted and print the last 3 letters
food = ["potatoes", "onions"]
print(two_d(food, 1, 3, 6))
# ons

# Problem 4
def get_length(aset):
    return len(aset)
# This function will print the length of the set
print(get_length({2,3,3,3,4}))
# 3

# Problem 5
def side_effect(mylist):
    mylist.sort()
# This function will sort the values in order, only if they are ints
num_strs = ["10","22","9","8"]
side_effect(num_strs)
print(num_strs)
# ["10","22","9","8"]

# Problem 6
l_o_d = [{"name" : "Bella Swab" ,
          "race" : "Vampire"},
         { "name" : "Jacob Wolf" ,
           "race" : "Werewolf" }]
# This program will use the get_length function
# to find the length of l_o_d
print(get_length(l_o_d))
# 2

# Problem 7
l_o_d.append({'name':'Casper'
              ,'race':'Ghost'})
# This program will add the l_o_d to the new variable
# and print the length
print(get_length(l_o_d))
# 3
             
# Problem 8
print(l_o_d[1]["race"])
# This will print the second 'race' assigned
# Werewolf


# Problem 9
def add_to_dict(d,key,val):
    d[key] = val
# This function takes a dictionary and adds another key and value to it
d = {"a":"b","c":"d"}
add_to_dict(d,"key","value")
print(d)
# {'a': 'b', 'c': 'd', 'key': 'value'}

# Problem 10
def update_tup(index, value):
    t[index] = value
# You cant update a tuple
t=(11,12,13)
print(update_tup(0,111))
# Error

