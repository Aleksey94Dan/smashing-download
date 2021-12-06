"""The module sends HTTP requests to the content."""


from functools import partial
from typing import Union

import requests

ses = requests.Session()


def _get_content(url: str, session: requests.Session) -> Union[str, bytes]:
    """Pull page content."""
    response = session.get(url)
    return response.text if response.encoding else response.content


get_content = partial(_get_content, session=ses)
