from ..utils import fetch_json


class Game:
    """
    Score and play data for a particular NHL game.
    Args:
        :game_pk: The game primary key 
    """

    _endpoint = "api/v1/game/{game_pk}/feed/live"

    def __init__(self, game_pk):
        self.endpoint = _endpoint.format(game_pk)
        self.json = fetch_json(endpoint=self.endpoint)

    def get_box_score(self):
        return self.json["boxscore"]["plays"]

    def get_line_score(self):
        return self.json["linescore"]["plays"]

    def get_play_by_play(self):
        return self.json["liveData"]["plays"]
