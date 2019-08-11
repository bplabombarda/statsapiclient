from .line_score import LineScore
from ..utils import fetch_json


class Game:
    """Score and play data for a particular NHL game.
    Args:
        :game_pk: The game primary key 
    """

    endpoint = "api/v1/game/{game_pk}/feed/live"

    def __init__(self, game_pk):
        game_endpoint = self.endpoint.format(game_pk=game_pk)
        self.json = fetch_json(endpoint=game_endpoint)

    def get_box_score(self):
        """Gets game boxscore data."""
        return self.json["liveData"]["boxscore"]

    def get_line_score(self):
        """Gets game linescore data."""
        return self.json["liveData"]["linescore"]

    def get_play_by_play(self):
        """Gets game play data."""
        return self.json["liveData"]["plays"]
