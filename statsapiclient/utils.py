"""Utility functions used across modules."""
from datetime import datetime

from requests import HTTPError, get

from statsapiclient.constants import (
    API_HOST,
    HEADERS,
    SCHEDULE_DATE_FORMAT,
)


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


def validate_date(date):
    """Validates that a date meets the specified format."""
    try:
        datetime.strptime(date, SCHEDULE_DATE_FORMAT.get('format'))
        return True
    except ValueError:
        format_display = SCHEDULE_DATE_FORMAT.get('display')

        raise ValueError(
            f"Incorrect date format, should be {format_display}")
