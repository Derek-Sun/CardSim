import random

class Card:
    def __init__(self, suit=0, rank=1):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs','Diamonds','Hearts','Spades']
    rank_names = [None, 'Ace', '2', '3','4','5','6','7','8','9','10','Jack','Queen','King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __cmp__(self, other):
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1

        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1

        return 0

    def numrank(self):
        return self.rank


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        s = [str(card) for card in self.cards]
        return '\n'.join(s)

    def draw_card(self):
        return self.cards.pop()

    def add_card(self,card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

class Hand(Deck):
    def __init__(self, owner=''):
        self.cards =[]
        self.owner = owner

    # Add up ranks of cards in hand, will figure out calculating ace later
    def eval_hand(self):
        sum = 0
        for card in self.cards:
            if card.rank > 10:
                sum += 10
            else:
                sum += card.rank
        return sum

def deal_card(d:Deck, h:Hand):
    h.add_card(d.draw_card())

d = Deck()
h = Hand()
d.shuffle()
deal_card(d,h)
print(h)
print(h.eval_hand())
deal_card(d,h)
print(h)
print(h.eval_hand())