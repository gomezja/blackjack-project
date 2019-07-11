import random

#====================Classes====================#
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)

class Deck:
    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        curr_deck = "Blackjack Deck\n=============="

        for card in self.deck:
            curr_deck += "\n" + card.__str__()

        return curr_deck

    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)

        card_value = values[card.rank]
        self.value += card_value

        if card_value == 11:
            self.aces += 1
    
    def adjust_for_ace(self):
        if self.aces > 0 and self.value > 21:
            self.value -= 10

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

#====================Functions====================#
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Current amount: {}\nEnter your bet amount: ".format(chips.total)))
        except:
            print("Not a number!")
        else:
            if chips.bet > chips.total:
                print("invalid funds")
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())

def hit_or_stand(deck, hand):
    global playing
    choice = ""

    while not choice.upper() == 'H' and not choice.upper() == 'S':
        print("\n====================")
        choice = input("Hit or stay (H/S)? ")
        print("\n====================")

    if choice.upper() == 'H':
        hand.add_card(deck.deal())
    else:
        playing = False

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

while True:
    deck = Deck()
    deck.shuffle()

    player_chips = Chips()
    take_bet(player_chips)

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    playing = True

    while playing:
        pass