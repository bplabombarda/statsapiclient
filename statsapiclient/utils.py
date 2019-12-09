"""Utility functions used across modules."""

from requests import HTTPError, get

from .constants import API_HOST, HEADERS


def fetch_json(endpoint, params=None):
    """
    Helper method for json fetching.
    Args:
        endpoint (str): resource endpoint
        params (dict): query parameters
    Raises:
        HTTPError: if requests does not return 200
    Returns:
        json: json object for selected API call
    """
    try:
        headers = dict(HEADERS)
        response = get(
            f"{API_HOST}/{endpoint}",
            params=params, headers=headers
        )
        response.raise_for_status()

        return response.json()
    except HTTPError as error:
        raise HTTPError(f"Error fetching data: {error}")
