"""This class allows retrieval of active teams by conference,
division, or all active teams."""

from .utils import fetch_json


class Team:
    """Lists of NHL teams by conference or division.
    """

    endpoint = "api/v1/teams"

    def __init__(self):
        json = fetch_json(endpoint=endpoint)
        self.data = []

        for n in ([i for i in range(0, 110)] + [5524, 5814, 5844, 7202, 7460, 7461]):
            res = fetch_json(f"{endpoint}/{n}")
            teams = res.json().get("teams", ())

            self.data += teams

    def get_all(self):
        """Returns a list of all teams.
        Returns:
            list: all teams
        """
        return self.data

    def get_active(self):
        """Returns a list of active teams.
        Returns:
            list: active teams
        """
        return list(filter(
            lambda team: team["active"] is True, self.data))

    def get_by_id(self, id):
        """Gets team object by given id.
        
        Args:
            id (int): the team id
            
        Returns:
            dict: the team dict
        """

        matches = list(filter(lambda t: t["id"] == id, self.data))

        if len(matches) > 1:
            print(matches)
            print("This shouldn't happen!")

        # return from existing data if we can
        if matches:
            return matches[0]

        team_endpoint = f"{self.endpoint}/{id}"

        return fetch_json(endpoint=team_endpoint)
