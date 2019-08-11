from .utils import fetch_json


class Teams:
    """
    Lists of NHL teams.
    """

    endpoint = "api/v1/teams"

    def __init__(self):
        json = fetch_json(endpoint=self.endpoint)
        self.data = json["teams"]

    def get_active(self):
        return [team for team in self.data if team.active]

    def get_active_by_conference(self):
        conferences = {
            "eastern": [],
            "western": [],
        }

        for team in self.data:
            conference = team["conference"]["name"].lower()
            conferences[conference].append(team)

        return conferences

    def get_active_by_division(self):
        divisions = {
            "atlantic": [],
            "central": [],
            "metropolitan": [],
            "pacific": [],
        }

        for team in self.data:
            division = team["division"]["name"].lower()
            divisions[division].append(team)

        return divisions
