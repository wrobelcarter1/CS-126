                                                        # Carter Wrobel
                                                        # 10/18/17
                                                        # CS #186
                                                        # Section 1
'''
    This program will go through the practice problems for chapter 7
'''

# Problem 1
a = [1, 10, 14]
for i in a:
    print(i)
# This will print out the list
# 1
# 10
# 14


# Problem 2
a = [1, 10, 14]
for i in a:
    print(i, end = " ")
# This will print the list on the same line with a space
# 1 10 14


# Problem 3
a = [1, 10, 14]
for i, j in enumerate(a):
    print(i)
# Enumerate will take the list and tell you the positions inside it
# 0
# 1
# 2


# Problem 4
x = "hello"
for i in x:
    print(i, end = " ")
# This will take the string hello and put spaces between the letters
# h e l l o


# Problem 5
a = []
for i in range(0, 10, 2):
    a.append(i)
print(a)
# It will count from 0-10 skipping by 2 but it wont include 10
# [0, 2, 4, 6, 8]


# Problem 6
a = {
    "name" : "Bella Swam",
    "likes" : ["Ed", "Jake"]
    }
for b in a["likes"]:
    print(b)
# It will print the list assigned to "likes" in the dictionary
# Ed
# Jake


# Problem 7
a = {
    42: "pirates",
    11: "ninjas",
    }
for i, j in a.items():
    print(j, i)
# This woll take the value assigned and show it then the key next to it
# pirates 42
# ninjas 11


# Problem 8
a = {
    42: "pirates",
    11: "ninjas",
    }
for i in a:
    print(i)
# This will print the dictionary keys
# 42
# 11


# Problem 9
a = {}
for i in range(0, 10, 2):
    a[i] = i * 100 + 11
print(a)
# This will take the list and the values 0,2,4,6,8 and assign them
# to a value that is the key *100 + 11
# {0: 11, 2: 211, 4: 411, 6: 611, 8: 811}


# Problem 10
a = {}
for i in range(0, 4):
    b = []
    for j in range(0, 4):
        b.append(j)
    a[i] = b
print(a)
# This will take list of 0-3 and assign each value the set 0,1,2,3 to
# each value in a dictionary
# {0: [0, 1, 2, 3], 1: [0, 1, 2, 3], 2: [0, 1, 2, 3], 3: [0, 1, 2, 3]}


# Problem 11
a = [{
    "name": "Bella Swan",
    "race": "Vampire"
    },
    {
    "name" : "Jacob Black",
    "race" : "Werewolf"
    }]
for b in a:
    print(b["name"])
# This will print both names in the dictionary
# Bella Swan
# Jacob Black


# Problem 12
a = ['apple', 'orange',
     'kiwi', 'pear']
count = 0
for fruit in a:
    if fruit[0] in 'aeiou':
        continue
    else:
        count +=1
print(count)
# This will go through each fruit name and check if there are vowels
# in it or not and then add up all the vowels
# 2
    

# Problem 13   *****
x = 3
while (x<10):
    x = x*2
print(x)
# 
# 12


# Problem 14  *****
x = "CS 126"
while (x != ""):
    x = x[1:]
print(x)
# 
# " "



# Problem 15
mylist = []
x = 0
while (not mylist):
    mylist.append(x)
    x += x
print(mylist)
# It will return 0 inside of the list [0]
# [0]


# Problem 16
total = 0
while True:
    total += 1
    if total > 10:
        break
print(total)
# it will add one each time and once it is bigger than 10 it
# will break out so 11 is the final answer
# 11


# Problem 17
count = 0
a = 5
b = 0
while (a or b):
    a -= 1
print(a or b)
# the output will be 1 because the statement will be true which is a 1
# but then we subtract 1 so we get 0
# 0


# Problem 18
animals = ["bear", "cat", "dog"]
while "bear" in animals:
    print("ROAR")
    del animals[-1]
# This code will execute 3 times
# ROAR
# ROAR
# ROAR


# Problem 19
nums = []
while len(nums)<5:
    nums.append(len(nums))
print(nums)
# It will create a list from 0-4
# [0, 1, 2, 3, 4]


# Problem 20
x = "hello"
while len(x)< 16:
    x = x*2
print(x)
# It will print hello 4 times because the first time it will go twice
# then it still will be less than 16 chracters so it will again and it
# will be printed 4 times before it ends
# hellohellohellohello

