#!/usr/bin/env python3

import os
import json

if __name__ == '__main__':
    try:
        os.system('pip install click')
    except:
        os.system('pip3 install click')

    if not os.path.exists('todo.json'):
        os.mknod('todo.json')

    with open('todo.json', 'w') as f:
        json.dump([], f)