class QuickSort:

    def __call__(self, list):
        tamanho_da_lista = len(list)
        if tamanho_da_lista > 0:
            self.quick_sort(list, 0, tamanho_da_lista - 1)

    def quick_sort(self,lista, inicio, fim):
        if inicio > fim:
            return
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

