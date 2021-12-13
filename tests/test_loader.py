"""Testing download."""

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
            '2021-01-01',
            '2557x1440',
            (
                'https://www.smashingmagazine.com/2020/12/'
                'desktop-wallpaper-calendars-january-2021/'
            ),
        ),
        (
            '2021-11-01',
            '2559x1440',
            (
                'https://www.smashingmagazine.com/2021/10/'
                'desktop-wallpaper-calendars-november-2021/'
            ),
        ),
        (
            '2021-12-01',
            '1439x900',
            (
                'https://www.smashingmagazine.com/2021/11/'
                'desktop-wallpaper-calendars-december-2021/'
            ),
        ),
    ],
)
def test_loader(
    desired_date,
    resolution,
    url,
    image,
    requests_mock,
):
    """Test download and save page."""
    with TemporaryDirectory() as path_to_save:
        path_to_save = Path(path_to_save)
        requests_mock.get(url, content=image)
        output = loader.download(resolution, desired_date, path_to_save)
        path_to_image = [
            image_path
            for image_path in output.iterdir()
            if image_path.is_file()
        ][0]

        assert len(list(output.iterdir())) == 1

        with open(path_to_image) as actual_image:
            assert image == actual_image.read()
