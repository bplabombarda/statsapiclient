"""Utility functions used across modules."""
from datetime import datetime

from requests import HTTPError, get

from statsapiclient.constants import (
    API_HOST,
    NHL_HOST,
    HEADERS,
    SCHEDULE_DATE_FORMAT,
)


def create_request(url, params={}):
    """Generic request function.

    Parameters
    ----------
    url : str
        The URL to which the request will be sent.
    params : dict
        Query parameters in dict form.

    Returns
    -------
    response : obj
        Response object.

    Raises
    ------
    HTTPError: if requests does not return 200.`
    """
    try:
        response = get(url, params=params, headers=dict(HEADERS))
        response.raise_for_status()

        return response
    except HTTPError:
        raise HTTPError


def fetch_html(endpoint, params=None):
    """Helper function to fetch JSON data.

    Parameters
    ----------
    endpoint : str
        The target resource endpoint.
    params : dict
        Query parameters in dict form.

    Returns
    -------
    html : str
        Web page text source at reqeusted URL.

    Raises
    ------
    HTTPError: if requests does not return 200.`
    """
    try:
        url = f"{NHL_HOST}/{endpoint}"
        response = create_request(url, params)

        return response.text
    except HTTPError:
        raise HTTPError


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
        url = f"{API_HOST}/{endpoint}"
        response = create_request(url, params)

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
