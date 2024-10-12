class QuickSort:

    def __call__(self, data: list) -> list:
        return self.quick_sort(data)

    def quick_sort(self, data: list) -> list:
        less = []
        equal = []
        greater = []

        if len(data) > 1:
            pivot = data[0]
            for x in data:
                if x < pivot:
                    less.append(x)
                elif x == pivot:
                    equal.append(x)
                elif x > pivot:
                    greater.append(x)
            return self.quick_sort(less) + equal + self.quick_sort(greater) 
        else: 
            return data
