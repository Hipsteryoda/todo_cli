#!/usr/bin/python3

import argparse
import actionManager 

try:
    parser = argparse.ArgumentParser(description = "Manages tasks in todo.md")
    parser.add_argument("-a", "--add", metavar='TASK', help="Add task")
    parser.add_argument("-c", "--complete", type=int, metavar="LINE_NUMBER", help="Complete task at linenumber IDX")
    parser.add_argument("-l", "--list", action='store_true', help="List tasks")
    parser.add_argument("-r", "--remove", type=int, metavar="LINE_NUMBER", help="Remove line at linenumber IDX")
    args = parser.parse_args()

    if args.add:
        actionManager.add(args.add)
    elif args.list:
        actionManager.list()
    elif args.remove:
        actionManager.remove(args.remove)
    elif args.complete:
        actionManager.complete(args.complete)

except Exception as e:
    print(e)
