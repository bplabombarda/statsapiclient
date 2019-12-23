"""This class allows retrieval of game data as different
types and layouts of the game data."""

from requests import HTTPError

from statsapiclient.line_score import LineScore
from statsapiclient.plays import Plays
from statsapiclient.summary import Summary
from statsapiclient.utils import fetch_json


class Game:
    """Score and play data for a particular NHL game.
    Args:
        :game_pk: The game primary key
    """
    def __init__(self, game_pk):
        self.game_pk = game_pk
        self.endpoint = f"api/v1/game/{game_pk}/feed/live"

        try:
            # Fetch json data for this game - we expect a HTTPError
            # if this is not successful.
            self.json = fetch_json(self.endpoint)

            # Build game data objects - we expect a KeyError if the
            # data cannot be found in the parsed dict.
            self.line_score = LineScore(self.json["liveData"]["linescore"])
            self.plays = Plays(self.json["liveData"]["plays"])
            # self.line_score = BoxScore(self.json["liveData"]["linescore"])
        except HTTPError as error:
            raise error
        except KeyError as error:
            raise error

    def get_summary(self):
        """Gets game summary data dict."""
        penalty_plays = self.plays.get_penalty_plays()
        scoring_plays = self.plays.get_scoring_plays()
        summary = Summary(penalty_plays, scoring_plays).game_summary

        return summary

    def __repr__(self):
        return f"<Game game_pk=${self.game_pk}>"
