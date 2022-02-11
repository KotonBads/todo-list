#!/usr/bin/env python3

import json
import time
import textwrap
from unicodedata import name
import click

import first_setup
import logger
import color


def get_todo() -> list:
    with open("todo.json") as f:
        todo = json.load(f)
    return todo


def add_todo(name: str, description: str):
    todo = get_todo()
    todo.append(
        {"name": name, "description": description, "added": time.time(), "done": False}
    )

    with open("todo.json", "w") as f:
        json.dump(todo, f)

    print(color.green("TODO added!"))
    print(f'{color.yellow("Name: ")} {color.cyan(name)}')
    print(f'{color.yellow("Description: ")} {color.cyan(description)}')

    logger.log(f"TODO: '{name}' added")


def mark_as_done(index: int):
    todo = get_todo()
    todo[index]["done"] = True

    with open("todo.json", "w") as f:
        json.dump(todo, f)

    print(color.green(f'TODO ({index}. {todo[index]["name"]}) marked as done!\n'))

    logger.log(f'TODO: \'{index} - {todo[index]["name"]}\' marked as done')


def unmark_as_done(index: int):
    todo = get_todo()
    todo[index]["done"] = False

    with open("todo.json", "w") as f:
        json.dump(todo, f)

    print(color.green(f'TODO ({index}. {todo[index]["name"]}) unmarked as done!\n'))

    logger.log(f'TODO: \'{index} - {todo[index]["name"]}\' unmarked as done')


def view_todo():
    todo = get_todo()
    for i, item in enumerate(todo):
        print(f'{color.blue(i)}. {color.yellow(item["name"])}')


def open_todo(index: int):
    todo = get_todo()
    print(f'{color.yellow("Name: ", bold = True)} {color.cyan(todo[index]["name"])}')
    print(
        f'{color.yellow("Description: ", bold = True)} {color.cyan(todo[index]["description"])}'
    )
    print(
        f'{color.yellow("Added: ", bold = True)} {color.cyan(time.ctime(todo[index]["added"]))}'
    )
    print(f'{color.green("Done: ")} {color.purple(todo[index]["done"])}')


def remove_todo(index: int):
    todo = get_todo()

    logger.log(
        f'TODO: \'{index} - {todo[index]["name"]}\' removed.\n\t\tContents: {todo[index]}'
    )

    todo.pop(index)

    with open("todo.json", "w") as f:
        json.dump(todo, f)

    print(color.green("TODO removed!\n"))


def ui(choice: str, text: str):
    if choice == "1":
        name = input(color.yellow("Enter Name: "))
        description = input(color.yellow("Enter Description: "))
        add_todo(name, description)

    elif choice == "2":
        index = int(input(color.yellow("Enter Index: ")))
        mark_as_done(index)

    elif choice == "3":
        index = int(input(color.yellow("Enter Index: ")))
        unmark_as_done(index)

    elif choice == "4":
        view_todo()

    elif choice == "5":
        index = int(input(color.yellow("Enter Index: ")))
        open_todo(index)

    elif choice == "6":
        index = int(input(color.yellow("Enter Index: ")))
        remove_todo(index)

    elif choice == "7":
        first_setup.main()

    elif choice == "h":
        print(text)

    elif choice == "c":
        click.clear()

    elif choice == "exit":
        exit()

    else:
        print(color.red("Invalid choice. Type 'h' for help.", bold=True))


def main():
    text = textwrap.dedent(
        f"""
        {color.blue('---------- TODO LIST ----------', bold = True)}
        {color.yellow('1.')} {color.cyan('Add a new TODO')}
        {color.yellow('2.')} {color.cyan('Mark a TODO as done')}
        {color.yellow('3.')} {color.cyan('Unmark a TODO as done')}
        {color.yellow('4.')} {color.cyan('View all TODOs')}
        {color.yellow('5.')} {color.cyan('Open a TODO')}
        {color.yellow('6.')} {color.cyan('Remove a TODO')}
        {color.yellow('7.')} {color.cyan('Setup / Clear TODO')}
        
        {color.purple('h')} - {color.green('Help')}
        {color.purple('c')} - {color.green('Clear screen')}
        {color.purple('exit')} - {color.green('Exit')}
        {color.blue('--------------------------------', bold = True)}
        """
    )

    print(text)

    while True:
        choice = input(color.green("Enter your choice: "))
        ui(choice, text)


if __name__ == "__main__":
    try:
        try:
            click.clear()
            main()

        except IndexError as e:
            click.clear()
            logger.warning(e)
            print(color.red("Invalid Index.", bold=True))
            raise

        except FileNotFoundError:
            click.clear()
            print(
                color.red(
                    "File 'todo.json': File not found.\nYou might want to run Setup (7)",
                    bold=True,
                )
            )
            raise

    except FileNotFoundError as e:
        logger.warning(e)
        print(color.red("Exiting...", bold=True))

    except (KeyboardInterrupt, SystemExit):
        logger.log("Exited")
        print(color.red("Exiting...", bold=True))

    except IndexError:
        main()
