#!/usr/bin/python3

import argparse
from config import TODO_FILE_PATH

# TODO:
# Add task function
# Allow for flexible tagging (e.g. -f <tag> <value>; -f due 2024-06-10)

def add(task):
    with open(TODO_FILE_PATH, 'a') as file:
        file.write("\n- [ ] " + task)
        file.close()

try:
    parser = argparse.ArgumentParser(description = "Manages tasks in todo.md")
    parser.add_argument("-a", "--add", help = "Add task")
    args = parser.parse_args()

    if args.add:
        add(args.add)

except Exception as e:
    print(e)
