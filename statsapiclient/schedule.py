"""This class allows retrieval of games from a given
date or date range.
"""


from datetime import datetime

from .constants import SCHEDULE_PARAMS, SCHEDULE_DATE_FORMAT
from .utils import fetch_json


class Schedule:
    """Schedule of all games on a given date or within a given date range.
    Args:
        :start_date: Date string in the format 'YYYY-MM-DD'
        :end_date: Date string in the format 'YYYY-MM-DD' (optional)
    """

    def __init__(self, start_date, end_date=None):
        self.endpoint = "api/v1/schedule"
        self.params = {"expand": SCHEDULE_PARAMS}

        self.validate_date(start_date)

        if end_date:
            self.validate_date(end_date)

        self.params["startDate"] = start_date
        self.params["endDate"] = end_date if end_date else start_date

        json = fetch_json(endpoint=self.endpoint, params=self.params)
        self.data = json["dates"]

    def get_games(self):
        """Gets a list of games compiled from a date or date range.
        Returns:
            list: flattened list of games in a given date range
        """
        games = []

        for date in self.data:
            games += date["games"]

        return games

    @staticmethod
    def validate_date(date):
        """Validates that a date meets the specified format."""
        try:
            datetime.strptime(date, SCHEDULE_DATE_FORMAT.get('format'))
            return True
        except ValueError:
            format_display = SCHEDULE_DATE_FORMAT.get('display')

            raise ValueError(
                f"Incorrect data format, should be {format_display}")
