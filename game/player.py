class Player(object):
    """
    A base Python class to represent game players.
    """
    def __init__(self):
        super(Player, self).__init__()
        self.hand = []  # the five cards that the player has.
        self.penalty = []  # the penalty pile that belongs to the player.

    def deal(self, pile):
        """
        Every Player subclass must implement this method. This method
        specifies how the cards will be dealt to the pile.
        
        The naive implementation here iterates over the cards and returns the
        first card in the deck that matches either the suite or value criteria.

        More complex criteria can be added, such as implementing a strategy
        for keeping chameleon cards while sacrificing a small card.
        """
        for c in self.hand:
            if c.suite == pile.current_suite or c.value == pile.current_value:
                pile.receive_card(c)
                self.hand.remove(c)
                break

            else:
                self.penalty.append(c)
                self.hand.remove(c)
                break

    def take_card(self, deck):
        """
        Takes a card from the deck.
        """

        card = deck.deal()
        self.hand.append(card)


