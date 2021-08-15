"""This class allows retrieval of franchises."""

from .utils import fetch_json


class Franchise:
    """Lists of NHL franchises.
    """

    endpoint = "api/v1/franchises"

    def __init__(self):
        json = fetch_json(endpoint=self.endpoint)
        self.data = json["franchises"]

    def get_all(self):
        """Returns a list of all franchises.

        Returns:
            list: all franchises
        """
        return self.data

    def get_by_id(self, franchise_id):
        """Gets franchise object by given id.

        Args:
            franchise_id (int): the franchise id

        Returns:
            dict: the franchise dict
        """

        matches = list(filter(lambda f: f["franchiseId"] == franchise_id, self.data))

        # return from existing data if we can
        if matches:
            return matches[0]

        franchise_endpoint = f"{self.endpoint}/{franchise_id}"

        return fetch_json(endpoint=franchise_endpoint)
