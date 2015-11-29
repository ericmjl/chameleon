from itertools import product
from random import shuffle
from collections import namedtuple

Card = namedtuple('Card', ['suite', 'value'])

class Deck(object):
    """
    A Python class to represent a deck of cards.
    """
    def __init__(self):
        super(Deck, self).__init__()
        self.cards = self.populate()

    def populate(self):
        """
        Populates the deck of cards, in order.
        """
        suites = ['spades', 'hearts', 'diamonds', 'clubs']
        values = range(1,14)

        cards = []

        for suite, value in product(suites, values):
            
            cards.append(Card(suite, value))
        
        cards.append(Card('red', 14))
        cards.append(Card('black', 14))

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

    