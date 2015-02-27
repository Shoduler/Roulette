# -*- coding: utf-8 -*-

class Outcome():
    """Represents the different outcomes

    Don't create Outcome object directly, use OutcomeFactory!

    Each outcome has a name and odds. Since all odds in roulette is on the form
    N:1 we only store N in odds. (This is not true in all casino games.)

    """
    def __init__(self, name, odds):
        self.name = name
        self.odds = odds

    def win_amount(self, amount):
        """Returns amount * self.odds"""
        pass

    def __eq__(self, other):
        """Compare the name attributes of self and other."""
        pass

    def __ne__(self, other):
        """Compare the name attributes of self and other."""
        pass

    def __str__(self):
        """Easy-to-read representation"""
        pass
        
    def __repr__(self):
        return '<{} ({}:1)>'.format(self.name, self.odds)

class OutcomeFactory():
    """Factory class for Outcome

    Since we want to be able to compare different outcomes with identity there
    should never be more than one object for each possible outcome. This is 
    accomplished by this factory.
    """
    def __init__(self):
        self.outcomes = {}

    def get(self, name, odds):
        """Return the request Outcome object. If it doesn't exist a new object
        is created, stored and returned. 
        
        Only to be used when setting up the game!
        """
        if not (name, odds) in self.outcomes:
            self.outcomes[(name, odds)] = Outcome(name, odds)

        return self.outcomes[(name, odds)]

    def by_name(self, name):
        """Return the requested Outcome object. Raise exception if it does not
        exist (ValueError)."""
        pass

    def __repr__(self):
        return '<Outcome factory>'