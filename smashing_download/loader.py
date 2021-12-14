"""The module downloads wallpaper for the desktop to the specified directory."""

import datetime
from pathlib import Path
from typing import Callable, Iterator

from smashing_download import parser, scrape

NAME_DIR = 'wallpaper-calendar-{0}-{1}'
ENCODING = 'utf-8'
WRITE_MODE = 'wb'


def make_directory(path_to_save: Path) -> None:
    """Create a directory."""
    path_to_save.mkdir(parents=True, exist_ok=True)


def store(path_to_save: Path, actual_data: bytes) -> None:
    """Write data along the specified path."""
    with open(path_to_save, mode=WRITE_MODE, encoding=ENCODING) as the_out:
        the_out.write(actual_data)


def _compose(function1, function2):  # type: ignore
    def inner(url: str, resolution: str):  # type: ignore
        return function1(function2(url), resolution)
    return inner


def get_image_hrefs(
    url: str,
    resolution: str,
) -> Callable[[str, str], Iterator[str]]:
    return _compose(parser.get_image_hrefs, scrape.get_content)(url, resolution)


def download(
    resolution: str,
    actual_date: datetime.date,
    path_to_save: Path,
) -> Path:
    """Download and save resuource in directory."""
    url = parser.urlunparse(actual_date)
    image_hrefs = get_image_hrefs(url, resolution)
    print(image_hrefs)
    return path_to_save
