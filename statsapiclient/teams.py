from .utils import fetch_json


class Teams:
    """
    Lists of NHL teams by conference or division.
    """

    endpoint = "api/v1/teams"

    def __init__(self):
        json = fetch_json(endpoint=self.endpoint)
        self.data = json["teams"]

    def get_active(self):
        return [team for team in self.data if team.active]

    def get_active_by_conference(self):
        conferences = {}

        for team in self.data:
            conference = team["conference"]["name"].lower()

            if not conference in conferences:
                conferences[conference] = [team]
            else:
                conferences[conference].append(team)

        return conferences

    def get_active_by_division(self):
        divisions = {}

        for team in self.data:
            division = team["division"]["name"].lower()

            if not division in divisions:
                divisions[division] = [team]
            else:
                divisions[division].append(team)

        return divisions
