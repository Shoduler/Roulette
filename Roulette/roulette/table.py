# -*- coding: utf-8 -*-

from roulette.exceptions import InvalidBet

class Table():
    """Contains all the bets made by players.

    The table has a limit that must be enforced for each player.
    """
    def __init__(self, limit = 1000):
        self.limit = limit
        self.bets = []

    def is_valid(self, bet):
        """Check if a bet would be legal."""
        pass

    def place_bet(self, bet):
        """Attempt to place a bet, if not legal an exception (InvalidBet) will
        be thrown.
        """
        pass

    def __iter__(self):
        """Return an iterator over all bets."""
        pass

    def __str__(self):
        """Easy-to-read representation"""
        pass

    def __repr__(self):
        return '<Table (0x{:08X})>'.format(id(self))

class Bet():
    """Represent the amount that the player has wagered on a specific outcome.
    """
    def __init__(self, amount, outcome):
        self.amount = amount
        self.outcome = outcome

    def win_amount(self):
        """Compute the amount won."""
        pass

    def lose_amount(self):
        """Amount lost."""
        pass

    def __str__(self):
        """Easy-to-read representation"""
        pass

    def __repr__(self):
        return '<Bet: {} on {}>'.format(self.amount, self.outcome)