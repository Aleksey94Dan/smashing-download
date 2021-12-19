import datetime
import os.path  # noqa: WPS301
from typing import Iterator
from urllib.parse import urlparse

from bs4 import BeautifulSoup, SoupStrainer

TEMPLATE_URL = (
    'https://www.smashingmagazine.com/{0}/{1}/'
    'desktop-wallpaper-calendars-{2}-{3}/'
)
PARSER = 'lxml'
IMAGE_TAG = 'a'
ONLY_A_TAGS = SoupStrainer(IMAGE_TAG)


def urlunparse(actual_date: datetime.date) -> str:
    """Collect url string from date."""
    actual_date = actual_date.replace(day=1)
    z_date = actual_date - datetime.timedelta(days=1)
    z_year = z_date.year
    z_month = z_date.strftime('%m')
    month_full_name = actual_date.strftime('%B').lower()
    return TEMPLATE_URL.format(
        z_year, z_month, month_full_name, actual_date.year,
    )


def _get_soup(html: str) -> BeautifulSoup:
    """Prepare the page for parsing."""
    return BeautifulSoup(
        markup=html,
        features=PARSER,
        parse_only=ONLY_A_TAGS,
    )


def _get_image_hrefs(soup: BeautifulSoup, resolution: str) -> Iterator[str]:
    """Get a list of links to images."""
    return (
        href['href'] for href in soup.find_all(IMAGE_TAG, text=resolution)
    )


def get_image_hrefs(html: str, resolution: str) -> Iterator[str]:
    """Get url for image."""
    return _get_image_hrefs(_get_soup(html), resolution)


def get_name_hrefs(image_href: str) -> str:
    """Get name for image."""
    path_from_url = urlparse(image_href).path
    _, name_image = os.path.split(path_from_url)
    return name_image
