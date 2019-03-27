# Lab 3 Math Quiz
# Carter Wrobel, Dakota Templeton
# cjw446, dpt38
# 10/2/17
# Section 1

# This program will use mathematical operators to create a simple math quiz
#

from random import randint

level = input("Choose a level: Beginner, Intermediate or Advanced: ")

if level == "Beginner":
    x = int(input("How many questions would you like (1-10)?: "))
    correct = 0
    for i in range(x):
        n1 = randint(1, 10)
        n2 = randint(1, 10)
        total = n1 + n2

        ans = input("What is %d + %d?: " % (n1, n2))
        if int(ans) == total:
            print("That is correct!.\n")
            correct = correct + 1
        else:
            print("No, the answer is %d.\n" % total)

    print("I asked you %d questions. You got %d of them right!" % (x, correct))
    print("Well Done!")

elif level == "Intermediate":
    x = int(input("How many questions would you like (1-10)?: "))
    correct = 0
    for i in range(x):
        n1 = randint(1, 25)
        n2 = randint(1, 25)
        total = n1 * n2

        ans = input("What is %d * %d?: " % (n1, n2))
        if int(ans) == total:
            print("That is correct!.\n")
            correct = correct + 1
        else:
            print("No, the answer is %d.\n" % total)

    print("I asked you %d questions. You got %d of them right!" % (x, correct))
    print("Well Done!")
else:
    x = int(input("How many questions would you like (1-10)?: "))
    correct = 0
    for i in range(x):
        n1 = randint(1, 50)
        n2 = randint(1, 50)
        total = float(round(((n1 ** 2) / n2), 2))

        ans = float(input("What is ((%d ^ 2)/ %d)(2 places):" % (n1, n2)))
        if float(round((ans), 2)) == total:
            print("That is correct!.\n")
            correct = correct + 1
        else:
            print("No, the answer is %d.\n" % total)

    print("I asked you %d questions. You got %d of them right!" % (x, correct))
    print("Well Done!")
