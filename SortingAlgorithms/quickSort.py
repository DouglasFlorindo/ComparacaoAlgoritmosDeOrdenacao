class QuickSort:

    def __call__(self, data: list) -> list:
        return self.quick_sort(data)

    def quick_sort(self, lista: list) -> list:
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
