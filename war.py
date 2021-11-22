# Alex Bai
# Game of War






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
        return 'Player %s: \r\n %s' % (self.name, str(self.pDeck))



