import unittest
from scorer_app.scorer_app import update_points
from nose.tools import assert_raises, assert_equal


class TestInputScore(unittest.TestCase):
    def test_if_input_values_are_none(self):
        player = update_points(None, None, None)
        assert_equal(player, None)