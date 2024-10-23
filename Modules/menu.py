from SortingAlgorithms.bubbleSort import *
from SortingAlgorithms.quickSortAntigo import *
from SortingAlgorithms.quickSort import *
from SortingAlgorithms.insertionSort import *
from SortingAlgorithms.selectionSort import *
from SortingAlgorithms.radixSort import *
from Modules.test import *

class Menu:

    def __init__(self):
        self.data_list: list = self.get_data('data.txt')
        self.separator: str = "==============="


    def __call__(self) -> None:
        self.main_menu()
        

    def get_data(self, file_name: str) -> list:
        try:
            raw: str = ''
            with open('data.txt') as f:
                raw = f.read()
                f.close()
            raw_list: list = raw.split(',')
            int_list: list = []
            for item in raw_list:
                int_list.append(int(item))
            return int_list
        except Exception as e:
            print(e)
            return []
        
    def main_menu(self):
        while True:
            print(self.separator)
            current_test: Test = Test()
            current_algorithm: callable = self.menu_algorithm()
            num_data: int = self.menu_data()
            num_tests: int = self.menu_iterations()

            current_test.execute_tests(current_algorithm, self.data_list[:num_data], num_tests)
            current_test.export_results_to_csv()
            print(current_test.get_relevant_results())
            
    

    def menu_algorithm(self) -> callable:
        print("Algoritmo:")
        print("1) Bubble Sort")
        print("2) Quick Sort")
        print("3) Insertion Sort")
        print("4) Radix Sort")
        print("5) Selection Sort")
        match int(input()):
            case 1:
                return BubbleSort()
            case 2: 
                return QuickSort()
            case 3:
                return InsertionSort()
            case 4:
                return RadixSort()
            case 5:
                return SelectionSort()
            case __default__:
                return None


    def menu_data(self) -> int:
        print("Número de dados:")
        print("1) 1K")
        print("2) 10K")
        print("3) 50K")
        print("4) 80K")
        print("5) 100K")
        match int(input()):
            case 1:
                return 10**3
            case 2:
                return 10**4
            case 3:
                return 10**4 * 5
            case 4:
                return 10**4 * 8
            case 5:
                return 10**5
            case __default__:
                return 0


    def menu_iterations(self) -> int:
        print("Número de iterações: ")
        return int(input())


