"""The module sends HTTP requests to the content."""

from typing import Union

import requests
from requests.exceptions import ConnectionError, HTTPError
from smashing_download import errors


def get_content(url: str) -> Union[str, bytes]:
    """Pull page content."""
    try:  # noqa: WPS229
        response = requests.get(url)
        response.raise_for_status()
    except ConnectionError as err1:
        raise errors.DownloadNetworkError(
            'An error occurred connecting to {0}'.format(url),
        ) from err1
    except HTTPError as err2:
        raise errors.DownloadError(
            'The requested information was not found.',
        ) from err2
    return response.text if response.encoding else response.content
