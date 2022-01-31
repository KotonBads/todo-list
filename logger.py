"""
Simple Logging system for Python.
"""

import time
import os

def mkfile(path: str = 'logs'):
    """
    Creates the log directory and the log file if it doesn't exist.
    """
    if not os.path.exists(path):
        os.mkdir(path)

    if not os.path.exists(f'{path}/{time.strftime("%Y-%m-%d")}.txt'):
        os.mknod(f'{path}/{time.strftime("%Y-%m-%d")}.txt')

def log(log: str, path: str = 'logs'):
    """
    Use this function to show LOG information.
    """
    mkfile(path)

    with open(f'{path}/{time.strftime("%Y-%m-%d")}.txt', 'a') as f:
        f.write(f'{time.strftime("LOG %H:%M:%S")} {log}\n')

def warning(log: str, path: str = 'logs'):
    """
    Use this function to show WARNING information.
    """
    mkfile(path)

    with open(f'{path}/{time.strftime("%Y-%m-%d")}.txt', 'a') as f:
        f.write(f'{time.strftime("WARNING %H:%M:%S")} {log}\n')

def error(log: str, path: str = 'logs'):
    """
    Use this function to show ERROR information.
    """
    mkfile(path)

    with open(f'{path}/{time.strftime("%Y-%m-%d")}.txt', 'a') as f:
        f.write(f'{time.strftime("ERROR %H:%M:%S")} {log}\n')

def debug(log: str, path: str = 'logs'):
    """
    Use this function to show DEBUG information.
    """
    mkfile(path)

    with open(f'{path}/{time.strftime("%Y-%m-%d")}.txt', 'a') as f:
        f.write(f'{time.strftime("DEBUG %H:%M:%S")} {log}\n')