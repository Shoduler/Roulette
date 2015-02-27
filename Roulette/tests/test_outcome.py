# -*- coding: utf-8 -*-

import unittest
from roulette.outcome import Outcome, OutcomeFactory

class OutcomeTestCase(unittest.TestCase):
    def test_outcome_name(self):
        outcome = Outcome('Red', 1)

        self.assertTrue(outcome.name == 'Red')
        self.assertTrue(outcome.odds == 1)