"""This class allows retrieval of game data as different
types and layouts of the game data."""

from statsapiclient.box_score import BoxScore
from statsapiclient.line_score import LineScore
from statsapiclient.plays import Plays
from statsapiclient.summary import Summary
from statsapiclient.utils import fetch_json


class Game:
    """Score and play data for a particular NHL game.
    Args:
        :game_pk: The game's primary key.
    """
    def __init__(self, game_pk):
        self.game_pk = game_pk
        self.endpoint = f"api/v1/game/{game_pk}/feed/live"
        self.json = fetch_json(self.endpoint)
        self.box_score = self.__build_box_score()
        self.line_score = self.__build_line_score()
        self.plays = self.__build_plays()

    def __repr__(self):
        return f"<Game game_pk={self.game_pk}>"

    def __build_box_score(self):
        """Parses linescore data into LineScore dataclass."""
        box_score_data = self.json["liveData"]["boxscore"]
        box_score = BoxScore(box_score_data)

        return box_score

    def __build_line_score(self):
        """Parses linescore data into LineScore dataclass."""
        line_score_data = self.json["liveData"]["linescore"]
        line_score = LineScore(
            line_score_data["currentPeriod"],
            line_score_data["currentPeriodOrdinal"],
            line_score_data["currentPeriodTimeRemaining"],
            line_score_data["hasShootout"],
            line_score_data["intermissionInfo"]["isIntermission"],
            line_score_data["powerPlayStrength"]
        )

        return line_score

    def __build_plays(self):
        """Builds and returns Plays object."""
        play_data = self.json["liveData"]["plays"]
        plays = Plays(
            play_data["allPlays"],
            play_data["currentPlay"],
            play_data["penaltyPlays"],
            play_data["scoringPlays"],
            play_data["playsByPeriod"]
        )

        return plays

    def get_summary(self):
        """Gets game summary data dict.
        TODO:
        Maybe write examples on how to achieve this from core
        modules rather than build to such a specific case.
        """
        penalty_plays = self.plays.get_penalty_plays()
        scoring_plays = self.plays.get_scoring_plays()
        summary = Summary(penalty_plays, scoring_plays).game_summary

        return summary
