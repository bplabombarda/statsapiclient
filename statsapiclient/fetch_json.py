from datetime import datetime

from requests import get


TODAY = datetime.today()
BASE_URL = "https://statsapi.web.nhl.com/{endpoint}"
HEADERS = {
    "user-agent": (
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
    ),
    "Dnt": ("1"),
    "Accept-Language": ("en"),
    "origin": ("https://statsapi.web.nhl.com"),
    "referer": ("https://www.nhl.com/"),
}


def fetch_json(endpoint, params):
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
    h = dict(HEADERS)
    fetch = get(BASE_URL.format(endpoint=endpoint), params=params, headers=h)

    fetch.raise_for_status()
    return fetch.json()
