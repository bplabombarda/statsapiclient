"""Utility functions used across modules."""

from requests import HTTPError, get

from statsapiclient.constants import API_HOST, HEADERS


def fetch_json(endpoint, params=None):
    """Helper function to fetch JSON data.

    Parameters
    ----------
    endpoint : str
        The target resource endpoint.
    params : dict
        Query parameters in dict form.

    Returns
    -------
    json : dict
        Payload for selected API call.

    Raises
    ------
    HTTPError: if requests does not return 200.`
    """
    try:
        headers = dict(HEADERS)
        response = get(
            f"{API_HOST}/{endpoint}",
            params=params,
            headers=headers)
        response.raise_for_status()

        return response.json()
    except HTTPError:
        raise HTTPError
