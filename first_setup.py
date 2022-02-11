#!/usr/bin/env python3

import os
import json


def main():
    try:
        os.system("pip3 install click")
    except:
        os.system("pip install click")

    if not os.path.exists("todo.json"):
        os.mknod("todo.json")

    with open("todo.json", "w") as f:
        json.dump([], f)


if __name__ == "__main__":
    main()
