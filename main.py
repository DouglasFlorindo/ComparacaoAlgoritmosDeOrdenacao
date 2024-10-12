from SortingAlgorithms.bubbleSort import *
from SortingAlgorithms.quickSortAntigo import *
from SortingAlgorithms.quickSort import *
from Modules.test import *
import sys
import random

sys.setrecursionlimit(1000000) # Aumenta o limite de recursividade (a quantidade de vezes que uma função pode chamar a si mesma)

lista = []

for i in range(1000):
    lista.append(i)

random.shuffle(lista)

obj = Test()
obj.execute_tests(QuickSort(), lista, 1)
obj.export_results_to_csv()
# Favor rodar somente um teste por vez ;)

# print(Test().execute_tests(QuickSort(), lista, 500))
# print(Test().execute_tests(BubbleSort(), lista, 500))
# print(Test().execute_tests(QuickSortAlt(), lista, 500))


