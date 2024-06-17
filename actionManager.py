from config import TODO_FILE_PATH

def writeToFile(lines, file):
    file.seek(0)                        # set the pointer to the 0th line
    file.truncate()                     # clear the whole file to be rewritten
    for line in lines:
        file.write(line)
    file.close()

def add(task):
    with open(TODO_FILE_PATH, 'a') as file:
        file.write("\n- [ ] " + task)
        file.close()
        list()

def list():
    with open(TODO_FILE_PATH, 'r') as file:
        lines = file.readlines()
        for idx in range(len(lines)):
            lines[idx] = lines[idx].replace("\n", "")
            print(f" {idx}   {lines[idx]}")
        file.close()

def remove(idx):
    with open(TODO_FILE_PATH, 'r+') as file:
        lines = file.readlines()
        del lines[idx]
        writeToFile(lines, file)
        file.close()
        list()

def tag(idx, key, value):
    # TODO: check if tag of same type exists already and replace
    with open(TODO_FILE_PATH, 'r+') as file:
        lines = file.readlines()
        lines[idx] = lines[idx].strip() + f" [{key}:: {value}]\n"
        writeToFile(lines, file)
        file.close()
        list()

def complete(idx):
    with open(TODO_FILE_PATH, 'r+') as file:
        lines = file.readlines()
        lines[idx] = lines[idx].replace('[ ]', '[x]')
        writeToFile(lines, file)
        file.close()
        list()

