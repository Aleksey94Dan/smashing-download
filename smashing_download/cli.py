
"""Extract images for the desktop."""
import  argparse
import os
from smashing_download import logger


def dir_path(path: str) -> str:
    if not os.path.isdir(path):
        raise argparse.ArgumentTypeError(
                '{} is not valid path'.format(path),
                )
    return path
    


def get_parser() -> argparse.ArgumentParser:
    """Parser comand line arguments."""
    parser = argparse.ArgumentParser(
        prog='smashing-download',
        description="CLI utility for downloading wallpaper from mashing site.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
       )
    parser.add_argument(
        '-r',
       '--res',
       type=str,
       default='1920x1080',
       help='Screen resolution, 2560x1440.'
   )
    parser.add_argument(
        '-o',
       '--output',
       type=dir_path,
       default=os.getcwd(),
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

