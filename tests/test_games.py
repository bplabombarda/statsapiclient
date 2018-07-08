import pytest

from statsapiclient import Game


g = Game(2017020123)

def test_schedule():
	teams = g['gameData']['teams']

	assert teams['away']['name'] == 'Los Angeles Kings'
