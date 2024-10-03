from enum import *
from time import *

class TimerState(Enum):
    RUNNING = 1
    IDLE = 2

class Timer:

    def __init__(self):
        self.state: TimerState = TimerState.IDLE
        self.start_time_ns: int = 0 
    

    def start(self):
        if self.state == TimerState.RUNNING:
            self.stop()
        self.reset_timer()
        self.state = TimerState.RUNNING
        self.start_time = process_time_ns()


    def stop(self) -> int:
        stop_time_ns: int = process_time_ns()
        if self.state == TimerState.IDLE:
            return 0
        self.state = TimerState.IDLE
        elapsed_time_ns = stop_time_ns - self.start_time_ns
        return elapsed_time_ns


    def reset_timer(self):
        self.start_time = 0
