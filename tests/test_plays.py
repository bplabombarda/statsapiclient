from statsapiclient.plays import Plays

mock_plays = {
    "all_plays": [1, 2, 3, 4, 5, 6],
    "current_play": {"My": "play"},
    "penalty_indicies": [1, 2, 3],
    "scoring_indicies": [4, 5, 6],
    "play_indicies_by_period": {
        "1": {},
        "2": {},
        "3": {},
    },
}


class TestPlays:
    def test_instantiate_plays(self):
        plays = Plays(**mock_plays)

        assert plays.all_plays == [1, 2, 3, 4, 5, 6]
        assert plays.current_play == {"My": "play"}
        assert plays.penalty_indicies == [1, 2, 3]
        assert plays.scoring_indicies == [4, 5, 6]
        assert plays.play_indicies_by_period == {"1": {}, "2": {}, "3": {}}
