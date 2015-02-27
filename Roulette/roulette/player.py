# -*- coding: utf-8 -*-

class Player():
    """Player superclass
    """
    def __init__(self, table):
        self.table = table

    def place_bets(self):
        """Create new bets at the table, uses Table.place_bet()."""
        pass

    def win(self, bet):
        """Notification of a win from Table. The bet can tell how much."""
        pass

    def lose(self, bet):
        """Notification of a loss from Table. The bet can tell how much."""
        pass

class Passenger57(Player):
    """A player that always places a bet on black."""
    pass