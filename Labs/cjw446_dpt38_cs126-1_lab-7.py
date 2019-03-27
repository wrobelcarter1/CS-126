#  Lab 7 Game Book
#  Dakota Templeton, Carter Wrobel
#  dpt38, cjw446
#  CS126L - Section 1
#  10/30/17

import random
questions = [
                {"question": "What year was NAU founded?",
                 "answers": [
                              "1901",
                              "1885",
                              "1899",
                              "1875"],
                 "correct": "3"},
                {"question": "What city is NAU located in?",
                 "answers": [
                             "Flagstaff",
                             "Page",
                             "Prescott",
                             "Phoenix"],
                 "correct": "1"},
                {"question": "Who is the president of NAU?",
                 "answers": [
                              "Joe Johnson",
                              "Tom Brady",
                              "Rita Cheng"],
                 "correct": "3"},
                {"question": "What is NAU's mascott's name?",
                 "answers": [
                                "Sparky",
                                "Louie",
                                "Baxter",
                                "Big Red",
                                "Wilber"],
                 "correct": "2"},
                {"question": "What are NAU's colors?",
                 "answers": [
                                "Blue and Gold",
                                "Green and Gold",
                                "Purple and Pink"],
                 "correct": "1"},
                {"question": "What is NAU's most popular major?",
                 "answers": [
                                "Nursing",
                                "Mechanical Engineering",
                                "Criminal Justice",
                                "Forestry"],
                 "correct": "3"},
                {"question": "How many students attend NAU?",
                 "answers": [
                                "14,000",
                                "29,000",
                                "32,000",
                                "23,000"],
                 "correct": "2"},
                {"question": "True or False, The majority of NAU"
                 " students smoke weed.",
                 "answers": [
                                "True",
                                "False"],
                 "correct": "2"},
                {"question": "What is the name of the mountain in flagstaff?",
                 "answers": [
                                "Mount Everest",
                                "Camelback Mountain",
                                "North Mountain",
                                "South Mountain",
                                "Humphrey's Peak"],
                 "correct": "5"},
                {"question": "What historical highway runs through Flagstaff?",
                 "answers": [
                                "Route 10",
                                "Highway 1",
                                "Route 66",
                                "Route 4"],
                 "correct": "3"}]

print("Welcome to our NAU Trivia Game!")
print("Good luck!")


def play_game(answer):
    random.shuffle(questions)
    count = 0
    for question in questions:
        print(question["question"])
        for i, choice in enumerate(question["answers"]):
            print(str(i + 1) + ". " + choice)
        answer = input("Choose an answer 1 - " +
                       str(len(question["answers"])) + ":")
        while int(answer) not in range(len(question["answers"])+1):
            answer = input("Choose an answer 1 - " +
                           str(len(question["answers"])) + ":")
        if answer == question["correct"]:
            print("Correct! Nice!")
            count = count + 1
            print("Your score is: " + str(count) + " out of 10")
            print("              ")
        else:
            print("NOPE, Wrong, Fake answer")
            print("Your score is: " + str(count) + " out of 10")
            print("                        ")

    return main()


def view_credits(answer):
    print("This game is brought to you in part by "
          "Carter Wrobel and Dakota Templeton. "
          "2017, CS126L.")
    print("                   ")
    return main()


def quit_game(answer):
    print("Hope you enjoyed the game!")


def main():
    answer = input("Pick an option(Play Game, View Credits, Exit): ")
    answer = answer.lower()
    if answer == "play game":
        play_game(answer)
    elif answer == "view credits":
        view_credits(answer)
    else:
        quit_game(answer)


if __name__ == "__main__":
    main()
