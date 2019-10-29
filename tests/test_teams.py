from statsapiclient.teams import Teams

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


class TestTeams:
    def test_get_active(self):
        teams = Teams()
        teams.data = mock_teams
        active = teams.get_active()

        assert active == mock_teams[:2]

    def test_get_active_by_conference(self):
        teams = Teams()
        teams.data = mock_teams
        by_conference = teams.get_active_by_conference()

        expected = {
            "conf_a": [mock_teams[0]],
            "conf_b": [mock_teams[1]],
        }

        assert by_conference == expected

    def test_get_active_by_division(self):
        teams = Teams()
        teams.data = mock_teams
        by_division = teams.get_active_by_division()

        expected = {
            "div_a": [mock_teams[0]],
            "div_b": [mock_teams[1]],
        }

        assert by_division == expected
