"""The module downloads wallpaper for the desktop to the specified directory."""

import datetime
from pathlib import Path

TEMPLATE_URL = (
    'https://www.smashingmagazine.com/{0}/{1}/'
    'desktop-wallpaper-calendars-{2}-{0}/'
)
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


def download(
    resolution: str,
    actual_date: datetime.date,
    path_to_save: Path,
) -> Path:
    """Download and save resuource in directory."""
    year = actual_date.year
    month = actual_date.strftime('%m')
    month_full_name = actual_date.strftime('%B')
    url = TEMPLATE_URL.format(year, month, month_full_name.lower())
    print(url)


    print(resolution)  # noqa: E303
    print(actual_date)  # noqa: E303
    print(path_to_save)  # noqa: E303

    return Path('pass')
