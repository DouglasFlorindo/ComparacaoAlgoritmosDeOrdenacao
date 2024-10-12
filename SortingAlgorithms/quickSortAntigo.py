class QuickSortAntigo:

    def __call__(self, data: list) -> list:
        return self.quick_sort_antigo(data)

    def partition(self, data: list, low: int, high: int) -> int:
        pivot = data[high]
        i = low - 1

        for j in range(low, high):
            if data[j] <= pivot:
                i += 1
                data[i], data[j] = data[j], data[i]

        data[i+1], data[high] = data[high], data[i+1]
        return i + 1

    def quick_sort_antigo(self, data: list, low: int = 0, high: int = None) -> list:
        if high is None:
            high = len(data) - 1

        if low < high:
            pivot_index = self.partition(data, low, high)
            self.quick_sort_antigo(data, low, pivot_index-1)
            self.quick_sort_antigo(data, pivot_index+1, high)
        
        return data



