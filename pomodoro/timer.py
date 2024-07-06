import time
from actionManager.bcolors import bcolors
import art

# TODO: Make a Timer class that allows you to start and stop the timer, etc.
class Timer:
    def __init__(self, current_task, minutes=25):
        self.timer_minutes = minutes
        self.timer_seconds = 60
        self.minutes_remaining = self.timer_minutes 
        self.seconds_remaining = self.timer_seconds
        self.current_task = current_task

    def start(self):
        try:
            # print task and time, clearing screen each second
            for i in range(1, self.timer_minutes + 1):
                self.minutes_remaining = self.timer_minutes - i
                for j in range(1, self.timer_seconds + 1):
                    self.seconds_remaining = self.timer_seconds - j
                    self.print_time_to_screen()
                    time.sleep(1)
            print("Time's up!")
            return 1
        except KeyboardInterrupt:
            print("")
            print("1) Pause the timer")
            print("2) Stop the timer")
            opt = input()
            if opt == '1':
                self.pause()
            elif opt == '2':
                self.stop()

    def stop(self):
        # reset the timer
        # increment the number of pomodoros
        pass

    def pause(self):
        # set self.minutes_remaining and self.seconds_remaining to the time left
        print("\033[2J\033[1;1H")
        print(f"{bcolors.UNDERLINE}{self.current_task}: Timer paused with {self.minutes_remaining}:{self.seconds_remaining:02}{bcolors.ENDC}")
        print("1) Continue")
        print("2) Stop")
        opt = input()
        if opt == '1':
            self.start()

    def print_time_to_screen(self):
        print("\033[2J\033[1;1H")           # ascii code for clear screen
        print(f"{bcolors.UNDERLINE}{self.current_task}{bcolors.ENDC}")
        if self.minutes_remaining >= 5:
            print(f"{bcolors.OKGREEN}")
            art.tprint(f"{self.minutes_remaining}:{self.seconds_remaining:02}", font="doh")
            print(f"{bcolors.ENDC}")
        else:
            print(f"{bcolors.RED}")
            art.tprint(f"{self.minutes_remaining}:{self.seconds_remaining:02}", font="doh")
            print(f"{bcolors.ENDC}")

