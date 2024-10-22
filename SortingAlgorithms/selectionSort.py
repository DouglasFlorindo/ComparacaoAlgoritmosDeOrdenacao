class SelectionSort:

    def __call__(self, data: list) -> list:
        return self.selection_sort(data)

    def selection_sort(self, data: list) -> list:
        if not data:
            return data
        for i in range(len(data)):
            min_i = i
            for j in range(i + 1, len(data)):
                if data[j] < data[min_i]:
                    min_i = j
            data[i], data[min_i] = data[min_i], data[i]
        return data