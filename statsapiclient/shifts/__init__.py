"""This class holds all shift data."""
from bs4 import BeautifulSoup

from statsapiclient.constants import SEASON_YEARS
from statsapiclient.utils import fetch_html
from statsapiclient.shifts.parser import ShiftReportParser


class Shifts:
    """This is where the shift data happens.

    Args:
        game_pk : int
            The game's primary key.
    """
    def __init__(self, game_pk):
        self.game_pk = game_pk

        year = SEASON_YEARS.get(self.game_pk[:4])
        partial_key = self.game_pk[4:]

        away_url = f"/scores/htmlreports/{year}/TV{partial_key}.HTM"
        home_url = f"/scores/htmlreports/{year}/TH{partial_key}.HTM"

        self.away = self.parse_shift_report(fetch_html(away_url))
        self.home = self.parse_shift_report(fetch_html(home_url))

    @staticmethod
    def parse_shift_report(raw_html):
        """Parse shift report HTML"""

        return ShiftReportParser(raw_html).parse()

    def __repr__(self):
        return f"<Shifts full_key={self.game_pk}>"
