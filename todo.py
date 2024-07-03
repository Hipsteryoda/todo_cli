#!/usr/bin/python3

import argparse
from actionManager import actionManager

try:
    parser = argparse.ArgumentParser(description = "Manages tasks in todo.md")
    parser.add_argument("-a", "--add", metavar='TASK', help="Add task")
    parser.add_argument("-c", "--complete", nargs=argparse.REMAINDER, type=int, metavar="LINE_NUMBER", help="Complete task at linenumber IDX")
    parser.add_argument("-l", "--list", action='store_true', help="List tasks")
    parser.add_argument("-m", "--modify", type=int, metavar="LINE_NUMBER", help="Modify task at linenumber IDX")
    parser.add_argument("-r", "--remove", type=int, metavar="LINE_NUMBER", help="Remove line at linenumber IDX")
    parser.add_argument("-s", "--start", help="Start work on a task")
    parser.add_argument("-t", "--tag", nargs=3, metavar="", help="<LINE> <KEY> <VALUE> Adds a tag with a value to a given line number")
    args = parser.parse_args()

    if args.add:
        due_date, priority = actionManager.collect_task_details()
        actionManager.add(args.add, due_date=due_date, priority=priority)
    elif args.list:
        actionManager.list()
    elif args.modify:
        actionManager.modify(args.modify)
    elif args.remove:
        actionManager.remove(args.remove)
    elif args.complete:
        actionManager.complete(args.complete)
    elif args.start:
        actionManager.start_task(args.start)
    elif args.tag:
        actionManager.tag(int(args.tag[0]), args.tag[1], args.tag[2])

except Exception as e:
    print(e)
