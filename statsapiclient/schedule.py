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

        json = fetch_json(endpoint=self.endpoint, params=self.params)
        self.games = [game for date in json["dates"] for game in date["games"]]
