# !/usr/bin/env python3

from smashing_download import cli
from smashing_download import logger
from smashing_download import loader
import logging





def main():

    args = cli.get_parser().parse_args()

    output = args.output
    res = args.res
    level = args.verbosity

    #todo: Разобрать с logger.NONE -> кажется какая-то херня

    logger.setup(level)
    logging.debug(
        'The program was called with arguments: {}'.format(args),
    )
    try:
        path_to_wallpapers = loader.download(res, output)
    except:
        pass
    else:
        print('Wallpaper download completed successfully')
        


if __name__ == '__main__':
    main()

