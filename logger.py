"""
Simple Logging system for Python.

- `logger.log(log, opt: path, opt: log_format)` - meant to be used for loggin info to the log file.
- `logger.warning(log, opt: path, opt: log_format)` - meant to be used for logging any warnings to the log file.
- `logger.error(log, opt: path, opt: log_format)` - meant to be used for logging any errors to the log file.
- `logger.debug(log, opt:path, opt: log_format)` - meant to be used for logging any debug info to the log file.
- `logger.mkfile(opt: path, opt: log_format)` - meant to be used to create the log file if it doesn't exist.

Example Usage:
```python
import logger

def foo(x):
    ...

try:
    foo(x)
except Exception as e:
    logger.error(e)
"""

import time
import os

def mkfile(path: str = 'logs', log_format: str = '%Y-%m-%d'):
    """
    Creates the log directory and the log file if it doesn't exist.
    """
    if not os.path.exists(path):
        os.mkdir(path)

    if not os.path.exists(f'{path}/{time.strftime(log_format)}.txt'):
        os.mknod(f'{path}/{time.strftime(log_format)}.txt')

def log(log: str, path: str = 'logs', log_format: str = '%Y-%m-%d'):
    """
    Use this function to show LOG information.
    """
    mkfile(path)

    with open(f'{path}/{time.strftime(log_format)}.txt', 'a') as f:
        f.write(f'{time.strftime("LOG %H:%M:%S")} {log}\n')

def warning(log: str, path: str = 'logs', log_format: str = '%Y-%m-%d'):
    """
    Use this function to show WARNING information.
    """
    mkfile(path)

    with open(f'{path}/{time.strftime(log_format)}.txt', 'a') as f:
        f.write(f'{time.strftime("WARNING %H:%M:%S")} {log}\n')

def error(log: str, path: str = 'logs'):
    """
    Use this function to show ERROR information.
    """
    mkfile(path)

    with open(f'{path}/{time.strftime("%Y-%m-%d")}.txt', 'a') as f:
        f.write(f'{time.strftime("ERROR %H:%M:%S")} {log}\n')

def debug(log: str, path: str = 'logs', log_format: str = '%Y-%m-%d'):
    """
    Use this function to show DEBUG information.
    """
    mkfile(path)

    with open(f'{path}/{time.strftime(log_format)}.txt', 'a') as f:
        f.write(f'{time.strftime("DEBUG %H:%M:%S")} {log}\n')