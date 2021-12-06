
"""Testing scrape."""

from smashing_download import scrape


def test_get_content(html, base_url, requests_mock):
    """Test request."""
    requests_mock.get(base_url, text=html)

    actual_content = scrape.get_content(base_url)  # act

    assert html == actual_content
