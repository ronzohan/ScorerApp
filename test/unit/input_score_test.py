import unittest
from scorer_app.scorer_app import update_points
from nose.tools import assert_raises, assert_equal


class TestInputScore(unittest.TestCase):
    def test_if_input_values_are_none(self):
        player = update_points(None, None, None)
        assert_equal(player, None)

    def test_if_the_scores_are_updated(self):
        player = update_points('Eden Hazard', '2', 'Chelsea')
        assert_equal(player, str(1))

    def test_if_score_input_is_less_than_0_or_more_than_4(self):
        player = update_points('Eden Hazard', '4', 'Chelsea')
        assert_equal(player, None)
