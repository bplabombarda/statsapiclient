import pytest

from statsapiclient import Schedule


s = Schedule('2017-10-23')
g = s.get_games()

def test_schedule():
	gk1 = g[0]['gamePk']
	gk2 = g[1]['gamePk']

	assert gk1 == 2017020123 and gk2 == 2017020124
