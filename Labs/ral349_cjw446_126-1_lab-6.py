# Lab 6 - Banners

# Rebecca Leggett and Carter Wrobel

# ral349 and cjw446

# 10-23-17

# Section 1


# The dictionary contains the banners for each letter of the alphabet,
# which will be accessed by the print_banner function
letters = {"A": ["#####",

                 "#   #",

                 "#####",

                 "#   #",

                 "#   #"],

           "B": ["#####",

                 "#   #",

                 "#####",

                 "#   #",

                 "#####"],

           "C": ["#####",

                 "#    ",

                 "#    ",

                 "#    ",

                 "#####"],

           "D": ["#####",

                 "#   #",

                 "#   #",

                 "#   #",

                 "#####"],

           "E": ["#####",

                 "#    ",

                 "#####",

                 "#    ",

                 "#####"],

           "F": ["#####",

                 "#    ",

                 "#####",

                 "#    ",

                 "#    "],

           "G": ["#####",

                 "#    ",

                 "# ###",

                 "#   #",

                 "#####"],

           "H": ["#   #",

                 "#   #",

                 "#####",

                 "#   #",

                 "#   #"],

           "I": ["#####",

                 "  #  ",

                 "  #  ",

                 "  #  ",

                 "#####"],

           "J": ["#####",

                 "  #  ",

                 "  #  ",

                 "# #  ",

                 "###  "],

           "K": ["#   #",

                 "#  # ",

                 "###  ",

                 "#  # ",

                 "#   #"],

           "L": ["#    ",

                 "#    ",

                 "#    ",

                 "#    ",

                 "#####"],

           "M": ["## ##",

                 "# # #",

                 "# # #",

                 "# # #",

                 "#   #"],
           "N": ["#   #",

                 "##  #",

                 "# # #",

                 "#  ##",

                 "#   #"],
           "O": ["#####",

                 "#   #",

                 "#   #",

                 "#   #",

                 "#####"],
           "P": ["#####",

                 "#   #",

                 "#####",

                 "#    ",

                 "#    "],
           "Q": ["#####",

                 "#   #",

                 "# # #",

                 "#####",

                 "    #"],
           "R": ["#####",

                 "#   #",

                 "#####",

                 "# #  ",

                 "#  # "],
           "S": ["#####",

                 "#    ",

                 "#####",

                 "    #",

                 "#####"],
           "T": ["#####",

                 "  #  ",

                 "  #  ",

                 "  #  ",

                 "  #  "],
           "U": ["#   #",

                 "#   #",

                 "#   #",

                 "#   #",

                 "#####"],
           "V": ["## ##",

                 "# # #",

                 "# # #",

                 "# # #",

                 "#   #"],
           "W": ["#   #",

                 "#   #",

                 "# # #",

                 "# # #",

                 "## ##"],
           "X": ["#   #",

                 " # # ",

                 "  #  ",

                 " # # ",

                 "#   #"],
           "Y": ["#   #",

                 " # # ",

                 "  #  ",

                 "  #  ",

                 "  #  "],
           "Z": ["#####",

                 "   # ",

                 "  #  ",

                 " #   ",

                 "#####"],
           }


def print_banner(word, direction):
    # make all letters upper case
    word = word.upper()
    # make sure the direction is lower case
    direction = direction.lower()

    if direction == "v":
        # the loop runs for the same amount of iterations as there are
        # letters in the word
        for i in range(len(word)):
            # this loop runs 5 times because each letter is 5 characters
            # tall
            for j in range(5):
                # this accesses the letter i of the word entered and then
                # prints each row of the banner of the letter
                print(letters[word[i]][j])
            # adds a space in between the letters to make it look nicer
            print(" ")

    else:
        # this loop runs 5 times since there are 5 rows of characters
        # in the banner for each letter
        for i in range(5):
            # runs for the same amount of iterations as there are
            # letters in the word
            for j in range(len(word)):
                # prints row number j of each letter with a space between
                # the row of each letter
                print(letters[word[j]][i], end=" ")
            # resets the print spaces so the next row will print on a new line
            print()


print_banner("SigmaChi", "h")
