from .constants import SCHEDULE_PARAMS
from .utils import fetch_json


class Schedule:
    """Schedule of all games on a given date or within a given date range.
    Args:
        :start_date: Date string in the format 'YYYY-MM-DD'
        :end_date: Date string in the format 'YYYY-MM-DD' (optional)
    """

    endpoint = "api/v1/schedule"

    params = {
        "expand": SCHEDULE_PARAMS
    }

    def __init__(self, start_date, end_date=None):
        self.params["startDate"] = start_date
        self.params["endDate"] = end_date if end_date else start_date

        json = fetch_json(endpoint=self.endpoint, params=self.params)
        self.data = json["dates"]

    def get_games(self):
        """Returns a list of games compiled from a date or date range."""
        games = []

        for date in self.data:
            games += [game for game in date["games"]]

        return games
