# Alex Bai
# Game of War


import random

VALUES = {
            'A': 14,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'T': 10,
            'J': 11,
            'Q': 12,
            'K': 13
        }
SUITS = ['s', 'c', 'h', 'd']

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return '%s%s' % (self.value, self.suit)

class War:
    def __init__(self):
        self.players = {}
        self.table = []
        self.loser = []

    def reset(self):
        # reset the table for a new game

        deck = [Card(value, suit) for value in list(VALUES.keys())
                                  for suit in SUITS]
        random.shuffle(deck)
        self.players['One'] = deck[:26]
        self.players['Two'] = deck[26:]
        self.table = []
        self.loser = []

    def checkEnoughCards(self, num_cards):
        # checks if players have less than num_cards required to be drawn

        for player, pDeck in self.players.items():
            if len(pDeck) < num_cards:
                self.loser.append(player)

    def battle(self):
        # encompasses an entire turn of play, including any wars
        # sets the loser if they ran out of cards
        
        # do both players have enough cards?
        self.checkEnoughCards(1)
        if self.loser:
            return

        # pop both cards
        p1_card = self.players['One'].pop(0)
        p2_card = self.players['Two'].pop(0)
        self.table.extend([p1_card, p2_card])
        print "P1 plays %s" % p1_card
        print "P2 plays %s" % p2_card

        # compare cards
        p1_card_value = VALUES[p1_card.value]
        p2_card_value = VALUES[p2_card.value]
        if p1_card.value == p2_card.value:
            print "WAR!"
            resolved = False
            while not resolved:
                self.checkEnoughCards(4)
                if self.loser:
                    return
                else:
                    # each draw 3 facedown, doesn't matter what they are
                    self.table.extend(self.players['One'][:3])
                    self.players['One'] = self.players['One'][3:]
                    self.table.extend(self.players['Two'][:3])
                    self.players['Two'] = self.players['Two'][3:]

                    # battle again
                    p1_card = self.players['One'].pop(0)
                    p2_card = self.players['Two'].pop(0)
                    print "P1 plays %s" % p1_card
                    print "P2 plays %s" % p2_card
                    self.table.extend([p1_card, p2_card])
                    p1_card_value = VALUES[p1_card.value]
                    p2_card_value = VALUES[p2_card.value]

                    if p1_card_value > p2_card_value:
                        self.players['One'].extend(self.table)
                        resolved = True
                        print "P1 wins the war!"
                    else:
                        self.players['Two'].extend(self.table)
                        resolved = True
                        print "P2 wins the war!"
        elif p1_card_value > p2_card_value:
            self.players['One'].extend(self.table)
            print "P1 wins the battle."
        else:
            self.players['Two'].extend(self.table)
            print "P2 wins the battle."

        self.table = []
        print '\r\n'
        print 'P1 headcount: %d    P2 headcount: %d' % \
            (len(self.players['One']), len(self.players['Two']))

    def run(self):
        self.reset()

        while not self.loser:
            self.battle()

        if len(self.loser) >= 2:
            # Extremely rare case that enough draws in a row occurred that
            # both players ran out of cards
            print "It's a draw!"
        elif self.loser == 'One':
            print "Player Two wins!"
        else:
            print "Player One wins!"




def main():
    game = War()
    game.run()

if __name__ == '__main__':
    main()


























