from statsapiclient import _get_json


class Game:
	_endpoint = 'api/v1/game/{game_pk}/feed/live'

	def __init__(self, game_pk):
		self.game_pk = game_pk
		self.game_endpoint = self._endpoint.format(self.game_pk)
		self.json = _fetch_json(endpoint=self.game_endpoint,
								params=self.params)

	def play_by_play(self):
		url = self._endpoint.format(game_pk=self.game_pk)
		response = self.fetch(url, params=None)

		return response['liveData']['plays']

	def boxscore(self):
		url = self._endpoint.format(game_pk=self.game_pk)
		response = self.fetch(url, params=None)

		return response['liveData']['boxscore']