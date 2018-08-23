import random
from time import sleep

#Used to create the cards with the Card class
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 
          'Queen':10, 'King':10, 'Ace':11}


class Card:
    """
    Class used to create the cards of the deck
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]
    
    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)

class Deck:
    """
    Class used to create the deck of cards
    """    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_str = ''
        for card in self.deck:
            deck_str += card.__str__() + "\n"
        return 'The order of cards in the deck is as follows:\n' + deck_str

    def shuffle(self):
    	#This method occurs in place, not requiring a return
        random.shuffle(self.deck)

    def deal(self):
        next_card = self.deck.pop()
        return(next_card)

class Hand:
    """
    Class used to hold the cards that the player and dealer have in their hands
    """
    def __init__(self, player):
        self.player = player
        self.hand_cards = [] #Start with empty list
        self.value = 0
        self.aces = 0

    def __str__(self):
        hand_str = ''
        for card in self.hand_cards:
            hand_str += card.__str__() + "\n"
        return "{}'s hand is:\n".format(self.player) + hand_str + "Which is valued at {}\n".format(self.value)

    def add_card(self, card):
        self.hand_cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
        if self.value > 21 and self.aces:
            self.value -=10
            self.aces -= 1

    def clean_hand(self):
        self.hand_cards = []
        self.value = 0
        self.aces = 0

class Chips:
    """
    Class used to track a player's chips
    """
    def __init__(self, total=100):
        self.total = int(total)
        self.bet = 0

    def make_bet(self, bet):
        try:
            bet = int(bet)
            if bet <= 0:
                print("We are sorry, you cannot bet {}".format(bet))
                return True
            elif bet > self.total:
                print("We are sorry, your bet of {} is greater than your total chips of {}".format(bet,self.total))
                return True
            else:
                self.total -= bet
                self.bet += bet
                print("We have accepted your bet of {}, your current total is {}".format(bet,self.total))
                return False
        except:
            print("We are sorry, you cannot bet {}".format(bet))
            return True

    def win_bet(self):
        self.total += self.bet*1.5
        self.bet = 0

    def return_bet(self):
        self.total += self.bet
        self.bet = 0