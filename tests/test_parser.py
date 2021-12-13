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
def test_parse_url(desired_date, expected_url):
    """Test url."""
    actual_url = parser.urlunparse(desired_date)  # act

    assert expected_url == actual_url
