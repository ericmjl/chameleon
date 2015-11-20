class Player(object):
    """
    A base Python class to represent game players.
    """
    def __init__(self):
        super(Player, self).__init__()
        self.deck = []
        self.penalty = []