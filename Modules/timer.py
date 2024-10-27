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
        """Reseta e inicia o timer, e armazena o tempo inicial."""
        if self.state == TimerState.RUNNING:
            self.stop()
        self.reset_timer()
        self.state = TimerState.RUNNING
        self.start_time_ns = perf_counter_ns()


    def stop(self) -> int:
        """Para o timer e retorna a diferença entre o tempo final e o tempo inicial em nanosegundos."""
        stop_time_ns: int = perf_counter_ns()
        if self.state == TimerState.IDLE:
            return 0
        self.state = TimerState.IDLE
        elapsed_time_ns = stop_time_ns - self.start_time_ns
        return elapsed_time_ns


    def time_callable(self, callable: callable, arg) -> int:
        """Retorna o tempo em nanosegundos da execução de um callable."""
        try:
            self.start()
            callable(arg)
            return self.stop()
        except Exception as e: 
            print(e)
            return -1
        

    def reset_timer(self):
        """Reseta o timer."""
        self.start_time_ns = 0    