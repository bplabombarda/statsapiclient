"""Utility functions used across modules."""
from datetime import datetime

from requests import HTTPError, get

from statsapiclient.constants import (
    API_HOST,
    NHL_HOST,
    HEADERS,
    SCHEDULE_DATE_FORMAT,
)


def create_request(url, params=None):
    """Generic request function.

    Args
        url (str): The URL to which the request will be sent.
        params (dict): Query parameters in dict form.

    Returns:
        response (obj): Response object.

    Raises
        HTTPError: if requests does not return 200.
    """
    try:
        response = get(
            url=url,
            headers=dict(HEADERS),
            params=params if params else {},
        )
        response.raise_for_status()

        return response
    except HTTPError as err:
        raise HTTPError from err


def fetch_html(endpoint, params=None):
    """Helper function to fetch JSON data.

    Args:
        endpoint (str): The target resource endpoint.
        params (dict): Query parameters in dict form.

    Returns:
        html (str): Web page text source at reqeusted URL.

    Raises:
        HTTPError: if requests does not return 200.`
    """
    try:
        url = f"{NHL_HOST}/{endpoint}"
        response = create_request(url, params)

        return response.text
    except HTTPError as err:
        raise HTTPError from err


def fetch_json(endpoint, params=None):
    """Helper function to fetch JSON data.

    Args:
        endpoint (str): The target resource endpoint.
        params (dict): Query parameters in dict form.

    Returns:
        json (dict): Payload for selected API call.

    Raises:
        HTTPError: if requests does not return 200.`
    """
    try:
        url = f"{API_HOST}/{endpoint}"
        response = create_request(url, params)

        return response.json()
    except HTTPError as err:
        raise HTTPError from err


def validate_date(date):
    """Validates that a date meets the specified format.

    Args:
        date (str): A YYYY-MM-DD formatted date string.
    """
    try:
        datetime.strptime(date, SCHEDULE_DATE_FORMAT.get('format'))

        return True
    except ValueError as err:
        format_display = SCHEDULE_DATE_FORMAT.get('display')

        raise ValueError(
            f"Incorrect date format, should be {format_display}") from err
