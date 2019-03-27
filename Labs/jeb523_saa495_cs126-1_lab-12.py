# Jackson Braudaway and Scott Ames
# jeb523 / saa495
# CS 126L Section 01
# Lab 12: Blackjack
# November 27, 2017

from lab10_Answer_Key_MV import Card
import random


class BlackjackHand:

    def __init__(self):
        self.newhand = []

    def add_card(self, new_card):
        self.newhand.append(new_card)

    def __str__(self):
        card_string = ""
        for cards in self.newhand:
            card_string += cards.get_rank() + " of "
            card_string += cards.get_suit()
            card_string += ", "
        return card_string

    def get_value(self):
        hand_value = 0
        for cards in self.newhand:
            hand_value += cards.get_value()
        if hand_value > 21:
            for cards in self.newhand:
                print(cards.get_value())
                if cards.get_value() == "11":
                    hand_value -= 10
                print("Here")
                return hand_value
        else:
            print("hi")
            return hand_value




w = BlackjackHand()
w.add_card(Card(38))
w.add_card(Card(0))
w.add_card(Card(2))
print(w.get_value())
print(w)

