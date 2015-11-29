from collections import namedtuple

class Pile(object):
    """docstring for Pile"""
    def __init__(self, chameleon, initial_card):
        super(Pile, self).__init__()
        self.cards = [initial_card]
        self.current_suite = initial_card.suite
        self.current_value = initial_card.value
        self.chameleon = chameleon

    def receive_card(self, card, new_suite=None, is_using_chameleon=False):
        """
        Receives a card to add to the pile of cards.
        """
        assert isinstance(card, tuple)
        assert len(card) == 2

        if card.value == 14 or card.value == self.chameleon and is_using_chameleon:
            assert new_suite != None, print('You must specify a new suite.')
            assert new_suite in ['hearts', 'spades', 'diamonds', 'clubs']

            self.current_suite = new_suite
            self.current_value = None

        else:
            self.cards.append(card)
            self.current_suite = card.suite
            self.current_value = card.value


    # def current_suite(self):
    #     """
    #     Reports the current suite at the top of the deck.
    #     """

    #     return self.cards[-1].suite

    # def current_value(self):
    #     """
    #     Reports the current value at the top of the deck.
    #     """
    #     return self.cards[-1].value