"""Utility functions used across modules."""

from requests import HTTPError, get

from statsapiclient.constants import API_HOST, HEADERS


def fetch_json(endpoint, params=None):
    """
    Helper function to fetch JSON data.
    Args:
        endpoint (str): resource endpoint
        params (dict): query parameters
    Raises:
        HTTPError: if requests does not return 200
    Returns:
        json: JSON object for selected API call.
    """
    try:
        headers = dict(HEADERS)
        response = get(f"{API_HOST}/{endpoint}", params, headers)
        response.raise_for_status()

        return response.json()
    except HTTPError:
        raise HTTPError
