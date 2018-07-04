import re
import os
import json 
from datetime import datetime

from requests import get


TODAY = datetime.today()
BASE_URL = 'https://statsapi.web.nhl.com/{endpoint}'
HEADERS = {
	'user-agent': ('Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'),
	'Dnt': ('1'),
	'Accept-Language': ('en'),
    'origin': ('https://statsapi.web.nhl.com'),
    'referer': ('https://www.nhl.com/')
	}

	
def _fetch_json(endpoint, params):
    """
    Helper method for json fetching.
    Args:
        endpoint (str): resource endpoint
        params (dict): query parameters
    Raises:
        HTTPError: if requests does not return 200
    Returns:
        json: json object for selected API call
    """
    h = dict(HEADERS)
    fetch = get(BASE_URL.format(endpoint=endpoint), params=params, headers=h)
    
    fetch.raise_for_status()
    return fetch.json()


class Schedule:
    """
    Schedule of all games on a given date or within a given date range.
    Args:
        :start_date: Date string in the format 'YYYY-MM-DD'
        :end_date: Date string in the format 'YYYY-MM-DD' (optional)
    """
    _endpoint = 'api/v1/schedule'
    params = {'expand': 'schedule.teams,schedule.linescore,schedule.decisions,schedule.scoringplays'}

    def __init__(self, start_date, end_date=None):
        self.start_date = start_date
        self.end_date = end_date
        if not self.end_date:
            self.params['startDate'] = self.start_date
            self.params['endDate'] = self.start_date
        else:
            self.params['startDate'] = self.start_date
            self.params['endDate'] = self.end_date
        self.json = _fetch_json(endpoint=self._endpoint, params=self.params)

    def _set_date_params(start, end):
        return 

    def _handle_games(self, json):
        games = []
        for date in json['dates']:
            games += [game for game in date['games']]

        return games
    
    def _build_result(self, game):
        away = game['linescore']['teams']['away']
        home = game['linescore']['teams']['home']
        result = {
            'gamePk': game['gamePk'],
            'gameDate': game['gameDate'],
            'away': {
                'team': home['team']['name'],
                'goals': home['goals'],
                'shots': home['shotsOnGoal']
            },
            'home': {
                'team': away['team']['name'],
                'goals': away['goals'],
                'shots': away['shotsOnGoal']
            }
        }
        
        return result
    
    def _handle_results(self, json):
        results = []
        for date in json['dates']:
            results += [self._build_result(game) for game in date['games']]
            
        return results

    def get_games(self):
        return self._handle_games(self.json)
    
    def get_results(self):
        return self._handle_results(self.json)