#!/usr/bin/python3

import argparse
from itertools import islice
from config import TODO_FILE_PATH

# TODO:
# Allow for flexible tagging (e.g. -f <tag> <value>; -f due 2024-06-10)
# Add a list option

def add(task):
    with open(TODO_FILE_PATH, 'a') as file:
        file.write("\n- [ ] " + task)
        file.close()

def list():
    with open(TODO_FILE_PATH, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line)
        file.close()

def remove(idx):
    with open(TODO_FILE_PATH, 'r+') as file:
        lines = file.readlines()
        del lines[idx]
        file.seek(0)                        # set the pointer to the 0th line
        file.truncate()                     # clear the whole file to be rewritten
        for line in lines:
            file.write(line)

try:
    parser = argparse.ArgumentParser(description = "Manages tasks in todo.md")
    parser.add_argument("-a", "--add", metavar='TASK', help="Add task")
    parser.add_argument("-l", "--list", action='store_true', help="List tasks")
    parser.add_argument("-r", "--remove", type=int, metavar="LINE_NUMBER", help="Remove line at linenumber IDX")
    args = parser.parse_args()

    if args.add:
        add(args.add)
    elif args.list:
        list()
    elif args.remove:
        remove(args.remove)

except Exception as e:
    print(e)
