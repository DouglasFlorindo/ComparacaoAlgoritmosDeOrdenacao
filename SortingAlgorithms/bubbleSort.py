class BubbleSort:

    def __call__(self, list):
        n = len(list)
        for i in range(n):
            already_sorted = True
            for j in range(n - i - 1):
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
                    already_sorted = False
            if already_sorted:
                break
        return list
    
