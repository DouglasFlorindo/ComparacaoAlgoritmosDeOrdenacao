from SortingAlgorithms.bubbleSort import *
from SortingAlgorithms.quickSort import *

from Modules.test import *


print(Test().execute_tests(BubbleSort(), [3, 1, 2], 1000))
print(Test().execute_tests(QuickSort(), [3, 1, 2], 1000))

