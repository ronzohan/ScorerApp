from lettuce import step, world
from scorer_app.scorer_app import TEAMS, APP
from webtest import TestApp
from nose.tools import assert_equal, assert_in
from scorer_app.compute_total_score import ComputeTotalScore


@step(u'Given all the teams are set')
def given_all_the_teams_are_set(step):
    world.TEAMS = TEAMS
    world.browser = TestApp(APP)
    world.response = world.browser.get('http://localhost:5000/')


@step(u'Then I see scores')
def then_i_see_scores(step):
    world.player = 'Jackson'
    world.point = 2
    world.team = 'Chelsea'
    form = world.response.forms['tally-form']
    form['player_name'] = world.player
    form['point_score'] = world.point
    form['team'] = world.team
    world.form_response = form.submit()

    compute = ComputeTotalScore(TEAMS)
    total = compute.compute_total()
    player = world.TEAMS[world.team]['players'][world.player]

    for row in step.hashes:
        team1_score = row['team1_score']
        team2_score = row['team2_score']

    assert_equal(team1_score, str(total[0]))
    assert_equal(team2_score, str(total[1]))