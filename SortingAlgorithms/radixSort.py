class RadixSort:

    def __call__(self, data: list) -> list:
        return self.radix_sort(data)

    def countingSort(self, array, place):
        size = len(array)
        output = [0] * size
        count = [0] * 10

        for i in range(0, size):
            index = array[i] // place
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = size - 1
        while i >= 0:
            index = array[i] // place
            output[count[index % 10] - 1] = array[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(0, size):
            array[i] = output[i]
   
    def radix_sort(self, data: list) -> list:  
        max_element = max(data)

        place = 1
        while max_element // place > 0:
            self.countingSort(data, place)
            place *= 10
        return data
