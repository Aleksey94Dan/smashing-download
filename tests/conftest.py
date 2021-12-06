"""Prepare fixture."""


from pathlib import Path

import pytest

FIXTURE_DIR = Path(__file__).resolve().parent / 'fixture'

BASE_HTML = FIXTURE_DIR / 'site/index.html'

BASE_URL = (
    'https://www.smashingmagazine.com/2021/10/'
    'desktop-wallpaper-calendars-november-2021/'
)


@pytest.fixture()
def html() -> str:
    """Return html file."""
    return BASE_HTML.read_text()


@pytest.fixture()
def base_url() -> str:
    """Return html file."""
    return BASE_URL
