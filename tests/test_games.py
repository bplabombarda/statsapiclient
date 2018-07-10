import pytest

from statsapiclient.games import Game


g = Game(2017020123)

def test_game_data():
	gd = g.get_game_data()
	away = gd['teams']['away']
	home = gd['teams']['home']

	assert away['id'] == 26 and home['id'] == 10
