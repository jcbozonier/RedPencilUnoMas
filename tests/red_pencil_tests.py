import unittest
import datetime
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
        self.some_day = datetime.datetime.now()
        self.some_day_and_a_month = datetime.datetime.now() + datetime.timedelta(31)
        self.good = Good()
        self.good.reduce_price(by=0.2, effective=self.some_day)
    def test_when_price_reduction_exceeds_30_percent(self):
        self.good.reduce_price(by=0.2, effective=self.some_day)
        self.assertFalse(self.good.is_red_pencil_promotion_active(), "It should immediately stop the promotion.")
    def test_when_30_days_have_passed(self):
        self.good.reduce_price(by=0.01, effective=self.some_day_and_a_month)
        self.assertTrue(self.good.is_red_pencil_promotion_active(), "It should immediately start the promotion.")

class given_a_good_stabilizing_after_having_a_non_promotional_price_reduction(unittest.TestCase):
    def setUp(self):
        self.some_day = datetime.datetime.now()
        self.some_day_and_a_month = datetime.datetime.now() + datetime.timedelta(31)
        self.good = Good()
        self.good.reduce_price(by=0.03, effective=self.some_day)
    def test_when_applying_red_pencil_price_reduction(self):
        self.good.reduce_price(by=0.1, effective=self.some_day)
        self.assertFalse(self.good.is_red_pencil_promotion_active(), "It should not enter the promotion because it's still stabilizing.")
