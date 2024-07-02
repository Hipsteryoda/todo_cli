# todo_cli
cli interface for managing tasks in central Obsidian file

# TODO
- [x] Move config to a yaml file in .config/todo-cli
- [x] If db doesn't exist, create the database in the proper schema
- [ ] When adding a new task, if nothing entered for due date, set it to today
- [ ] Implement a way to complete multiple tasks at once
- [ ] Integrate a pomodoro timer
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
