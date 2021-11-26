"""The module downloads wallpaper for the desktop to the specified directory."""

from pathlib import Path

TEMPLATE_URL = (
    'https://www.smashingmagazine.com/{0}/{1}/'
    'desktop-wallpaper-calendars-{2}-{3}/'
)


def download(resolution: str, path_to_save: Path) -> Path:
    """Download and save resuource in directory."""
    return Path('pass')
