from itertools import product
from random import shuffle

class Deck(object):
    """
    A Python class to represent a deck of cards.
    """
    def __init__(self):
        super(Deck, self).__init__()
        self.cards = self.initialize()

    def initialize(self):
        """
        Initializes the deck of cards, in order.
        """
        suites = ['spades', 'hearts', 'diamonds', 'clubs']
        values = range(1,14)

        cards = []

        for suite, value in product(suites, values):
            cards.append((suite, value))
        
        cards.append(('red', 'joker'))
        cards.append(('black', 'joker'))

        return cards

    def shuffle(self):
        """
        Shuffles the deck of cards.
        """
        shuffle(self.cards)

    def deal(self):
        """
        Deals a card from the top of the deck, and removes it from the deck.
        """
        card = self.cards[0]
        self.cards.remove(card)

        return card

    def has_cards(self):
        """
        Returns boolean True/False if the deck has cards or not.
        """

        return bool(self.cards)

    