# -*- coding: utf-8 -*-

import unittest
from roulette.wheel import Wheel
import random

class WheelTestCase(unittest.TestCase):
    def test_create_wheel_uses_default_rng(self):
        wheel = Wheel()

        self.assertIsInstance(wheel.rng, random.Random)