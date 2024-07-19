#!/usr/bin/python3

import argparse
from actionManager import actionManager

try:
    parser = argparse.ArgumentParser(description = "Manages tasks in todo.md")
    parser.add_argument("-a", "--add", metavar='TASK', help="Add task")
    parser.add_argument("-c", "--complete", nargs=argparse.REMAINDER, type=int, metavar="LINE_NUMBER", help="Complete task at linenumber IDX")
    parser.add_argument("-l", "--list", action='store_true', help="List tasks")
    parser.add_argument("-lt", "--list_with_tag", nargs="?", default="-", help="List tasks")
    parser.add_argument("-rt", "--remove_tag", nargs=argparse.REMAINDER, metavar="TAG", help="Remove tag")
    parser.add_argument("-m", "--modify", type=int, metavar="LINE_NUMBER", help="Modify task at linenumber IDX")
    parser.add_argument("-r", "--remove", nargs=argparse.REMAINDER, type=int, metavar="LINE_NUMBER", help="Remove line at linenumber IDX")
    parser.add_argument("-s", "--start", help="Start work on a task")
    parser.add_argument("-t", "--tag", nargs=argparse.REMAINDER, help="<IDX> <TAG> Adds a tag with a value to a given line number")
    args = parser.parse_args()

    if args.add:
        actionManager.add(args.add)
    elif args.complete:
        actionManager.complete(args.complete)
    elif args.list:
        actionManager.list()
    elif args.list_with_tag != "-":
        actionManager.list_with_tag(args.list_with_tag)
    elif args.remove_tag:
        actionManager.remove_tag(args.remove_tag[0], args.remove_tag[1])
    elif args.modify:
        actionManager.modify(args.modify)
    elif args.remove:
        actionManager.remove(args.remove)
    elif args.tag:
        actionManager.tag(args.tag[0], args.tag[1])
    elif args.start:
        actionManager.start_task(args.start)
except Exception as e:
    print(e)
