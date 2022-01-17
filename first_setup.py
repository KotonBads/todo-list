#!/usr/bin/env python3

import os
import json

if __name__ == '__main__':
    if not os.path.exists('todo.json'):
        os.mknod('todo.json')

    with open('todo.json', 'w') as f:
        json.dump([], f)