# Jackson Braudaway, Scott Ames and Carter Wrobel
# jeb523 / saa495 / cjw446
# CS 126L Section 01
# Lab 12: Blackjack
# December 11, 2017

# imports from lab 10 file
from lab10_Answer_Key_MV import Card
from lab10_Answer_Key_MV import ChipBank
import random


class BlackjackHand:
    # Creates a hand for blackjack
    def __init__(self):
        # Initializes start values
        self.newhand = []

    def add_card(self, new_card):
        # adds a card to an empty string
        self.newhand.append(new_card)

    def __str__(self):
        # Prints out the hand
        card_string = ""
        for card in self.newhand:
            card_string += (str(card) + ", ")
        card_string = card_string.strip(", ")
        # Strips the comma at the end of the hand
        return card_string

    def get_value(self):
        # Adding up the values of the cards to give total
        # in blackjack
        hand_value = 0
        for cards in self.newhand:
            points = cards.get_value()
            # Checks to see if you have an Ace, then makes
            # the best decision based on your score at the time
            if points == 11:
                if hand_value <= 10:
                    hand_value += points
                else:
                    hand_value += 1
            else:
                hand_value += points
        return hand_value


class Blackjack:
    # Runs the game of Blackjack
    def __init__(self, starting_dollars):
        # Initializing a player hand and a dealer hand
        self.player_hand = BlackjackHand()
        self.dealer_hand = BlackjackHand()
        self.wager = 0
        self.list_of_cards = []
        self.bank = ChipBank(starting_dollars)
        self.new_card = ""
        # Creates the deck of cards
        for i in range(52):
            deck = Card(i)
            self.list_of_cards.append(deck)
            # print(str(deck.get_value()))
        # Shuffles the deck
        random.shuffle(self.list_of_cards)

    def draw(self):
        # Draws cards
        if self.list_of_cards is False:
            # If the list is empty it creates the deck
            for i in range(52):
                deck = Card(i)
                self.list_of_cards.append(deck)
                # print(str(deck.get_value()))
            random.shuffle(self.list_of_cards)
        else:
            pass
        self.drawn_card = self.list_of_cards[0]
        self.drawn_card.face_up()
        self.list_of_cards.remove(self.drawn_card)
        # Removes the card after drawing
        return self.drawn_card

    def start_hand(self, wager):
        # Starts the Blackjack hand
        self.active = True
        self.wager = wager
        self.bank.withdraw(int(self.wager))
        # First, adds the dealers first card face-down
        self.new_card = self.list_of_cards[0]
        self.dealer_card_one = self.new_card
        # Sets the dealer's card to a variable
        self.list_of_cards.remove(self.list_of_cards[0])
        self.dealer_hand.add_card(self.new_card)
        # Second, adds the player's first card face-up
        self.new_card = self.list_of_cards[0]
        self.list_of_cards.remove(self.list_of_cards[0])
        self.new_card.face_up()
        self.player_hand.add_card(self.new_card)
        # Third, Dealer card face-up
        self.new_card = self.list_of_cards[0]
        self.list_of_cards.remove(self.list_of_cards[0])
        self.new_card.face_up()
        self.dealer_hand.add_card(self.new_card)
        # Finally, the 4th card for the starting hand of the player, face-up
        new_card = self.list_of_cards[0]
        self.list_of_cards.remove(self.list_of_cards[0])
        new_card.face_up()
        self.player_hand.add_card(new_card)
        print("Your starting hand: " + str(self.player_hand))
        print("Dealer's starting hand: " + str(self.dealer_hand))

    def hit(self):
        # Gives the player a card if they hit and have less than 21
        player_value = self.player_hand.get_value()
        self.player_hand.get_value()
        if player_value < 21:
            new_card = self.list_of_cards[0]
            self.list_of_cards.remove(new_card)
            new_card.face_up()
            self.player_hand.add_card(new_card)
            print("You drew a " + str(new_card))
            print("Your hand is now " + str(self.player_hand))

            player_value = self.player_hand.get_value()
            if player_value > 21:
                print("Your hand: " + str(self.player_hand))
                print("BUSTED! You lose.")
                self.end_hand("lose")
            elif player_value == 21:
                print("You have 21! You must stand.")
                self.stand()
                self.end_hand("win")

        # If they have 21, prompts the player to stay
        elif player_value == 21:
            print("You have 21! You must stand.")
            self.stand()
            self.end_hand("win")
        # If over 21, then the player loses
        else:
            print("Your hand: " + str(self.player_hand))
            print("BUSTED! You lose.")
            self.end_hand("lose")

    def stand(self):
        # Moves to the dealers hand to see who wins
        self.dealer_card_one.face_up()
        # makes the dealer's first card face up
        dealer_value = self.dealer_hand.get_value()
        player_value = self.player_hand.get_value()
        while dealer_value <= 16:
            self.new_card = self.list_of_cards[0]
            self.list_of_cards.remove(self.new_card)
            self.new_card.face_up()
            self.dealer_hand.add_card(self.new_card)
            dealer_value = self.dealer_hand.get_value()
            print("Dealer draws a " + str(self.new_card))
            print("Dealer's hand: " + str(self.dealer_hand))
        if dealer_value > 21:
            print("The dealer busted! You win!")
            self.end_hand("win")
        elif dealer_value > player_value:
            print("Your value of cards is: " + str(player_value))
            print("Dealer's value of cards are: " + str(dealer_value))
            print("The dealer won. Try again!")
            self.end_hand("lose")

        elif player_value > dealer_value:
            print("Your hand: " + str(self.player_hand))
            print("Your value of cards is: " + str(player_value))
            print("The dealers value of cards is: " + str(dealer_value))
            print("Your hand is higher than the dealer's. You won!")
            self.end_hand("win")
        else:
            print("It's a tie. You push.")
            self.end_hand("push")

    def end_hand(self, outcome):
        self.outcome = outcome
        if self.outcome == "win":
            self.bank.deposit(self.wager * 2)
            self.player_hand = BlackjackHand()
            self.dealer_hand = BlackjackHand()
            self.active = False
        elif self.outcome == "push":
            self.bank.deposit(self.wager)
            self.player_hand = BlackjackHand()
            self.dealer_hand = BlackjackHand()
            self.active = False
        elif self.outcome == "lose":
            self.player_hand = BlackjackHand()
            self.dealer_hand = BlackjackHand()
            self.active = False

    def game_active(self):
        # Shows whether a game is in progress or not
        if self.active is True:
            return True
        else:
            return False


if __name__ == "__main__":
    # Test code
    a = int(input("Enter how much you want to bet: "))
    blackjack = Blackjack(a)
    while blackjack.bank.get_balance() > 0:
        print("Your remaining chips: " + str(blackjack.bank))
        wager = int(input("How much would you like to wager?: "))
        blackjack.start_hand(wager)
        while blackjack.game_active():
            choice = input("STAND or HIT: ").upper()
            if choice == "STAND":
                blackjack.stand()
            elif choice == "HIT":
                blackjack.hit()
        print()
    print("Out of money! The casino wins!")
