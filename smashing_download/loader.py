"""The module downloads wallpaper for the desktop to the specified directory."""

import datetime
from functools import partial
from multiprocessing import Pool
from pathlib import Path
from typing import Callable, Iterator

from progress.bar import ShadyBar
from smashing_download import parser, scrape

NAME_DIR = 'wallpaper-calendar-{0}-{1}'
DOWNLOAD = 'Download'
WORKERS = 5


def make_directory(path_to_save: Path) -> None:
    """Create a directory."""
    path_to_save.mkdir(parents=True, exist_ok=True)


def store(path_to_save: Path, actual_data: bytes) -> None:  # pragma: no cover
    """Write data along the specified path."""
    with open(path_to_save, mode='wb') as the_out:
        the_out.write(actual_data)


def _compose(function1, function2):  # type: ignore
    def inner(url: str, resolution: str):  # type: ignore
        return function1(function2(url), resolution)
    return inner


def get_image_hrefs(
    url: str,
    resolution: str,
) -> Callable[[str, str], Iterator[str]]:
    """Get links to pictures."""
    return _compose(parser.get_image_hrefs, scrape.get_content)(url, resolution)


def _pull(image_href: str, path_to_dir: Path) -> None:  # pragma: no cover
    image_name = parser.get_name_hrefs(image_href)
    path_to_image = path_to_dir / image_name
    image = scrape.get_content(image_href)
    if isinstance(image, bytes):
        store(path_to_image, image)


def download(  # noqa: WPS210
    resolution: str,
    actual_date: datetime.date,
    path_to_save: Path,
) -> Path:
    """Download and save resuource in directory."""
    url = parser.urlunparse(actual_date)
    image_hrefs = list(get_image_hrefs(url, resolution))  # type: ignore
    name_dir = Path(
        NAME_DIR.format(actual_date.year, actual_date.month),
    ) / resolution
    path_to_dir = path_to_save / name_dir
    make_directory(path_to_dir)
    pull = partial(_pull, path_to_dir=path_to_dir)
    pg_bar = ShadyBar(DOWNLOAD, max=len(image_hrefs))

    with Pool(WORKERS) as pool:
        for _ in pg_bar.iter(pool.imap_unordered(pull, image_hrefs)):
            pass
    return path_to_dir
