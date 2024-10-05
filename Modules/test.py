from Modules.timer import *

class Test:

    def __init__(self):
        self.execution_times_ns: list = []
        self.total_execution_time_ns: int = 0 
        self.average_execution_time_ns: int = 0
        self.timer: Timer = Timer()


    def test(self, sorting_algorithm: callable, data: list) -> int:
        """
            Executa o algoritmo de ordenação uma vez e retorna o tempo de execução em nanosegundos.\n
            Obs: o algoritmo de ordenação deve ser chamável.
        """
        return self.timer.time_callable(sorting_algorithm, data)
        

    def execute_tests(self, sorting_algorithm: callable, data: list, num_iterations: int) -> dict:
        """
            Limpa os resultados, executa o algoritmo de ordenação n vezes e armazena os tempos de execução, o tempo total de execução e a média do tempo de execução. Também retorna os resultados em forma de dicionário.\n
            Obs: o algoritmo de ordenação deve ser chamável.
        """
        try: 
            self.clear_results()
            for i in range(num_iterations):
                execution_time_ns: int = self.test(sorting_algorithm, data)
                self.execution_times_ns.append(execution_time_ns)
            self.total_execution_time_ns = sum(self.execution_times_ns)
            self.average_execution_time_ns = self.total_execution_time_ns // num_iterations
            results: dict = {
                'execution_times_ns': self.execution_times_ns,
                'total_execution_time_ns': self.total_execution_time_ns,
                'average_execution_time_ns': self.average_execution_time_ns
            }
            return results
        except Exception as e: 
            print(e)
        
    
    def clear_results(self):
        """Limpa os resultados armazenados."""
        self.execution_times_ns: list = []
        self.total_execution_time_ns: int = 0 
        self.average_execution_time_ns: int = 0
        
    
