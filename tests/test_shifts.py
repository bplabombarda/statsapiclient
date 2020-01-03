from unittest.mock import patch

from statsapiclient.shifts import Shift


class TestShift:
    @patch("statsapiclient.shifts.fetch_html")
    @patch("statsapiclient.shifts.BeautifulSoup")
    def test_instantiate_shift(self, mock_fetch, MockSoup):
        shift = Shift("2000123456")

        expected_away = "/scores/htmlreports/20002001/TV123456.HTM"
        expected_home = "/scores/htmlreports/20002001/TH123456.HTM"

        assert shift.away_url == expected_away
        assert shift.home_url == expected_home

    @patch("statsapiclient.shifts.fetch_html")
    @patch("statsapiclient.shifts.BeautifulSoup")
    def test_repr(self, mock_fetch, MockSoup):
        shift = Shift("2000123456")

        assert shift.__repr__() == "<Shift full_key=2000123456>"
