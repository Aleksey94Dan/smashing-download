"""The module sends HTTP requests to the content."""

from typing import Union

import requests
from requests.exceptions import ConnectionError
from smashing_download import errors


def get_content(url: str) -> Union[str, bytes]:
    """Pull page content."""
    try:
        response = requests.get(url)
    except ConnectionError as err1:
        raise errors.DownloadNetworkError(
            'An error occurred connecting to {0}'.format(url),
        ) from err1
    return response.text if response.encoding else response.content
