"""
Colors text
"""
def red(string: str, bold: bool = False):
    return f'\033[1;31m{string}\033[0m' if bold else f'\033[31m{string}\033[0m'

def green(string: str, bold: bool = False):
    return f'\033[1;32m{string}\033[0m' if bold else f'\033[32m{string}\033[0m'

def yellow(string: str, bold: bool = False):
    return f'\033[1;33m{string}\033[0m' if bold else f'\033[33m{string}\033[0m'

def blue(string: str, bold: bool = False):
    return f'\033[1;34m{string}\033[0m' if bold else f'\033[34m{string}\033[0m'

def purple(string: str, bold: bool = False):
    return f'\033[1;35m{string}\033[0m' if bold else f'\033[35m{string}\033[0m'

def cyan(string: str, bold: bool = False):
    return f'\033[1;36m{string}\033[0m' if bold else f'\033[36m{string}\033[0m'

def white(string: str, bold: bool = False):
    return f'\033[1;37m{string}\033[0m' if bold else f'\033[37m{string}\033[0m'