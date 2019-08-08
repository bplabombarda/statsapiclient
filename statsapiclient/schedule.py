from .utils import fetch_json


class Schedule:
    """
    Schedule of all games on a given date or within a given date range.
    Args:
        :start_date: Date string in the format 'YYYY-MM-DD'
        :end_date: Date string in the format 'YYYY-MM-DD' (optional)
    """

    endpoint = "api/v1/schedule"
    params = {
        "expand": "schedule.teams,schedule.linescore,schedule.decisions,schedule.scoringplays"
    }

    def __init__(self, start_date, end_date=None):
        self.params["startDate"] = start_date
        self.params["endDate"] = end_date if end_date else start_date
        json = fetch_json(endpoint=self.endpoint, params=self.params)
        self.dates = json["dates"]

    def games_from_dates(self, dates):
        games = []
        for date in dates:
            games += [game for game in date["games"]]

        return games

    def get_games(self):
        return self.games_from_dates(self.dates)
