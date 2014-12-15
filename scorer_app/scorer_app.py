"""
Controller file
"""

from flask import Flask, render_template, request
from _ast import IsNot
from compute_total_score import ComputeTotalScore


PLAYERS_TEAM1 = {'Eden Hazard': '1', 'Jackson': '2', 'March': '3', 'Apple': '4', 'Lincoln': '5'}
PLAYERS_TEAM1_SCORE = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0}
TEAM1 = {'players': PLAYERS_TEAM1, 'name': 'Chelsea', 'scores': PLAYERS_TEAM1_SCORE}

PLAYERS_TEAM2 = {'Costa': '1', 'Terry': '2', 'Cahill': '3', 'Drogba': '4', 'Cech': '5'}
PLAYERS_TEAM2_SCORE = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0}
TEAM2 = {'players': PLAYERS_TEAM2, 'name': 'Liverpool', 'scores': PLAYERS_TEAM2_SCORE}

TEAMS = {'Chelsea': TEAM1, 'Liverpool': TEAM2}

APP = Flask(__name__)


@APP.route('/')
def hello_world():
    player_name = request.args.get('player_name')
    point_score = request.args.get('point_score')
    team = request.args.get('team')

    player = update_points(player_name, point_score, team)
    compute = ComputeTotalScore(TEAMS)
    total = compute.compute_total()

    if player is None:
        return render_template('index.html',
                               error_message='Player not found or score input error.',
                               total1=total[0], total2=total[1])
    else:
        compute = ComputeTotalScore(TEAMS)
        total = compute.compute_total()

        return render_template('index.html', player_name=player_name,
                               point_score=TEAMS[team]['scores'][player],
                               team=team, total1=total[0], total2=total[1])


def update_points(player_name, point_score, team):

    if point_score is not None:
        if int(point_score) < 1:
            return None
        elif int(point_score) > 3:
            return None

    try:
        player = TEAMS[team]['players'][player_name]
        TEAMS[team]['scores'][player] += int(point_score)
    except:
        player = None

    return player


if __name__ == '__main__':
    APP.run(debug=True)
