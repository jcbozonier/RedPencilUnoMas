import unittest
from good import *

class given_a_fresh_good_with_no_history(unittest.TestCase):
    def setUp(self):
        self.good = Good()
    def test_when_price_reduced_less_than_5_percent(self):
        self.good.reduce_price(by=.03)
        self.assertFalse(self.good.is_red_pencil_promotion_active(), "It should NOT activate the red pencil promotion")
        self.good = Good()
    def test_when_price_reduced_by_5_percent(self):
        self.good.reduce_price(by=.05)
        self.assertTrue(self.good.is_red_pencil_promotion_active(), "It should activate the red pencil promotion")
        self.good = Good()
    def test_when_price_reduced_by_30_percent(self):
        self.good.reduce_price(by=.30)
        self.assertTrue(self.good.is_red_pencil_promotion_active(), "It should NOT activate the red pencil promotion")
        self.good = Good()
    def test_when_price_reduced_by_31_percent(self):
        self.good.reduce_price(by=.31)
        self.assertFalse(self.good.is_red_pencil_promotion_active(), "It should NOT activate the red pencil promotion")

class given_a_good_in_a_red_pencil_promotion(unittest.TestCase):
    def setUp(self):
        self.good = Good()
        self.good.reduce_price(by=0.3)
    def test_when_price_reduction_exceeds_30_percent(self):
        self.good.reduce_price(by=0.1)
        self.assertFalse(self.good.is_red_pencil_promotion_active(), "It should immediately stop the promotion.")
