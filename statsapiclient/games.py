"""This class allows retrieval of game data as different
types and layouts of the game data."""

from statsapiclient.line_score import LineScore
from statsapiclient.plays import Play
from statsapiclient.shifts import Shifts
from statsapiclient.utils import fetch_json


class Game:
    """Score and play data for a particular NHL game.

    Parameters
    ----------
    game_pk : str
        The game's primary key.

    Properties
    ----------
    game_pk : str
        Primary key of the game.

    endpoint : str
        The API game endpoint for the game_pk passed.

    json : dict
        The raw response from the API endpoint.

    box_score : BoxScore
        A BoxScore object created from the game's data.

    line_score : LineScore
        A LineScore object created from the game's data.

    plays : Play
        A Play object created from the game's gata.

    shifts : Shifts
        A Shifts object created from the game's data.
    """
    def __init__(self, game_pk):
        self.game_pk = game_pk
        self.endpoint = f"api/v1/game/{game_pk}/feed/live"
        self.json = fetch_json(self.endpoint)
        self.type = self.json["gameData"]["game"]["type"]

        if self.type in ("R", "P"):
            self.line_score = self.build_line_score()
            self.plays = self.build_plays()
            self.shifts = Shifts(game_pk)

    def __repr__(self):
        return f"<Game game_pk={self.game_pk}>"

    def build_line_score(self):
        """Parses linescore data into LineScore dataclass."""
        line_score_data = self.json["liveData"]["linescore"]
        line_score = LineScore(
            line_score_data["currentPeriod"],
            line_score_data["currentPeriodOrdinal"],
            line_score_data["currentPeriodTimeRemaining"],
            line_score_data["hasShootout"],
            line_score_data["intermissionInfo"]["inIntermission"],
            line_score_data["powerPlayStrength"]
        )

        return line_score

    def build_plays(self):
        """Builds and returns Play object."""
        play_data = self.json["liveData"]["plays"]
        plays = Play(
            play_data["allPlays"],
            play_data["currentPlay"],
            play_data["penaltyPlays"],
            play_data["scoringPlays"],
            play_data["playsByPeriod"]
        )

        return plays
