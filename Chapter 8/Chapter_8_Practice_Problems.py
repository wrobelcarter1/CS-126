                                                        # Carter Wrobel
                                                        # 10/18/17
                                                        # CS #186
                                                        # Section 1
'''
    This program will go through the practice problems for chapter 8
'''


# Problem 1
fh = open("cs_desc.txt", "r")
x = fh.read()
print(x)
# The entire text file will print


# Problem 2
fh = open("cs_desc.txt", "r")
lines = fh.readlines()
x = lines[2]
fh.close()
print(x)
# The 2. bullet point will print


# Problem 3
fh = open("cs_desc.txt", "w")
fh.write("Check out NAU")
fh.close()
# This adds the test "Check out NAU." to the file
fh = open("cs_desc.txt", "r")
x = fh.readline()
fh.close()
print(x)
# "Check out NAU"


# Problem 4
fh = open("cs_desc.txt", "a")
fh.write("\nCheck out NAU")
fh.close()

fh = open("cs_desc.txt", "r")
lines = fh.readlines()
x = lines[6]
fh.close()
print(x)
# ERROR index out of range, there is nothing on line 6

# Problem 5
fh = open("cs_desc.txt", "a")
x = fh.readline()
fh.close()
print(x)
# ERROR, you cant read it when calling "a" only when you call "r"


# Problem 6
fh = open("cs_desc.txt", "w")
for i in range(3):
    fh.write(i)
x = i
fh.close()
print(x)

# Problem 7
fh = open("cs_desc.txt", "r")
x = fh.readline()
x = len(x)
fh.close()
print(x)
#


# Problem 8
fh = open("cs_desc.txt", "r")
x = fh.readlines()
x = len(x)
fh.close()


# Problem 9
fh = open("cs_desc.txt", "r")
lines = fh.readlines()
for i in lines:
    x = i
    fh.write(i)
fh.close()
print(i)
#


# Problem 10
fh = open("cs_desc.txt", "r+")
lines = fh.readlines()
for i in range(len(lines)):
    fh.write(str(i))
x = fh.readline()
fh.close()
print(x)
#

