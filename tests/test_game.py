from unittest.mock import patch

from statsapiclient.game import Game


class TestGame:
    @patch("statsapiclient.game.fetch_json")
    def test_instantiate_game(self, mock_fetch):
        game = Game(123456)

        assert game.game_pk == 123456

    @patch("statsapiclient.game.fetch_json")
    def test_repr(self, mock_fetch):
        game = Game(654321)

        assert game.__repr__() == "<Game game_pk=654321>"
