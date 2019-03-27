# Lab 10 - Casino Night
# cjw446 and gmw94
# Carter Wrobel and Gavin Wagner
# CS126L - Section 1
# 11/26/17
import random


class Card:

    def __init__(self, num):
        # Card Suit
        if 0 <= num <= 12:
            self.card_suit = "Spades"
        elif 12 < num <= 25:
            self.card_suit = "Hearts"
        elif 25 < num <= 38:
            self.card_suit = "Clubs"
        else:
            self.card_suit = "Diamonds"
        # Card Rank
        if num == 0 or num == 13 or num == 26 or num == 39:
            self.card_rank = "Ace"
        elif num == 10 or num == 23 or num == 36 or num == 49:
            self.card_rank = "Jack"
        elif num == 11 or num == 24 or num == 37 or num == 50:
            self.card_rank = "Queen"
        elif num == 12 or num == 25 or num == 38 or num == 51:
            self.card_rank = "King"
        else:
            self.card_rank = str(num)
        # Card Value
        if num == 0 or num == 13 or num == 26 or num == 39:
            self.card_value = 11
        elif num == 10 or num == 23 or num == 36 or num == 49:
            self.card_value = 10
        elif num == 11 or num == 24 or num == 37 or num == 50:
            self.card_value = 10
        elif num == 12 or num == 25 or num == 38 or num == 51:
            self.card_value = 10
        else:
            self.card_value = num

    def face_down(self):
        self.card_face = "<facedown>"
        return self.card_face

    def face_up(self):
        self.card_face = "<faceup>"
        return self.card_face

    def __str__(self):
        return self.card_rank + " of " + self.card_suit

    def get_suit(self):
        return self.card_suit

    def get_rank(self):
        return self.card_rank

    def get_value(self):
        return self.card_value


class ChipBank:
    def __init__(self, value):
        self.balance = value

    def withdraw(self, amount):
        if self.balance < amount:
            return self.balance
        self.balance = self.balance - amount
        return amount

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def get_balance(self):
        return self.balance

    def __str__(self):
        self.black = self.balance // 100
        self.green = (self.balance % 100) // 25
        self.red = ((self.balance % 100) % 25) // 5
        self.blue = (((self.balance % 100) % 25) % 5) // 1
        return str(self.black) + " blacks, " + str(self.green) +
    " greens, " + str(self.red) + " reds, " + str(self.blue) + 
    " blues -- totaling $" + str(self.balance)


if __name__ == "__main__":
    card = Card(37)
    print(card)
    print(card.get_value())
    print(card.get_suit())
    print(card.get_rank())
    card.face_down()
    print(card)

    cs = ChipBank(149)
    print(cs)
    cs.deposit(7)
    print(cs.get_balance())
    print(cs)
    print(cs.withdraw(84))
    print(cs)
    cs.deposit(120)
    print(cs)
    print(cs.withdraw(300))
