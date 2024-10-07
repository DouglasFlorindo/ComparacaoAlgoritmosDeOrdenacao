class BubbleSort:

    def __call__(self, data: list) -> list:
        return self.bubble_sort(data)
    
    def bubble_sort(self, data: list) -> list:
        n = len(data)
        for i in range(n):
            already_sorted = True
            for j in range(n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    already_sorted = False
            if already_sorted:
                break
        return data       

