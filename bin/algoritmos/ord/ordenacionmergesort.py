from bin.algoritmos.ordenacion import Ordenacion
from bin.algoritmos.comprobar import comprobar_ejecucion_ordenacion as comp
from bin.algoritmos.ord.ordenacioninsercion import ordenacion_insercion

k = 7


class OrdenacionMergesort(Ordenacion):

    def __init__(self):
        super().__init__(0)

    def ejecutar(self, data_input, valor_busqueda=None):
        comp(data_input)
        return ordenacion_mergesort(list(data_input), list(data_input), 0, len(data_input) - 1)

    def analizar(self, data_input, analysis, valor_busqueda=None):
        pass


def ordenacion_mergesort(ls, aux, pri, ult):
    if ult <= pri + k - 1:
        return ordenacion_insercion(aux, pri, ult)
    else:
        mit = pri + (ult - pri) // 2
        ordenacion_mergesort(aux, ls, pri, mit)
        ordenacion_mergesort(aux, ls, mit + 1, ult)
        if ls[mit] <= ls[mit + 1]:
            return ls
        merge(ls, aux, pri, mit, ult)
        return aux


def merge(ls, aux, pri, mit, ult):
    i, j = pri, mit + 1
    for m in range(pri, ult + 1):
        if i > mit:
            aux[m] = ls[j]
            j += 1
        elif j > ult:
            aux[m] = ls[i]
            i += 1
        elif ls[j] < ls[i]:
            aux[m] = ls[j]
            j += 1
        else:
            aux[m] = ls[i]
            i += 1
