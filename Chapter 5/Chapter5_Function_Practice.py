                                                        # Carter Wrobel
                                                        # 9/26/17
                                                        # CS #186
                                                        # Section 1
'''
    This program will find out if the first or last letters are
    the same.
'''

# First letter function
def first_letter(word1, word2):
    w1 = str(word1)[0]
    w2 = str(word2)[0]

    if w1.lower() == w2.lower():
        return "True"
    return "False"

word1 = input("Enter a word: ")
word2 = input("Enter a word: ")

print(first_letter(word1, word2))


# Last letter function
def last_letter(word1, word2):
    w1 = str(word1)[-1]
    w2 = str(word2)[-1]

    if w1.lower() == w2.lower():
        return "True"
    return "False"

word1 = input("Enter a word: ")
word2 = input("Enter a word: ")

print(first_letter(word1, word2))


