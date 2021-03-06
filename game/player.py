from random import choice

class Player(object):
    """
    A base Python class to represent game players.
    """
    def __init__(self, chameleon):
        super(Player, self).__init__()
        self.hand = []  # the five cards that the player has.
        self.penalty = []  # the penalty pile that belongs to the player.
        self.chameleon = chameleon  # the card value that is the chameleon card

    def deal(self, pile):
        """
        Every Player subclass must implement this method. This method
        specifies how the cards will be dealt to the pile.
        
        The naive implementation here iterates over the cards and returns the
        first card in the deck that matches either the suite or value criteria.

        More complex criteria can be added, such as implementing a strategy
        for keeping chameleon cards while sacrificing a small card.
        """
        if not self.has_cards():
            pass

        else:

            if self.has_matching_suite(pile):
                c = sorted([c for c in self.hand if c.suite == pile.current_suite], key=lambda x:x.value)
                c = c[0]
                print('Dealing {0} of {1}'.format(c.value, c.suite))
                pile.receive_card(c, new_suite=None, is_using_chameleon=False)
                self.hand.remove(c)

            elif self.has_matching_value(pile):
                c = choice([c for c in self.hand if c.value == pile.current_value])
                print('Dealing {0} of {1}'.format(c.value, c.suite))
                pile.receive_card(c, new_suite=None, is_using_chameleon=False)
                self.hand.remove(c)

            elif self.has_chameleon() or self.has_joker():
                c = choice([c for c in self.hand if c.value == self.chameleon or c.value == 14])
                new_suite = choice([c.suite for c in self.hand if c.value != self.chameleon and c.value != 14])
                print('Dealing {0} of {1}'.format(c.value, c.suite))
                pile.receive_card(c, new_suite=new_suite, is_using_chameleon=False)
                self.hand.remove(c)      

            else:
                # Choose a card of minimum value.
                c = sorted([c for c in self.hand], key = lambda x:x.value)
                new_suite = None
                c = c[0]
                print("No cards. Penalty with {0} of {1}.".format(c.value, c.suite))
                self.penalty.append(c)
                self.hand.remove(c)


    def take_card(self, deck):
        """
        Takes a card from the deck.
        """
        if deck.has_cards():
            card = deck.deal()
            self.hand.append(card)

        else:
            print('Deck has no more cards.')

    def penalty_score(self):
        """
        Computes the final penalty score.
        """
        return sum([c.value for c in self.penalty])

    def has_chameleon(self):
        """
        Boolean that returns whether the chameleon card is present in hand.
        """
        return self.chameleon in [c.value for c in self.hand]

    def has_joker(self):
        """
        Boolean that returns whether the joker card is present in hand.
        """
        return 14 in [c.value for c in self.hand]

    def has_matching_suite(self, pile):
        """
        Boolean that returns whether the hand contains a card of matching suite.
        """
        cs = pile.current_suite
        return cs in [c.suite for c in self.hand]

    def has_cards(self):
        """
        Boolean that returns whether the player still has cards or not.
        """
        return bool(self.hand)

    def has_matching_value(self, pile):
        """
        Boolean that returns whether the hand contains a card of matching value.
        """

        cv = pile.current_value
        return cv in [c.value for c in self.hand]

    def most_common_suite(self, value=None):
        """
        Returns the most common suite on hand.
        """