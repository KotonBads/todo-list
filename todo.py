#!/usr/bin/env python3

import json
import platform
import os
import textwrap
import first_setup

# ANSI Escape Codes
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
white = '\033[37m'
end = '\033[0m'
bold = '\033[1m'

def get_todo() -> list:
    with open('todo.json') as f:
        todo = json.load(f)
    return todo

def add_todo(name: str, description: str):
    todo = get_todo()
    todo.append(
            {
            'name': name, 
            'description': description, 
            'done': False
            }
        )

    with open('todo.json', 'w') as f:
        json.dump(todo, f)
    
    print(f'{green}TODO added!{end}\n')

def mark_as_done(index: int):
    todo = get_todo()
    todo[index]['done'] = True

    with open('todo.json', 'w') as f:
        json.dump(todo, f)
    
    print(f'{green}TODO marked as done!{end}\n')

def view_todo():
    todo = get_todo()
    for i, item in enumerate(todo):
        print(f'{blue}{i}: {yellow}{item["name"]}{end}\n')

def open_todo(index: int):
    todo = get_todo()
    print(f'{yellow}{bold}Name:{end} {cyan}{todo[index]["name"]}{end}')
    print(f'{yellow}{bold}Description:{end} {cyan}{todo[index]["description"]}{end}')
    print(f'{green}{bold}Done:{end} {purple}{todo[index]["done"]}{end}')

def remove_todo(index: int):
    todo = get_todo()
    todo.pop(index)

    with open('todo.json', 'w') as f:
        json.dump(todo, f)
    
    print(f'{green}TODO removed!{end}\n')

def clear():
    if platform.system() == 'Windows':
        os.system('cls')

    elif platform.system() == 'Linux':
        os.system('clear')

    elif platform.system() == 'Darwin':
        os.system('clear')

    else:
        print(f'{red}Unknown OS{end}\n')

def ui(choice: str, text: str):
    if choice == '1':
        name = input(f'{yellow}Enter name: {end}')
        description = input(f'{yellow}Enter description: {end}')
        add_todo(name, description)

    elif choice == '2':
        index = int(input(f'{yellow}Enter index: {end}'))
        mark_as_done(index)

    elif choice == '3':
        view_todo()

    elif choice == '4':
        index = int(input(f'{yellow}Enter index: {end}'))
        open_todo(index)
    
    elif choice == '5':
        index = int(input(f'{yellow}Enter index: {end}'))
        remove_todo(index)

    elif choice == '6':
        exit()
    
    elif choice == '7':
        first_setup.main()

    elif choice == 'h':
        print(text)

    elif choice == 'c':
        clear()

    else:
        print(f'{red}Invalid choice. Type \'h\' for help.{end}')

def main():
    text = textwrap.dedent(\
        f"""
        {blue}{bold}---------- TODO LIST ----------{end}
        {yellow}1.{end} {cyan}Add a new TODO{end}
        {yellow}2.{end} {cyan}Mark a TODO as done{end}
        {yellow}3.{end} {cyan}View all TODOs{end}
        {yellow}4.{end} {cyan}Open a TODO{end}
        {yellow}5.{end} {cyan}Remove a TODO{end}
        {yellow}6.{end} {cyan}Exit{end}
        {yellow}7.{end} {cyan}Setup / Clear TODO{end}
        
        {purple}h{end} - {green}Help{end}
        {purple}c{end} - {green}Clear screen{end}
        {blue}{bold}--------------------------------{end}
        """
    )

    print(text)

    while True:
        choice = input(f'{green}Enter your choice: {end}')
        ui(choice, text)


if __name__ == '__main__':
    try:
        try:
            main()

        except IndexError:
            print(f'{red}{bold}Invalid index.{end}')
            raise

        except FileNotFoundError:
            print(f'{red}{bold}File \'todo.json\': File not found.{end}')
            raise
        
        else:
            main()
    
    except (FileNotFoundError, KeyboardInterrupt, SystemExit):
        print(f'{red}{bold}Exiting...{end}')
    
    except IndexError:
        main()