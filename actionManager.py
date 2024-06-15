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

def list():
    with open(TODO_FILE_PATH, 'r') as file:
        lines = file.readlines()
        for idx, val in enumerate(lines):
            lines[idx] = lines[idx].replace("\n", "")
            print(lines[idx])     
        file.close()

def remove(idx):
    with open(TODO_FILE_PATH, 'r+') as file:
        lines = file.readlines()
        del lines[idx]
        writeToFile(lines, file)

def complete(idx):
    with open(TODO_FILE_PATH, 'r+') as file:
        lines = file.readlines()
        lines[idx] = lines[idx].replace('[ ]', '[x]')
        writeToFile(lines, file)
        file.close()

