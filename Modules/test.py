from Modules.timer import *
import socket
from csv import DictWriter


class Test:

    def __init__(self):
        self.algorithm: callable = None
        self.data_pre: list = []
        self.data_post: list = []
        self.data_quantity: int = 0
        self.tests_quantity: int = 0
        self.execution_times_ns: list = []
        self.total_execution_time_ns: int = 0 
        self.average_execution_time_ns: int = 0
        self.host_name: str = self.get_host_name()
        self.timer: Timer = Timer()


    def time_test(self, sorting_algorithm: callable, data: list) -> int:
        """
            Executa o algoritmo de ordenação uma vez e retorna o tempo de execução em nanosegundos.\n
            Obs: o algoritmo de ordenação deve ser chamável.
        """
        result: int = self.timer.time_callable(sorting_algorithm, data)

        return result
        

    def execute_tests(self, sorting_algorithm: callable, data: list, num_iterations: int = 1) -> dict:
        """
            Limpa os resultados, executa o algoritmo de ordenação n vezes e armazena os tempos de execução, o tempo total de execução e a média do tempo de execução. Também retorna os resultados em forma de dicionário.\n
            Obs: o algoritmo de ordenação deve ser chamável.
        """
        try: 
            
            if not self.functional_test(sorting_algorithm):
                print('Algoritmo não passou o teste funcional.\nTeste interrompido.')
                return 
            
            self.clear_results()
            self.algorithm = sorting_algorithm.__class__.__name__
            self.data_pre = data
            self.data_post = sorting_algorithm(data)
            self.data_quantity = len(data)
            self.tests_quantity = num_iterations

            for i in range(num_iterations):
                execution_time_ns: int = self.time_test(sorting_algorithm, data)
                self.execution_times_ns.append(execution_time_ns)

            self.total_execution_time_ns = sum(self.execution_times_ns)
            self.average_execution_time_ns = self.total_execution_time_ns // num_iterations

            return self.get_relevant_results()
        
        except Exception as e: 

            print(e)
        
    
    def clear_results(self):
        """Limpa os resultados armazenadobj = Test()
obj.execute_tests(QuickSort(), lista, 1)
print(obj.get_relevant_results())
obj.export_results_to_csv()os."""
        self.algorithm: callable = None
        self.data_pre: list = []
        self.data_post: list = []
        self.data_quantity: int = 0
        self.tests_quantity: int = 0
        self.execution_times_ns: list = []
        self.total_execution_time_ns: int = 0 
        self.average_execution_time_ns: int = 0
        
    
    def functional_test(self, sorting_algorithm: callable) -> bool:
        """Verifica se o algoritmo consegue ordenar uma lista teste."""
        try:

            result: list = sorting_algorithm([1, 4, 2, 3, 5])
            if not result == [1, 2, 3, 4, 5]:
                return False
            return True
        
        except Exception as e:

            print(e)


    def get_relevant_results(self) -> dict:
        """Retorna os resultados armazenados mais relevantes."""
        return {
                'Nome da máquina': self.host_name,
                'Algoritmo': self.algorithm,
                'Quantidade de dados ordenados': self.data_quantity,
                'Quantidade de testes realizados': self.tests_quantity,
                'Tempo total de execução em ms': self.total_execution_time_ns / 10**6,
                'Tempo médio de execução em ms': self.average_execution_time_ns / 10**6
            }
    

    
    def export_results_to_csv(self, csv_path: str = r'resultsTable.csv'):
        results = self.get_relevant_results()
        csv_header = [ # TODO
                'Nome da máquina',
                'Algoritmo',
                'Quantidade de dados ordenados',
                'Quantidade de testes realizados',
                'Tempo total de execução em ms',
                'Tempo médio de execução em ms'
            ]
        
        with open(csv_path, "a", newline="") as f_object:
            dictwriter_object = DictWriter(f_object, fieldnames=csv_header)
            dictwriter_object.writerow(results)
            f_object.close()


    def get_host_name(self) -> str:
        """Retorna o nome da máquina executando o teste."""
        host_name: str = None

        try:
            host_name = socket.gethostname()
        except Exception as e:
            print(e)

        return host_name
    