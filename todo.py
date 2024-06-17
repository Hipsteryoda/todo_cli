#!/usr/bin/python3

import argparse
import actionManager 

try:
    parser = argparse.ArgumentParser(description = "Manages tasks in todo.md")
    parser.add_argument("-a", "--add", metavar='TASK', help="Add task")
    parser.add_argument("-c", "--complete", type=int, metavar="LINE_NUMBER", help="Complete task at linenumber IDX")
    parser.add_argument("-l", "--list", action='store_true', help="List tasks")
    parser.add_argument("-r", "--remove", type=int, metavar="LINE_NUMBER", help="Remove line at linenumber IDX")
    parser.add_argument("-t", "--tag", metavar="<KEY> <VALUE>", nargs=3, help="Adds a tag with a value to a given line number")
    args = parser.parse_args()

    if args.add:
        actionManager.add(args.add)
    elif args.list:
        actionManager.list()
    elif args.remove:
        actionManager.remove(args.remove)
    elif args.complete:
        actionManager.complete(args.complete)
    elif args.tag:
        actionManager.tag(int(args.tag[0]), args.tag[1], args.tag[2])
        # print(args.tag)

except Exception as e:
    print(e)
