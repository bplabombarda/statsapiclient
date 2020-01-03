from statsapiclient.plays import Play

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

mock_plays_by_period = {
    "all_plays": [
        {"about": {"eventIdx": 0}},
        {"about": {"eventIdx": 1}},
        {"about": {"eventIdx": 2}},
        {"about": {"eventIdx": 3}},
        {"about": {"eventIdx": 4}},
        {"about": {"eventIdx": 5}},
    ],
    "current_play": {"My": "play"},
    "penalty_indicies": [1, 2, 3],
    "scoring_indicies": [4, 5, 6],
    "play_indicies_by_period": {
        1: {"startIndex": 0, "endIndex": 1},
        2: {"startIndex": 2, "endIndex": 3},
        3: {"startIndex": 4, "endIndex": 5}
    },
}


class TestPlays:
    def test_instantiate_plays(self):
        plays = Play(**mock_plays)

        assert plays.all_plays == [1, 2, 3, 4, 5, 6]
        assert plays.current_play == {"My": "play"}
        assert plays.penalty_indicies == [1, 2, 3]
        assert plays.scoring_indicies == [4, 5, 6]
        assert plays.play_indicies_by_period == {"1": {}, "2": {}, "3": {}}

    def test_get_plays_by_period(self):
        plays = Play(**mock_plays_by_period)

        first = [{"about": {"eventIdx": 0}}, {"about": {"eventIdx": 1}}]
        assert plays.get_plays_by_period(1) == first

        second = [{"about": {"eventIdx": 2}}, {"about": {"eventIdx": 3}}]
        assert plays.get_plays_by_period(2) == second

        third = [{"about": {"eventIdx": 4}}, {"about": {"eventIdx": 5}}]
        assert plays.get_plays_by_period(3) == third
