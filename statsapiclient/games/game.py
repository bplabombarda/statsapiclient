from requests import HTTPError

from statsapiclient.games.line_score import LineScore
from ..utils import fetch_json


class Game:
    """Score and play data for a particular NHL game.
    Args:
        :game_pk: The game primary key 
    """

    endpoint = "api/v1/game/{game_pk}/feed/live"

    def __init__(self, game_pk):
        self.pk =  game_pk
        game_endpoint = self.endpoint.format(game_pk=self.pk)
        try:
            self.error = None
            self.json = fetch_json(endpoint=game_endpoint)
        except HTTPError as error:
            self.error = error
            self.json = None

    def _filter_plays(self, type):
        """Filter for only penalty or only scoring plays.
        Args:
            :type: The play type. Either `penaltyPlays` or `scoringPlays`
        """
        plays = self.get_plays()
        all_plays = plays["allPlays"]
        event_plays = plays[type]
        
        return list(filter(
            lambda p: p["about"]["eventIdx"] in event_plays, all_plays
        ))

    def _build_event_play(self, play):
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

    def get_box_score(self):
        """Gets game boxscore data."""
        return self.json["liveData"]["boxscore"]

    def get_line_score(self):
        """Gets game linescore object."""
        data = self.json["liveData"]["linescore"]

        return LineScore(data)

    def get_plays(self):
        """Gets game play data."""
        return self.json["liveData"]["plays"]

    def get_penalty_plays(self):
        """Gets a list of penalty plays."""
        return self._filter_plays("penaltyPlays")

    def get_scoring_plays(self):
        """Gets a list of scoring plays."""
        return self._filter_plays("scoringPlays")

    def get_summary(self):
        """Gets game summary data dict."""
        penalty_plays = list(map(
            self._build_event_play,
            self.get_penalty_plays()
        ))
        scoring_plays = list(map(
            self._build_event_play,
            self.get_scoring_plays()
        ))

        return {
            "penalty_plays": penalty_plays,
            "scoring_plays": scoring_plays,
        }

    def __repr__(self):
        return f"<Game pk=${self.pk}>"
