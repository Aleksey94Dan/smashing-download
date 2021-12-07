"""Prepare fixture."""

from pathlib import Path

import pytest

FIXTURE_DIR = Path(__file__).resolve().parent / 'fixture'

BASE_PAGE = FIXTURE_DIR / 'site/index.html'
BASE_IMAGE = FIXTURE_DIR / 'images/nov-21-no-shave-november-cal-640x480.jpg'

BASE_URL = (
    'https://www.smashingmagazine.com/2021/10/'
    'desktop-wallpaper-calendars-november-2021/'
)
IMAGE_URL = (
    'http://files.smashingmagazine.com/'
    'wallpapers/nov-21/no-shave-november/'
    'cal/nov-21-no-shave-november-cal-320'
    'x480.jpg?_ga=2.186979051.295077633.16'
    '38885607-1210454835.1632544118'
)


@pytest.fixture()
def html() -> str:
    """Return html file."""
    return BASE_PAGE.read_text()


@pytest.fixture()
def image() -> bytes:
    """Return image file."""
    return BASE_IMAGE.read_bytes()


@pytest.fixture()
def base_url() -> str:
    """Return url of html file."""
    return BASE_URL


@pytest.fixture()
def image_url() -> str:
    """Return url of image file."""
    return IMAGE_URL
