# -*- coding: utf-8 -*-
"""
Roulette
========

This package implements the casino game roulette.

"""

from roulette.game import Game
from roulette.table import Table
from roulette.wheel import Wheel
from roulette.outcome import OutcomeFactory

outcome_factory = OutcomeFactory()