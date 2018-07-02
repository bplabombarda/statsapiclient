from statsapiclient import Client


class Game(Client):
	_endpoint = 'api/v1/game/{game_pk}/feed/live'

	def __init__(self, game_pk):
		self.game_pk = game_pk

	def play_by_play(self):
		url = self._endpoint.format(game_pk=self.game_pk)
		response = self.fetch(url, params=None)

		return response['liveData']['plays']

	def boxscore(self):
		url = self._endpoint.format(game_pk=self.game_pk)
		response = self.fetch(url, params=None)

		return response['liveData']['boxscore']