from unittest.mock import patch

from statsapiclient.game import Game

mock_game = {
    "liveData": {
        "boxscore": {"this_is": "the boxscore"},
        "linescore": {"this_is": "the line score"},
        "plays": {
            "allPlays": [
                {"about": {"eventIdx": 0}},
                {"about": {"eventIdx": 1}},
                {"about": {"eventIdx": 2}},
            ],
            "penaltyPlays": [1],
            "scoringPlays": [2],
        }
    }
}


def mock_json():
    return mock_game


class TestGame:
    # TODO: Do this
    @patch('statsapiclient.utils.fetch_json', side_effect=mock_json)
    def test_box_score(self, fetch):
        game = Game('123456789')

        assert game.box_score == {"this_is": "the box score"}

    @patch('statsapiclient.utils.fetch_json', side_effect=mock_json)
    def test_line_score(self, fetch):
        game = Game('123456789')

        assert game.line_score == {"this_is": "the line score"}

    def test_plays(self):
        assert True

    def test_penalty_plays(self):
        assert True

    def test_scoring_plays(self):
        assert True

    def test_summary(self):
        assert True

    def test_filter_plays(self):
        plays = mock_game["liveData"]

        # assert Game.filter_plays()
        assert True
