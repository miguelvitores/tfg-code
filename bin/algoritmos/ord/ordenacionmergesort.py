from bin.algoritmos.ordenacion import Ordenacion
from bin.algoritmos.comprobar import comprobar_ejecucion_ordenacion as comp
from bin.algoritmos.comprobar import comprobar_analisis_ordenacion as compa
from bin.algoritmos.ord.ordenacioninsercion import ordenacion_insercion
from bin.algoritmos.ord.ordenacioninsercion import ordenacion_insercion_analisis

k = 7


class OrdenacionMergesort(Ordenacion):

    def __init__(self):
        super().__init__(5)

    def ejecutar(self, data_input, valor_busqueda=None):
        comp(data_input)
        return ordenacion_mergesort(list(data_input), list(data_input), 0, len(data_input) - 1)

    def analizar(self, data_input, analysis, valor_busqueda=None):
        compa(data_input, analysis)
        return ordenacion_mergesort_analisis(list(data_input), list(data_input), 0, len(data_input) - 1, analysis)


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


def ordenacion_mergesort_analisis(ls, aux, pri, ult, an):
    an.sum_eu(len(aux) + 2)

    an.sum_co(1)
    if ult <= pri + k - 1:
        return ordenacion_insercion_analisis(aux, pri, ult, an)

    else:
        an.sum_declaracion(1)
        mit = pri + (ult - pri) // 2

        ordenacion_mergesort_analisis(aux, ls, pri, mit, an)
        ordenacion_mergesort_analisis(aux, ls, mit + 1, ult, an)

        an.sum_co(1)
        if ls[mit] <= ls[mit + 1]:
            return ls

        merge_analisis(ls, aux, pri, mit, ult, an)
        return aux


def merge_analisis(ls, aux, pri, mit, ult, an):
    an.sum_eu(len(aux) + 3)

    an.sum_declaracion(2)
    i, j = pri, mit + 1

    an.sum_declaracion(1)
    for m in range(pri, ult + 1):
        an.sum_co(1)

        if i > mit:
            an.sum_co(1)

            an.sum_in(1)
            aux[m] = ls[j]

            an.sum_te(1)
            j += 1
        elif j > ult:
            an.sum_co(2)

            an.sum_in(1)
            aux[m] = ls[i]

            an.sum_te(1)
            i += 1
        elif ls[j] < ls[i]:
            an.sum_co(3)

            an.sum_in(1)
            aux[m] = ls[j]

            an.sum_te(1)
            j += 1
        else:
            an.sum_co(3)

            an.sum_in(1)
            aux[m] = ls[i]

            an.sum_te(1)
            i += 1

        an.sum_te(1)
    an.sum_co(1)
