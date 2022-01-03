# !/usr/bin/env python3

import logging

from smashing_download import cli, errors, loader, logger

EXIT_SUCCES = 0
EXIT_FAILURE = 1


def main() -> int:  # pragma: no cover

    args = cli.get_parser().parse_args()

    logger.setup(args.verbosity)
    logging.debug(
        'The program was called with arguments: {0}'.format(args),
    )
    exit_code = EXIT_FAILURE
    try:
        path_to_wallpapers = loader.download(args.res, args.date, args.output)
    except errors.DownloadNetworkError as err1:
        logging.debug(str(err1.__cause__), exc_info=True)  # noqa: WPS609
        logging.error(err1.message)
    except errors.DownloadError as err2:
        logging.debug(str(err2.__cause__), exc_info=True)  # noqa: WPS609
        logging.error(err2.message)
    else:
        exit_code = EXIT_SUCCES
        print(  # noqa: WPS421
            'Wallpaper loading completed successfully to {0}'.format(
                path_to_wallpapers,
            ),
        )
    return exit_code


if __name__ == '__main__':
    exit(main())
