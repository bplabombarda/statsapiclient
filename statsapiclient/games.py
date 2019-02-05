from .fetch_json import fetch_json


class Game:
    """
    Schedule of all games on a given date or within a given date range.
    Args:
        :start_date: Date string in the format 'YYYY-MM-DD'
        :end_date: Date string in the format 'YYYY-MM-DD' (optional)
    """
    
    endpoint = "api/v1/game/{gamePk}/feed/live"
    params = {
        "expand": "schedule.teams,schedule.linescore,schedule.decisions,schedule.scoringplays"
    }

    def __init__(self):
        return

    def get_play_by_play(self):
        return

    def get_box_score(self):
        return
