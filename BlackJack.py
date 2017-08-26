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
        print("Hand Value: " + str(self.handValue()))

    '''Creates a list of cards in the hand and returns the list'''
    def getHand(self):
        card_hand = []
        for card in self.hand:
            card_hand.append(card.rank + " of " + card.suit)
        return card_hand
    
def deal_card(d:Deck, h:Hand):
    h.hit(d.deal_Card())

class Player:
    def __init__(self, money = 0):
        self.win = 0
        self.loss = 0
        self.tie = 0
        self.chips = money
        self.hand = Hand()
    
    def clearHand(self):
        self.hand = Hand()
        
def getStatus(player):
    print(player.hand.getHand())
    player.hand.getVal()

def replayGame():
    replay = int(input("1)Play Again  2)End\n"))
    while replay != 1 and replay != 2:
        print("Invalid input.")
        replay = int(input("Please enter 1 to replay and 2 to end.\n"))
    return replay

def tieGame(p: Player):
     print("Even Money")
     p.tie +=1
     print("Wins " + str(p.win) + ", Losses " + str(p.loss) + ", Ties " + str(p.tie))

def winGame(p: Player):
    print("Player wins!")
    p.win += 1
    print("Wins " + str(p.win) + ", Losses " + str(p.loss) + ", Ties " + str(p.tie))

def loseGame(p: Player):
    print("Dealer wins!")
    p.loss += 1
    print("Wins " + str(p.win) + ", Losses " + str(p.loss) + ", Ties " + str(p.tie))

def getPlayerMove(p: Player, d: Deck):
    while 1:
        player_move = int(input("1)Hit  2)Stand\n"))
        while player_move != 1 and player_move != 2:
            print("Invalid input.")
            player_move = int(input("Please enter 1 for Hit and 2 for Stand"))
        if player_move == 1:
            deal_card(d, p.hand)
            getStatus(p)
            if (p.hand.handValue() > 21):
                return 1
        else:
            return 0


    
''' initiates a game with one player'''

def startGame():
    p = Player(1000)
    dealer = Player(1000)
    d = Deck()
    count = 0

    while 1:
        print("Game # " + str(count))
        count += 1
        if (d.deck_size() < 15): #Reshuffle a new deck when shoe is too small
            print("... Reshuffling Deck...")
            d = Deck()
        deal_card(d, dealer.hand)
        deal_card(d, p.hand)
        deal_card(d, dealer.hand)
        deal_card(d, p.hand)
        print("Dealer's Cards")
        print(dealer.hand.getHand()[1])
        print("Player's Cards")
        getStatus(p)
        if int(p.hand.handValue()) == 21 and int(dealer.hand.handValue()) == 21:
            tieGame(p)
            getReplay = replayGame()
            if getReplay == 1:
                p.clearHand()
                dealer.clearHand()
                continue
            else:
                break
        elif int(p.hand.handValue()) == 21 and int(dealer.hand.handValue()) != 21:
            print("Player Blackjack!")
            winGame(p)
            getReplay = replayGame()
            if getReplay == 1:
                p.clearHand()
                dealer.clearHand()
                continue
            else:
                break
        elif int(p.hand.handValue()) != 21 and int(dealer.hand.handValue()) == 21:
            print("Dealer Blackjack!")
            loseGame(p)
            getReplay = replayGame()
            if getReplay == 1:
                p.clearHand()
                dealer.clearHand()
                continue
            else:
                break
        else:
            bust = getPlayerMove(p, d)
            if bust == 1:
               print("Bust! \nDealer wins!")
               getReplay = replayGame()
               if getReplay == 1:
                  p.clearHand()
                  dealer.clearHand()
                  continue
               else:
                  break
            else:
                print("Standing")
            while int(dealer.hand.handValue() < 17):
                deal_card(d, dealer.hand)

            if (int(dealer.hand.handValue() > 21)):
                getStatus(dealer)
                print("Dealer Busted!")
                winGame(p)
                getReplay = replayGame()
                if getReplay == 1:
                    p.clearHand()
                    dealer.clearHand()
                    continue
                else:
                    break
            elif (int(dealer.hand.handValue()) > int(p.hand.handValue())):
                getStatus(dealer)
                loseGame(p)
                getReplay = replayGame()
                if getReplay == 1:
                    p.clearHand()
                    dealer.clearHand()
                    continue
                else:
                    break
            elif (int(dealer.hand.handValue()) < int(p.hand.handValue())):
                getStatus(dealer)
                winGame(p)
                getReplay = replayGame()
                if getReplay == 1:
                    p.clearHand()
                    dealer.clearHand()
                    continue
                else:
                    break
            else:
                getStatus(dealer)
                tieGame(p)
                getReplay = replayGame()
                if getReplay == 1:
                    p.clearHand()
                    dealer.clearHand()
                    continue
                else:
                    break


startGame()