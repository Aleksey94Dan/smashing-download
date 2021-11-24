"""Basic logging setup."""

import logging
from typing import Optional


# __all__ = ['NONE', 'DEBUG', 'INFO', 'ERROR']


NONE = 'none'
DEBUG = 'debug'
INFO = 'info'
ERROR = 'error'



def setup(level: Optional[str]):
    """Configure a basic logger."""
    if level == INFO:
        log_level = logging.INFO
    elif level == DEBUG:
        log_level = logging.DEBUG
    elif level == ERROR:
        log_level = logging.ERROR
    else:
        log_level = logging.CRITICAL

    logger = logging.getLogger()
    logger.setLevel(log_level)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    )
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

