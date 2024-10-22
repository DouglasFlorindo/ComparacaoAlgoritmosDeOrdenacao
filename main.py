from SortingAlgorithms.bubbleSort import *
from SortingAlgorithms.quickSortAntigo import *
from SortingAlgorithms.quickSort import *
from SortingAlgorithms.insertionSort import *
from SortingAlgorithms.selectionSort import *
from SortingAlgorithms.radixSort import *
from Modules.test import *
import sys

sys.setrecursionlimit(1000000) # Aumenta o limite de recursividade (a quantidade de vezes que uma função pode chamar a si mesma)
# 1K 10K 50K 80K 100K

def get_data(file_name: str) -> list:
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
    

def menu_algorithm() -> callable:
    print("Selecione o algoritmo:")
    print("1) Bubble Sort")
    print("2) Quick Sort")
    match int(input()):
        case 1:
            return BubbleSort()
        case 2: 
            return QuickSort()
        case __default__:
            return None
    

def menu_data() -> int:
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
        

def menu_iterations() -> int:
    print("Número de iterações: ")
    return int(input())
    

data_list: list = get_data('data.txt')
separator: str = "========================="

while True:
    print(separator)
    
    break