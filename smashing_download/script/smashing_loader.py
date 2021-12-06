# !/usr/bin/env python3

import logging
import sys

from smashing_download import cli, loader, logger

EXIT_SUCCES = 0
EXIT_FAILURE = 1


def main() -> None:

    args = cli.get_parser().parse_args()

    logger.setup(args.verbosity)
    logging.debug(
        'The program was called with arguments: {0}'.format(args),
    )
    exit_code = EXIT_FAILURE
    path_to_wallpapers = loader.download(args.res, args.date, args.output)
    print(path_to_wallpapers)
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
