class InsertionSort:

    def __call__(self, data: list) -> list:
        return self.insertion_sort(data)

    def insertion_sort(self, data: list) -> list:
        for step in range(1, len(data)):
                key = data[step]
                j = step - 1
                   
                while j >= 0 and key < data[j]:
                    data[j + 1] = data[j]
                    j = j - 1
                
                data[j + 1] = key
        return data
