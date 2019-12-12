"""This class allows retrieval of game data as different
types and layouts of said data.
"""
from requests import HTTPError

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
            self.json = fetch_json(self.endpoint)
            self.box_score = self.json["liveData"]["boxscore"]
            self.line_score = self.json["liveData"]["linescore"]
            self.plays = self.json["liveData"]["plays"]
            self.summary = self.build_summary()
        except HTTPError as error:
            raise Exception(f"{error}")
        except KeyError as error:
            raise Exception(f"{error}")

    def build_summary(self):
        """Build summary data dict."""
        penalty_plays = self.filter_plays(self.plays, "penaltyPlays")
        penalty_plays = list(map(self.build_event_play, penalty_plays))

        scoring_plays = self.filter_plays(self.plays, "scoringPlays")
        scoring_plays = list(map(self.build_event_play, scoring_plays))

        return {
            "penalty_plays": penalty_plays,
            "scoring_plays": scoring_plays,
        }

    @staticmethod
    def build_event_play(play):
        """Create a play dict for game summary.
        Args:
            :play: A play dict from raw play-by-play data.
        """
        strength = ""

        if play["result"]["eventTypeId"] == "GOAL":
            strength = play["result"]["strength"]["name"]

        if play["result"]["eventTypeId"] == "PENALTY":
            penalty = play["result"]["secondaryType"]
            minutes = play["result"]["penaltyMinutes"]
            strength = f"{penalty} ({minutes} min)"

        return {
            "period": play["about"]["ordinalNum"],
            "time": play["about"]["periodTimeRemaining"],
            "team": play["team"]["triCode"],
            "strength": strength,
            "description": play["result"]["description"],
        }

    @staticmethod
    def filter_plays(plays, play_type):
        """Filter for only penalty or only scoring plays.
        Args:
            :play_type: Either `penaltyPlays` or `scoringPlays`
        Returns:
            list: A list of plays of the given event type.
        """
        all_plays = plays["allPlays"]
        event_plays = plays[play_type]

        return list(filter(
            lambda p: p["about"]["eventIdx"] in event_plays, all_plays))

    def __repr__(self):
        return f"<Game game_pk=${self.game_pk}>"
