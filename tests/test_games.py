from unittest.mock import patch

from statsapiclient.games import Game


class TestGame:
    @patch("statsapiclient.games.fetch_json")
    @patch("statsapiclient.games.Shifts")
    def test_instantiate_game(self, mock_fetch, MockShift):
        game = Game("2000123456")

        assert game.game_pk == "2000123456"

    @patch("statsapiclient.games.fetch_json")
    @patch("statsapiclient.games.Shifts")
    def test_repr(self, mock_fetch, MockShift):
        game = Game("2000123456")

        assert game.__repr__() == "<Game game_pk=2000123456>"
