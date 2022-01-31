import time
import os

def log(log: str, path: str = 'logs'):
    if not os.path.exists(path):
        os.mkdir(path)

    if not os.path.exists(f'{path}/{time.strftime("%Y-%m-%d")}.txt'):
        os.mknod(f'{path}/{time.strftime("%Y-%m-%d")}.txt')

    with open(f'{path}/{time.strftime("%Y-%m-%d")}.txt', 'a') as f:
        f.write(f'{time.strftime("%H:%M:%S")} {log}\n')