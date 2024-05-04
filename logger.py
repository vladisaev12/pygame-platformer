import time
import math
from enum import Enum

stime = time.time()


class DEBUG_LEVEL(Enum):
    INFO = 0
    WARNING = 1
    ERROR = 2
    DEBUG = 3

def running_time():
    raw_secs = time.time() - stime
    secs = math.floor(raw_secs)
    millisecs = int(float('{:.4f}'.format(raw_secs - secs)) * 10)
    mins = secs // 60
    
    return f"{mins:02}:{secs:02}:{millisecs:04}"

def log_write(msg: str, debug_level: DEBUG_LEVEL):
    log_file.write(f"[{running_time()}] {debug_level} {msg}")
    print(f"[{running_time()}] {debug_level} {msg}")


log_file = open("1.log", "+w")
log_write("Log File Connected", DEBUG_LEVEL.INFO)
