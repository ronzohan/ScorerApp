"""
Controller file
"""

from flask import Flask, render_template, request

PLAYERS_TEAM1 = {'Eden Hazard': '1', 'a': '2', 'b': '3', 'c': '4', 'd': '5'}
PLAYERS_TEAM1_SCORE = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0}
TEAM1 = {'players': PLAYERS_TEAM1, 'name': 'Chelsea', 'scores': PLAYERS_TEAM1_SCORE}

PLAYERS_TEAM2 = {'e': '1', 'f': '2', 'g': '3', 'h': '4', 'i': '5'}
PLAYERS_TEAM2_SCORE = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0}
TEAM2 = {'players': PLAYERS_TEAM2, 'name': 'Liverpool', 'scores': PLAYERS_TEAM2_SCORE}

TEAMS = {'Chelsea': TEAM1, 'Liverpool': TEAM2}

APP = Flask(__name__)


@APP.route('/')
def hello_world():
    player_name = request.args.get('player_name')
    point_score = request.args.get('point_score')
    team = request.args.get('team')

    try:
        player = update_points(player_name, point_score, team)
        return render_template('index.html', player_name=player_name, 
                               point_score=TEAMS[team]['scores'][player])
    except:
        return render_template('index.html', player_name=None, 
                               point_score=None)


def update_points(player_name, point_score, team):
    try:
        player = TEAMS[team]['players'][player_name]
        TEAMS[team]['scores'][player] += point_score
    except:
        player = None

    return player


if __name__ == '__main__':
    update_points('Eden Hazard', 2, 'Chelsea')
    #APP.run(debug=True)
