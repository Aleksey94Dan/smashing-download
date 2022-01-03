[![Maintainability](https://api.codeclimate.com/v1/badges/e1a64d12d2ef22070d46/maintainability)](https://codeclimate.com/github/Aleksey94Dan/smashing-download/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/e1a64d12d2ef22070d46/test_coverage)](https://codeclimate.com/github/Aleksey94Dan/smashing-download/test_coverage)


# Description
Console utility for downloading desktop wallpaper from the resource [https://www.smashingmagazine.com/](https://www.smashingmagazine.com/).

# Requirements

You must have python version 3.10 installed. or higher.
Also you must have pip installed - The Python Package Installer.

# Installation

Install from pip with:

```
$ pip install --upgrade -i https://test.pypi.org/simple/ smashing-download --extra-index-url https://pypi.org/simple

```


# Help

    usage: smashing-download [-h] [-d DATE] [-o OUTPUT] [-v {debug,info,error}] res

    CLI utility for downloading wallpaper from mashing site.

    positional arguments:
      res                   Screen resolution, 1920x1080.

    options:
      -h, --help            show this help message and exit
      -d DATE, --date DATE  Year and month for download.
      -o OUTPUT, --output OUTPUT
                            The directory where to save files
      -v {debug,info,error}, --verbosity {debug,info,error}
                            Enable verbosity mode.


# Application call example
## Download to current directory

    smashing-loader 320x480

## Download to designated directory

    smashing-loader 320x480 -o ~/example/

## Download with verbose output

    smashing-loader 320x480 -o ~/example/ -v debug
