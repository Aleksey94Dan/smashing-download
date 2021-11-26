
"""Extract images for the desktop."""
import argparse
from pathlib import Path

from smashing_download import logger


def dir_path(path_to_save: str) -> Path:
    path = Path(path_to_save)
    if not path.is_dir():
        raise argparse.ArgumentTypeError(
            '{0} is not valid path'.format(path),
        )
    return path


def get_parser() -> argparse.ArgumentParser:
    """Parser comand line arguments."""
    parser = argparse.ArgumentParser(
        prog='smashing-download',
        description='CLI utility for downloading wallpaper from mashing site.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        '-r',
        '--res',
        type=str,
        default='1920x1080',
        help='Screen resolution, 2560x1440.',
    )
    parser.add_argument(
        '-o',
        '--output',
        type=dir_path,
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
