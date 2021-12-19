from datetime import date

import pytest
from smashing_download import parser


@pytest.mark.parametrize(  # noqa: WPS317
    (
        'desired_date', 'expected_url',
    ),
    [
        (
            date.fromisoformat('2021-01-01'),
            (
                'https://www.smashingmagazine.com/2020/12/'
                'desktop-wallpaper-calendars-january-2021/'
            ),
        ),
        (
            date.fromisoformat('2021-02-01'),
            (
                'https://www.smashingmagazine.com/2021/01/'
                'desktop-wallpaper-calendars-february-2021/'
            ),
        ),
        (
            date.fromisoformat('2021-03-01'),
            (
                'https://www.smashingmagazine.com/2021/02/'
                'desktop-wallpaper-calendars-march-2021/'
            ),
        ),
        (
            date.fromisoformat('2021-04-01'),
            (
                'https://www.smashingmagazine.com/2021/03/'
                'desktop-wallpaper-calendars-april-2021/'
            ),
        ),
        (
            date.fromisoformat('2021-05-01'),
            (
                'https://www.smashingmagazine.com/2021/04/'
                'desktop-wallpaper-calendars-may-2021/'
            ),
        ),
        (
            date.fromisoformat('2021-06-01'),
            (
                'https://www.smashingmagazine.com/2021/05/'
                'desktop-wallpaper-calendars-june-2021/'
            ),
        ),
        (
            date.fromisoformat('2021-07-01'),
            (
                'https://www.smashingmagazine.com/2021/06/'
                'desktop-wallpaper-calendars-july-2021/'
            ),
        ),
        (
            date.fromisoformat('2021-08-01'),
            (
                'https://www.smashingmagazine.com/2021/07/'
                'desktop-wallpaper-calendars-august-2021/'
            ),
        ),
        (
            date.fromisoformat('2021-09-01'),
            (
                'https://www.smashingmagazine.com/2021/08/'
                'desktop-wallpaper-calendars-september-2021/'
            ),
        ),
        (
            date.fromisoformat('2021-10-01'),
            (
                'https://www.smashingmagazine.com/2021/09/'
                'desktop-wallpaper-calendars-october-2021/'
            ),
        ),
        (
            date.fromisoformat('2021-11-01'),
            (
                'https://www.smashingmagazine.com/2021/10/'
                'desktop-wallpaper-calendars-november-2021/'
            ),
        ),
        (
            date.fromisoformat('2021-12-01'),
            (
                'https://www.smashingmagazine.com/2021/11/'
                'desktop-wallpaper-calendars-december-2021/'
            ),
        ),
    ],
)
def test_parse_base_url(desired_date, expected_url):
    """Test url."""
    actual_url = parser.urlunparse(desired_date)  # act

    assert expected_url == actual_url


def test_get_image_hrefs(html, expected_hrefs):
    """Test get image hrefs."""
    actual_hrefs = set(parser.get_image_hrefs(html, '320x480'))  # act

    assert expected_hrefs == actual_hrefs


@pytest.mark.parametrize(  # noqa: WPS317
    (
        'hrefs', 'expected_image_name',
    ),
    [
        (
            (
                'http://files.smashingmagazine.com/wallpapers/nov-21/'
                'no-shave-november/nocal/nov-21-no-shave-november-nocal'
                '-640x480.jpg?_ga=2.14374199.1677587011.1639791961-12104'
                '54835.1632544118'
            ),
            'nov-21-no-shave-november-nocal-640x480.jpg',
        ),
        (
            (
                'http://files.smashingmagazine.com/wallpapers/nov-21/'
                'winter-is-here/nocal/nov-21-winter-is-here-nocal-192'
                '0x1200.png?_ga=2.257169675.1677587011.1639791961-121'
                '0454835.1632544118'
            ),
            'nov-21-winter-is-here-nocal-1920x1200.png',
        ),
    ],
)
def test_get_name_hrefs(hrefs, expected_image_name):
    """Test get name from hrefs."""
    actual_image_name = parser.get_name_hrefs(hrefs)  # act

    assert expected_image_name == actual_image_name
