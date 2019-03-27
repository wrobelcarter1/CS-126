# Lab1 Mad Libs
# Carter Wrobel, Greg Geary, Zeyu Zhang
# cjw446, gsg62, zz74
# 9/18/17
# Section 1

# Ask user to enter different verbs, adjectives, adverbs and nouns using
# the input command
name_1 = input("Enter a male name: ")
adj_1 = input("Enter an adjective: ")
verb_1 = input("Enter a verb: ")
name_2 = input("Enter another name: ")
pverb = input("Enter a past tense verb: ")
adj_2 = input("Enter an adjective: ")
verb_2 = input("Enter a verb: ")
adverb = input("Enter an adverb: ")
noun_1 = input("Enter a noun(thing): ")
noun_2 = input("Enter a place: ")
verb_3 = input("Enter a past tense verb: ")
adj_3 = input("Enter an adjective: ")

# We will use the print command to print out the story and plug in all of
# our variables.
print("My First Mad Lib Story")
print("======================")
print("There was a kid named " + name_1 + ".")
print("He was a " + adj_1 + " kind of kid.")
print("One day, " + name_1 + " was " + verb_1 + " up to " + name_2 + ".")
print(name_2 + " was " + pverb + " to see " + name_1 + ".")
print(name_2 + " thought " + name_1 + " was a " + adj_2 + " " + noun_1 + ".")
print(name_1 + " was shocked by that.")
print(name_2 + " " + verb_2 + " away.")
print(name_1 + " " + adverb + " " + verb_3 + " to " + noun_2 + ".")
print(name_1 + " now thought that " + name_2 + " was " + adj_3 + ".")
print("That is the story of " + name_1 + " and " + name_2 + ".")
