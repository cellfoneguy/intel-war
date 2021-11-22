# Alex Bai
# Game of War


import random

VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
SUITS = ['s', 'c', 'h', 'd']

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return '%s%s' % (self.value, self.suit)

class Player:
    def __init__(self, name, pDeck):
        self.name = name
        self.pDeck = pDeck

    def __repr__(self):
        return 'Player %s: %s' % (self.name, str(self.pDeck))

class War:
    def __init__(self):
        self.players = None

    def reset(self):
        deck = [Card(value, suit) for value in VALUES for suit in SUITS]
        random.shuffle(deck)
        p1 = Player('One', deck[:26])
        p2 = Player('Two', deck[26:])
        self.players = [p1, p2]

    def run(self):
        self.reset()
        print self.players[0]

def main():
    game = War()
    game.run()

if __name__ == '__main__':
    main()
