                                                        # Carter Wrobel
                                                        # 10/24/17
                                                        # CS #186
                                                        # Section 1
'''
    This program will ask the user to input a word and then
    calculate the words scrabble word score.
'''
# Scrabble word dictionary with scores for letters
input_file = open("scrabble_words.txt", 'r')
def word_score(word):
    scrabble_score = { "a" : 1,
                       "b" : 3,
                       "c" : 3,
                       "d" : 2,
                       "e" : 1,
                       "f" : 4,
                       "g" : 2,
                       "h" : 4,
                       "i" : 1,
                       "j" : 8,
                       "k" : 5,
                       "l" : 1,
                       "m" : 3,
                       "n" : 1,
                       "o" : 1,
                       "p" : 3,
                       "q" : 10,
                       "r" : 1,
                       "s" : 1,
                       "t" : 1,
                       "u" : 1,
                       "v" : 4,
                       "w" : 4,
                       "x" : 8,
                       "y" : 4,
                       "z" : 10,
                       }
                       
    
    score = []
    for i in range(len(word)):
        word = word.lower()
        a = scrabble_score[word[i]]
        score.append(a)
        # print(score)
        total = sum(score)
    print("The Scrabble score for " + word + " is: " + str(total))
input_file.close()
       
'''
word = input("Enter a word: ")
word_score(word)
'''
