"""Extract images for the desktop."""
import argparse
import datetime
from pathlib import Path

from smashing_download import logger


def get_dir_path(path_to_save: str) -> Path:  # pragma: no cover
    """Get the directory entered by the user."""
    path = Path(path_to_save)
    if not path.is_dir():
        raise argparse.ArgumentTypeError(
            '{0} is not valid path'.format(path),
        )
    return path


def get_date(actual_date: str) -> datetime.date:  # pragma: no cover
    """Get the date entered by the user."""
    if len(actual_date.split('-')) < 2:
        raise argparse.ArgumentTypeError(
            '{0} is not valid format date'.format(actual_date),
        )
    actual_date = '{0}-01'.format(actual_date)
    return datetime.date.fromisoformat(actual_date)


def get_resolution(actual_res: str) -> str:  # pragma: no cover
    """Get the screen resolution entered by the user."""
    res = actual_res.split('x')
    if len(res) < 2:
        raise argparse.ArgumentTypeError(
            '{0} is not valid resolution'.format(''.join(res)),
        )
    return 'x'.join(res)


def get_parser() -> argparse.ArgumentParser:  # pragma: no cover
    """Parser comand line arguments."""
    parser = argparse.ArgumentParser(
        prog='smashing-download',
        description='CLI utility for downloading wallpaper from mashing site.',
    )
    parser.add_argument(
        'res',
        type=get_resolution,
        help='Screen resolution, 1920x1080.',
    )
    parser.add_argument(
        '-d',
        '--date',
        type=get_date,
        default=datetime.date.today(),
        help='Year and month for download.',
    )
    parser.add_argument(
        '-o',
        '--output',
        type=get_dir_path,
        default=Path.cwd(),
        help='The directory where to save files',
    )
    parser.add_argument(
        '-v',
        '--verbosity',
        type=str,
        default=logger.NONE,
        choices=[
            logger.DEBUG,
            logger.INFO,
            logger.ERROR,
        ],
        help='Enable verbosity mode.',
    )
    return parser
