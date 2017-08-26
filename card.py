import random

SUITS = ["Diamonds", "Hearts", "Spade", "Clubs"]
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.rank + " of " + self.suit)

    def getValue(self):
        if self.rank == 'J' or self.rank == 'Q' or self.rank == 'K':
            return 10
        elif self.rank == 'A':
            return 11
        else:
            return int(self.rank)


class Deck:
    '''Creates a shuffled deck of cards'''
    def __init__(self):
        self.shoe = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.shoe.append(card)
        random.shuffle(self.shoe)

    def deal_Card(self):
        return self.shoe.pop()

    def deck_size(self):
        return len(self.shoe)

class Hand(Deck):
    def __init__(self):
        self.hand = []

    def handValue(self):
        self.value = 0
        ace_count = 0
        for card in self.hand:
            if card.rank == 'A':
                ace_count += 1
            self.value += card.getValue()
        while ace_count > 0:
            if self.value > 21:
                self.value -= 10
                ace_count -= 1
            else:
                return self.value
        return self.value

    def hit(self, card):
        self.hand.append(card)

    '''Prints out the hand value'''
    def getVal(self):
        print(self.handValue())

    '''Creates a list of cards in the hand and returns the list'''
    def getHand(self):
        card_hand = []
        for card in self.hand:
            card_hand.append(card.rank + " of " + card.suit)
        return card_hand
    
def deal_card(d:Deck, h:Hand):
    h.hit(d.deal_Card())

