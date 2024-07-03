# todo_cli
cli interface for managing tasks in central Obsidian file

# TODO
- [x] Move config to a yaml file in .config/todo-cli
- [x] If db doesn't exist, create the database in the proper schema
- [x] When adding a new task, if nothing entered for due date, set it to today
- [x] Implement a way to complete multiple tasks at once
- [x] Integrate a pomodoro timer
- [ ] Improve pomodoro timer functionality
- [ ] Add a way to modify tasks (due_date, priority, etc)
- [ ] Add a way to add tags to tasks
- [ ] Clean up the quereies in actionManager; find a more organized way of doing this

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

    
