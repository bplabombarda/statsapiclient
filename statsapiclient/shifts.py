"""This class holds all shift data and contains
 methods to access it.
"""
from statsapiclient.constants import SEASON_YEARS
from statsapiclient.utils import fetch_html


class Shift:
    """This is where the shift data happens.

    Parameters
    ----------
    game_pk : int
        The game's primary key.
    """
    def __init__(self, game_pk):
        # TODO: make a `year_from_pk` utility.
        year = SEASON_YEARS.get(game_pk[:4])
        pk = game_pk[4:]

        away_url = f"/scores/htmlreports/{year}/TV{pk}.HTM"
        home_url = f"/scores/htmlreports/{year}/TH{pk}.HTM"

        self.away_raw = fetch_html(away_url)
        self.home_raw = fetch_html(home_url)

        self.away_toi = self.parse_shift_report(self.away_raw)
        self.home_toi = self.parse_shift_report(self.home_raw)

    def __repr__(self):
        return f"<Shift game_pk={self.game_pk}>"

    def parse_shift_report(self, raw_html):
        
        return
