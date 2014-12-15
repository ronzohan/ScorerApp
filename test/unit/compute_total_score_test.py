import unittest
from nose.tools import assert_raises, assert_equal
from scorer_app.compute_total_score import ComputeTotalScore


class TestInputScore(unittest.TestCase):
    def test_if_input_values_are_none(self):
        
