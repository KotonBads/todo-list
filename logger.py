import time
import os

def log(log: str):
    if not os.path.exists('logs/'):
        os.mkdir('logs/')

    if not os.path.exists(f'logs/{time.strftime("%Y-%m-%d")}.txt'):
        os.mknod(f'logs/{time.strftime("%Y-%m-%d")}.txt')

    with open(f'logs/{time.strftime("%Y-%m-%d")}.txt', 'a') as f:
        f.write(f'{time.strftime("%H:%M:%S")} {log}\n')