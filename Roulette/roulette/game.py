# -*- coding: utf-8 -*-

class Game():
    """Runs the roulette simulation.

    Each round consists of the following phases:
    1. Place bets
    2. Spin wheel
    3. Resolve all bets
    """
    def __init__(self, wheel, table):
        self.wheel = wheel
        self.table = table
        self.players = None

    def run(self, players):
        """Start the simulation of an entire game for the provided players."""
        self.players = players