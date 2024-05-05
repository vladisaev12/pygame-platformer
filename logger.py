import time
import math
from enum import Enum
from os.path import isfile
from os import getcwd

stime = time.time()

def running_time():
    raw_secs = time.time() - stime
    secs = math.floor(raw_secs)
    millisecs = int(float('{:.4f}'.format(raw_secs - secs)) * 10)
    mins = secs // 60
    
    return f"{mins:02}:{secs:02}:{millisecs:04}"

class Logger:
    
    class DEBUG_LEVEL(Enum):
        INFO =    0
        WARNING = 1
        ERROR =   2
        DEBUG =   3

    def __init__(self, debug_level: DEBUG_LEVEL) -> None:
        self._debug_level = debug_level
        self.log_file = open("latest.log", "w")
        print(getcwd())
        if not isfile(getcwd() + "/latest.log"):
            self.log_file = open("latest.log", "x")
            self.log_write("Logger Initilizated", self.DEBUG_LEVEL.INFO)
        elif isfile(getcwd() + "latest.log"):
            self.log_file = open("latest.log", "w")
            self.log_write("Logger Initilizated", self.DEBUG_LEVEL.INFO)

    def log_write(self, msg: str, debug_level):
        if self.DEBUG_LEVEL[debug_level.name] == self.DEBUG_LEVEL[self._debug_level.name]:
            self.log_file.write("\n")
            self.log_file.write(f"[{running_time()}] {debug_level} {msg}")
            print("\n")
            print(f"[{running_time()}] {debug_level} {msg}")


