"""Testing scrape."""

import pytest
from requests.exceptions import ConnectionError
from smashing_download import errors, scrape


def test_get_text(html, base_url, requests_mock):
    """Test request."""
    requests_mock.get(base_url, text=html)

    actual_content = scrape.get_content(base_url)  # act

    assert html == actual_content


def test_get_content(image, image_url, requests_mock):
    """Test request."""
    requests_mock.get(image_url, content=image)

    actual_content = scrape.get_content(image_url)  # act

    assert image == actual_content


@pytest.mark.parametrize(
    'code', [404],
)
def test_bad_response(code, requests_mock):
    """Test response 404."""
    url = 'https://status_code/{0}'.format(code)
    requests_mock.get(url, status_code=code)
    with pytest.raises(errors.DownloadError):  # noqa: AAA03
        scrape.get_content(url)


@pytest.mark.parametrize(
    'err', [errors.DownloadNetworkError],
)
def test_bad_connection(err, requests_mock):
    """Test connection error."""
    url = 'https://connection/error'
    requests_mock.get(url, exc=ConnectionError)

    with pytest.raises(err):  # noqa: AAA03
        scrape.get_content(url)
