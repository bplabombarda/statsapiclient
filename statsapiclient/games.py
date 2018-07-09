from statsapiclient import _fetch_json


class Game:
    """
    A game object to access boxscore and play-by-play data
    Args:
        :game_pk: The primary key for the target game.
    """
    _endpoint = 'api/v1/game/{game_pk}/feed/live'
    params = {}

    def __init__(self, game_pk):
        self.game_pk = game_pk
        self.game_endpoint = self._endpoint.format(
                                game_pk=self.game_pk)
        self.json = _fetch_json(
                        endpoint=self.game_endpoint,
                        params=self.params)

    def _handle_game_data(self, json):
        return json['gameData']
        
    def get_game_data(self):
        return self._handle_game_data(self.json)