# todo_cli
CLI to-do manager that allows for tagging, prioritization, pomodoro timers, and more. 

# TODO
- [x] Move config to a yaml file in .config/todo-cli
- [x] If db doesn't exist, create the database in the proper schema
- [x] When adding a new task, if nothing entered for due date, set it to today
- [x] Implement a way to complete multiple tasks at once
- [x] Integrate a pomodoro timer
- [x] Improve pomodoro timer functionality
- [x] Add a way to modify tasks (due_date, priority, etc)
- [x] Add a way to remove tasks
- [x] Add a way to add tags to tasks
- [ ] Add a way to remove tags from tasks
- [ ] Add a way to list all distinct tags
- [ ] Clean up the quereies in actionManager; find a more organized way of doing this
- [ ] Add a way to make tasks recurring (day, week, month, etc.)

# Configuration
Add a file `config.yaml` in `.config/todo-cli` with the following contents:
```
config:
    # specify relative path to todo file from $HOME; do not include ~ in path
    todo_file_path: PATH_TO_MARKDOWN_FILE
    db_file_path: PATH_TO_SQLITE_FILE
```

# Features

## New!
Pomodoro timer:
1. `-s` option starts a 25 minute pomodoro timer for the specified task
    - TODO: stop/pause/resume functionality
    - TODO: track number of pomodoros completed per task
    - TODO: allow custom pomodoro length

## Existing
1. `-a` option adds a new task
2. `-c` option completes a task
    - Allows for multiple tasks to be completed at once
3. `-l` lists all uncompleted tasks
4. `-r` removes a task

    
