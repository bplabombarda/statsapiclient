from statsapiclient.line_score import LineScore


mock_box_score = {
    "current_period": 1,
    "current_period_display": "1st",
    "current_period_time_remaining": "20:00",
    "has_shootout": False,
    "is_at_intermission": False,
    "power_play_strength": "Even",
}


class TestBoxScore:
    def test_instantiate_box_score(self):
        line_score = LineScore(**mock_box_score)

        assert line_score.current_period == 1
        assert line_score.current_period_display == "1st"
        assert line_score.current_period_time_remaining == "20:00"
        assert line_score.has_shootout is False
        assert line_score.is_at_intermission is False
        assert line_score.power_play_strength == "Even"
