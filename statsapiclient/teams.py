"""This class allows retrieval of active teams by conference,
division, or all active teams."""

from .utils import fetch_json


class Teams:
    """Lists of NHL teams by conference or division.
    """

    endpoint = "api/v1/teams"

    def __init__(self):
        json = fetch_json(endpoint=self.endpoint)
        self.data = json["teams"]

    def get_active(self):
        """Returns a list of active teams.
        Returns:
            list: active teams
        """
        return list(filter(
            lambda team: team["active"] is True, self.data))

    def get_active_by_conference(self):
        """Returns a list of active teams by conference.
        Returns:
            list: active teams by conference
        """
        conferences = {}

        for team in self.data:
            conference = team["conference"]["name"].lower()

            if team["active"] is True:
                if conference not in conferences:
                    conferences[conference] = [team]
                else:
                    conferences[conference].append(team)

        return conferences

    def get_active_by_division(self):
        """Returns a list of active teams by division.
        Returns:
            list: active teams by division
        """
        divisions = {}

        for team in self.data:
            division = team["division"]["name"].lower()

            if team["active"] is True:
                if division not in divisions:
                    divisions[division] = [team]
                else:
                    divisions[division].append(team)

        return divisions
