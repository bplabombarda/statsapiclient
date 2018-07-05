from statsapiclient import _fetch_json


class Game:
    _endpoint = 'api/v1/game/{game_pk}/feed/live'
    params = {}

    def __init__(self, game_pk):
        self.game_pk = game_pk
        self.game_endpoint = self._endpoint.format(
                                game_pk=self.game_pk)
        self.json = _fetch_json(
                        endpoint=self.game_endpoint,
                        params=self.params)

    def play_by_play(self):
        return

    def boxscore(self):
        return
    
    def scoring_plays(self):
        return