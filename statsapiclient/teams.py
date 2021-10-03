"""This class allows retrieval of active teams by conference,
division, or all active teams."""

from .utils import HTTPError, fetch_json


class Team:
    """Lists of NHL teams by conference or division.
    """

    endpoint = "api/v1/teams"

    def __init__(self):
        self.data = []

        for team_id in (list(range(0, 110)) + [5524, 5814, 5844, 7202, 7460, 7461]):
            try:
                res = fetch_json(f"{self.endpoint}/{team_id}")
                teams = res.get("teams", ())
            except HTTPError:
                continue

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

    def get_by_id(self, team_id):
        """Gets team object by given id.

        Args:
            team_id (int): the team id

        Returns:
            dict: the team dict
        """

        matches = list(filter(lambda t: t["id"] == team_id, self.data))

        # return from existing data if we can
        if matches:
            return matches[0]

        team_endpoint = f"{self.endpoint}/{team_id}"

        return fetch_json(endpoint=team_endpoint)
