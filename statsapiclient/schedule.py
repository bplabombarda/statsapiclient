"""This class allows retrieval of games from a given
date or date range."""

from statsapiclient.constants import SCHEDULE_PARAMS
from statsapiclient.utils import fetch_json, validate_date


class Schedule:
    """Schedule of all games on a given date or within a given date range.

    Parameters
    ----------
    start_date : str
        Date string for start of range in the format 'YYYY-MM-DD'.

    end_date : str
        Date string for end of range in the format 'YYYY-MM-DD' (optional).
    """
    def __init__(self, start_date, end_date=None):
        self.endpoint = "api/v1/schedule"
        self.params = {"expand": SCHEDULE_PARAMS}

        validate_date(start_date)

        if end_date:
            validate_date(end_date)

        self.params["startDate"] = start_date
        self.params["endDate"] = end_date if end_date else start_date

        self.games = self.get_games()

    def get_date_range(self):
        """Gets the date range for the schedule object.

        Returns:
            tuple: a tuple of two date strings
        """
        start_date = self.params["startDate"]
        end_date = self.params["endtDate"]

        return (start_date, end_date)

    def get_games(self):
        """Gets games for the objects date range.

        Returns:
            list: a list of game dicts
        """
        json = fetch_json(endpoint=self.endpoint, params=self.params)

        return [game for date in json["dates"] for game in date["games"]]
