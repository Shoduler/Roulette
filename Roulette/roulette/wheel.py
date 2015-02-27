# -*- coding: utf-8 -*-

from roulette.outcome import OutcomeFactory
import random

class Wheel():
    """Contains the 38 bins of the roulette Wheel. The bins are numbered 0 to 37
    where 0-36 represent their actual numbers. 00 is mapped to 37.
    
    A random number generator (rng) can be provided for testing purposes.

    The wheel should also 
    """
    def __init__(self, rng = None):
        self.bins = tuple(Bin() for i in range(38))
        self.rng = rng if rng is not None else random.Random()
        self.bin_builder()

    def next(self):
        """Generate the next winning bin and return it."""
        pass

    def get(self, bin):
        """Returns a bin"""
        pass

    def bin_builder(self):
        """Build all 38 bins with their respective outcomes.
        
        There's quite a few different bets in roulette that will add outcomes
        to the different bins.

        The following bets exist on the American roulette table:
        Single, Split, Street, Corner, Double street, Basket, Top line, 1-18,
        19-36, Red, Black, Even, Odd, Dozen (1-12, 13-24, 25-36), 
        Column (3c + 1, 3c + 2 and 3c + 3, where 0 <= c < 12).
        """
        pass

class Bin():
    """A collection of Outcomes that all will be winning or losing at the same
    time. There should be 38 different Bins (1-36, 0 and 00).

    Since it will be mostly read and very rarely changed or created a frozenset
    is used for implementing the storage of outcomes.
    """
    def __init__(self, *outcomes):
        self.outcomes = outcomes

    def add(self, outcome):
        """Will need to recreate self.outcomes with the added outcome."""
        pass

    def __str__(self):
        """Easy-to-read representation"""
        pass

    def __repr__(self):
        return '<{}>'.format(', '.join(self.outcomes))

class NonRandom():
    """Custom random number generator. Only for testing!
   
    By setting the attribute seed the next choice can be controlled.
    """
    def __init__(self):
        self.seed = None

    def choice(self, sequence):
        return sequence[self.seed]