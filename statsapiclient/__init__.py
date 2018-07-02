import re
import os
import json 
from datetime import datetime

from requests import get


class Client:
	TODAY = datetime.today()
	BASE_URL = 'https://statsapi.web.nhl.com/{endpoint}'
	HEADERS = {
		'user-agent': ('Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'),
		'Dnt': ('1'),
		'Accept-Language': ('en'),
	    'origin': ('https://statsapi.web.nhl.com')
		}

	def __init__(self):
		return

	def _build_url(self, path):
		return self.BASE_URL.format(endpoint=path)

	def _request(self, path, params):
		url = self._build_url(path)
		req = get(url, params=params)

		return req.json()

	def fetch(self, path, params):
		return self._request(path, params)