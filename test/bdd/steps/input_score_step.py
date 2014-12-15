from lettuce import step, world
from scorer_app.scorer_app import TEAMS, APP
from webtest import TestApp
from nose.tools import assert_equal


@step(u'Given that a player "([^"]*)" scored from team "([^"]*)"')
def given_that_a_player_group1_scored_from_team_group2(step, player, team):
    world.browser = TestApp(APP)
    world.response = world.browser.get('http://localhost:5000/')
    world.TEAMS = TEAMS


@step(u'And that the player scored 2 points')
def and_that_the_player_scored_2_points(step):
    for row in step.hashes:
        world.player = row['player_name']
        world.point = row['point_score']
        world.team = row['team']


@step(u'When I hit submit')
def when_i_hit_submit(step):
    form = world.response.forms['tally-form']
    form['player_name'] = world.player
    form['point_score'] = world.point
    form['team'] = world.team
    world.form_response = form.submit()


@step(u'Then the player "([^"]*)" score was been tallied.')
def then_the_player_group1_score_was_been_tallied(step, group1):
    player = TEAMS['Chelsea']['players'][str(group1)]
    assert_equal(world.TEAMS['Chelsea']['scores'][player], 2)