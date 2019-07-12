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
            self.aces -= 1

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
    # print("\nChips ${}".format(chips.total))
    
    while True:
        try:
            chips.bet = int(input("Total Wager: $"))
        except:
            print("Not a number!\n")
        else:
            if chips.bet <= 0:
                print("Minimum bet is at least $1\n")
            elif chips.bet > chips.total:
                print("Insufficient funds\n")
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing
    choice = ""

    print("\n====================\n")
    while not choice == 'H' and not choice == 'S':
        choice = input("Hit or stay [H/S]? ").upper()

    if choice == 'H':
        hit(deck, hand)
    else:
        playing = False

def player_wins(hand, chips):
    print("\nWINNER!\n+${}".format(chips.bet))
    chips.win_bet()

def dealer_wins(hand, chips):
    print("\nLOSER!\n-${}".format(chips.bet))
    chips.lose_bet()

def push():
    print("PUSH")

def show_some(player, dealer):
    print("\nDealer's Score (???)\n--------------------\n<Hidden Card>\n{}".format(dealer.cards[1]))
    print("\nYour Score ({})\n--------------------".format(player.value), *player.cards, sep="\n")

def show_all(player, dealer):
    print("\nDealer's Score ({})\n--------------------".format(dealer.value), *dealer.cards, sep="\n")
    print("\nYour Score ({})\n--------------------".format(player.value), *player.cards, sep="\n")

def play_again():
    choice = ""
    
    while not choice == 'Y' and not choice == 'N':
        choice = input("Play again [Y/N]? ").upper()

    return choice

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

print("Blackjack!")

player_chips = Chips()
print("\nChips ${}".format(player_chips.total))

while True:
    deck = Deck()
    deck.shuffle()

    take_bet(player_chips)

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    player_hand.adjust_for_ace()

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    dealer_hand.adjust_for_ace()

    show_some(player_hand, dealer_hand)

    playing = True

    while playing:
        hit_or_stand(deck, player_hand)

        if playing and player_hand.value <= 21:
            show_some(player_hand, dealer_hand)
        elif playing and player_hand.value > 21:
            show_all(player_hand, dealer_hand)
            dealer_wins(player_hand, player_chips)
            break
        else:
            break

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)
        
        if dealer_hand.value > 21 or dealer_hand.value < player_hand.value:
            player_wins(player_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, player_chips)
        else:
            push()

    print("\nChips ${}".format(player_chips.total))

    if play_again() == 'Y':
        if player_chips.total > 0:
            playing = True
            print()
            continue
        else:
            print("\nYour Broke!")
            break
    else:
        break