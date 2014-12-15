from lettuce import step, world
from scorer_app.scorer_app import TEAMS, APP
from webtest import TestApp
from nose.tools import assert_equal


@step(u'Given all the teams are set')
def given_all_the_teams_are_set(step):
    world.TEAMS = TEAMS
    world.browser = TestApp(APP)
    world.response = world.browser.get('http://localhost:5000/')


@step(u'Then I see scores')
def then_i_see_scores(step):
    assert False, 'This step must be implemented'