from unittest import TestCase
from unittest.mock import patch

from statsapiclient.shifts import Shift


class TestShift(TestCase):
    @patch("statsapiclient.shifts.fetch_html")
    @patch("statsapiclient.shifts.BeautifulSoup")
    def test_instantiate_shift(self, mock_fetch, MockSoup):
        shift = Shift("2000123456")

        expected_away = "/scores/htmlreports/20002001/TV123456.HTM"
        expected_home = "/scores/htmlreports/20002001/TH123456.HTM"

        self.assertEqual(shift.away_url, expected_away)
        self.assertEqual(shift.home_url, expected_home)

    @patch("statsapiclient.shifts.fetch_html")
    @patch("statsapiclient.shifts.BeautifulSoup")
    def test_repr(self, mock_fetch, MockSoup):
        shift = Shift("2000123456")

        expected = "<Shift full_key=2000123456>"
        self.assertEqual(shift.__repr__(), expected)
