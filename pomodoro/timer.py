import time
from actionManager.bcolors import bcolors

def timer(current_task, t=25):
    # print task and time, clearing screen each second
    for i in range(1, t):
        # FIXME: timer stops at 1:00
        print(t - i)
        for j in range(1, 61):
            # clear screen
            print("\033[2J\033[1;1H")
            print(f"{bcolors.UNDERLINE}{current_task}{bcolors.ENDC}")
            print(f"Time left: {t - i}:{60-j:02}")
            time.sleep(1)
    print("Time's up!")
    return 1

# TODO: add a way to stop the timer
# TODO: add a way to pause the timer
# TODO: add a way to resume the timer
