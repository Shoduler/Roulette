# -*- coding: utf-8 -*-

import unittest

if __name__ == "__main__":
    all_tests = unittest.TestLoader().discover('tests') 
    unittest.TextTestRunner().run(all_tests)