"""The module handles errors."""


class DownloadError(Exception):
    """Exception due to download errors."""

    def __init__(self, message):  # type: ignore
        """Initialize message of download error."""
        self.message = message


class DownloadNetworkError(DownloadError):
    """Connection error exception."""

    def __init__(self, message):  # type: ignore
        """Initialize message of connection error."""
        self.message = message
