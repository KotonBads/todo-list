"""
Colors text
"""

from typing import Union


def red(string: Union[str, int], bold: bool = False):
    return f"\033[1;31m{string}\033[0m" if bold else f"\033[31m{string}\033[0m"


def green(string: Union[str, int], bold: bool = False):
    return f"\033[1;32m{string}\033[0m" if bold else f"\033[32m{string}\033[0m"


def yellow(string: Union[str, int], bold: bool = False):
    return f"\033[1;33m{string}\033[0m" if bold else f"\033[33m{string}\033[0m"


def blue(string: Union[str, int], bold: bool = False):
    return f"\033[1;34m{string}\033[0m" if bold else f"\033[34m{string}\033[0m"


def purple(string: Union[str, int], bold: bool = False):
    return f"\033[1;35m{string}\033[0m" if bold else f"\033[35m{string}\033[0m"


def cyan(string: Union[str, int], bold: bool = False):
    return f"\033[1;36m{string}\033[0m" if bold else f"\033[36m{string}\033[0m"


def white(string: Union[str, int], bold: bool = False):
    return f"\033[1;37m{string}\033[0m" if bold else f"\033[37m{string}\033[0m"
