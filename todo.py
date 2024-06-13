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
try:
    parser = argparse.ArgumentParser(description = "Manages tasks in todo.md")
    parser.add_argument("-a", "--add", metavar='TASK', help = "Add task")
    parser.add_argument("-l", "--list", action='store_true', help = "List tasks")
    args = parser.parse_args()

    if args.add:
        add(args.add)
    elif args.list:
        list()

except Exception as e:
    print(e)
