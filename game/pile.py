from collections import namedtuple

class Pile(object):
    """docstring for Pile"""
    def __init__(self):
        super(Pile, self).__init__()
        self.cards = []
        self.current_suite = None
        self.current_value = None

    def receive_card(self, card, new_suite=None):
        """
        Receives a card to add to the pile of cards.
        """
        assert isinstance(card, namedtuple)
        assert len(card) == 2

        if card.value != 'joker':
            self.cards.append(card)
            self.current_suite = card.suite
            self.current_value = card.value

        else:
            assert new_suite != None, print('You must specify a new suite.')
            assert new_suite in ['hearts', 'spades', 'diamonds', 'clubs']

            self.current_suite = new_suite
            self.current_value = None


    def current_suite(self):
        """
        Reports the current suite at the top of the deck.
        """

        return self.cards[-1].suite

    def current_value(self):
        """
        Reports the current value at the top of the deck.
        """
        return self.cards[-1].value