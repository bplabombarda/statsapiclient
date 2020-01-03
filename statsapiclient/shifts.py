"""This class holds all shift data and contains
 methods to access it.
"""
from bs4 import BeautifulSoup

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
        self.full_key = game_pk
        self.year = SEASON_YEARS.get(self.full_key[:4])
        self.pk = self.full_key[4:]

        self.away_url = f"/scores/htmlreports/{self.year}/TV{self.pk}.HTM"
        self.home_url = f"/scores/htmlreports/{self.year}/TH{self.pk}.HTM"

        self.away_raw = fetch_html(self.away_url)
        self.home_raw = fetch_html(self.home_url)

        self.away_toi = self.parse_shift_report(self.away_raw)
        self.home_toi = self.parse_shift_report(self.home_raw)

    def __repr__(self):
        return f"<Shift full_key={self.full_key}>"

    def parse_shift_report(self, raw_html):
        soup = BeautifulSoup(raw_html, "html.parser")
        return soup
