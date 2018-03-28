import json
import requests

from statsapiclient.constants import headers

class StatsApiClient:
	
	def __init__(self):
		self.src_data = None
		self.req_err = None

	def get_date_string_format():
		return 'YYYYMMDD'

	def get_base_uri(self):
		return 'https://statsapi.web.nhl.com/'

	def get_headers(self):
		return {
			'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
      'referer': 'http://nhl.com/stats/'
    }

	def build_request(self):
		return

	def fetch(self, uri):
		return requests.get(uri).json()

	def get_games_uri(self, date):
		return '{}{}'.format(
			self.get_base_uri(), 
			'api/v1/schedule?startDate={}&endDate={}'.format(date, date)
		)

	def get_games(self, date):
		return self.fetch(self.get_games_uri(date))

	def get_game_data(self, game_pk):
		return '{}{}'.format(
			self.get_base_uri(),
			'api/v1/game/{}/feed/live'.format(game_pk)
		)
