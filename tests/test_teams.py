from unittest import TestCase
from unittest.mock import patch

from statsapiclient.teams import Team

mock_teams = [
    {
        "active": True,
        "conference": {
            "name": "CONF_A",
        },
        "division": {
            "name": "DIV_A",
        },
    },
    {
        "active": True,
        "conference": {
            "name": "CONF_B",
        },
        "division": {
            "name": "DIV_B",
        },
    },
    {
        "active": False,
        "conference": {
            "name": "CONF_Z",
        },
        "division": {
            "name": "DIV_X",
        },
    },
]


@patch("statsapiclient.teams.fetch_json")
class TestTeam(TestCase):
    def test_get_active(self, mock_fetch):
        teams = Team()
        teams.data = mock_teams
        active = teams.get_active()

        self.assertEqual(active, mock_teams[:2])
