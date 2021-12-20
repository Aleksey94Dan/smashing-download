"""Testing download."""

from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest
from smashing_download import loader


@pytest.mark.parametrize(  # noqa: WPS317, AAA01
    (
        'desired_date', 'resolution', 'url',
    ),
    [
        (
            date.fromisoformat('2021-02-01'),
            '320x480',
            (
                'https://www.smashingmagazine.com/2021/01/'
                'desktop-wallpaper-calendars-february-2021/'
            ),
        ),
    ],
)
def test_loader(  # noqa: WPS211, WPS210
    desired_date,
    resolution,
    url,
    html,
    expected_hrefs,
    image,
    requests_mock,
):
    """Test download and save page."""
    with TemporaryDirectory() as path_to_save:
        path_to_save = Path(path_to_save)
        requests_mock.get(url, text=html)
        for href in expected_hrefs:
            requests_mock.get(href, content=image)
        output = loader.download(
            resolution=resolution,
            actual_date=desired_date,
            path_to_save=path_to_save,
        )
        path_to_images = list(output.iterdir())

        assert len(path_to_images) == len(expected_hrefs)

        for path_to_image in path_to_images:
            with open(path_to_image, 'rb') as actual_image:
                assert image == actual_image.read()
