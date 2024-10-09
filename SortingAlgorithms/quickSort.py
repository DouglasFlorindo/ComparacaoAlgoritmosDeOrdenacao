
def __call__(self, data: array):
    self.quick_sort(data)

    def partition(array, low, high):
        pivot = array[high]
        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]

        array[i+1], array[high] = array[high], array[i+1]
        return i+1

    def quicksort(array, low=0, high=None):
        if high is None:
            high = len(array) - 1

        if low < high:
            pivot_index = partition(array, low, high)
            quicksort(array, low, pivot_index-1)
            quicksort(array, pivot_index+1, high)









"""
class QuickSort:
    lista = [5, 4, 3, 2, 1]
    def __call__(self, lista):
        self.quick_sort(lista)
        return lista
    def quick_sort(self, lista):

        print(lista)
        tamanho_da_lista = len(lista)
        if tamanho_da_lista > 0:
            inicio = 0
            fim = tamanho_da_lista - 1
            anterior = inicio
            posterior = fim
            pivo = lista[inicio]

            while anterior < posterior:
                while anterior < posterior and lista[posterior] > pivo:
                    posterior = posterior - 1

                if anterior < posterior:
                    lista[anterior] = lista[posterior]
                    anterior = anterior + 1

                while anterior < posterior and lista[anterior] <= pivo:
                    anterior = anterior + 1

                if anterior < posterior:
                    lista[posterior] = lista[anterior]
                    posterior = posterior - 1

                lista[anterior] = pivo
            print(lista)

            return lista
"""

##lista = [5,4,7,2,1]

"""lista = [8, 2, 3, 7,9]
def quicksort(lista):
    listaOrdenada=[]
    menores = []
    maiores=[]
    igual=[]

    pivo = len(lista)//2
    pivo = lista[pivo+1]
    print(pivo)

    for i in lista:
        if i < pivo:
            menores.append(i)
        if i == pivo:
            igual.append(i)
        if i > pivo:

            maiores.append(i)



    for me in menores:
        listaOrdenada.append(me)
    for ig in igual:

        listaOrdenada.append(ig)
    for ma in maiores:

        listaOrdenada.append(ma)

    print(listaOrdenada)


quicksort(lista)
print("oioioio")
"""



#Python
