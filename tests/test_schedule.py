import pytest

from statsapiclient import Schedule


s = Schedule('2017-10-23')
g = s.get_games()

gk_one = games[0]['gamePk']
gk_two = games[1]['gamePk']

def test_schedule():
	assert gk_one == 2017020123 and gk_two == 2017020124
