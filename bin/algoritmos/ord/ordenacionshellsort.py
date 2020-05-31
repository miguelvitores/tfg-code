import bin.operaciones_basicas as ob
from bin.algoritmos.ordenacion import Ordenacion
from bin.algoritmos.comprobar import comprobar_ejecucion_ordenacion as comp
from bin.algoritmos.comprobar import comprobar_analisis_ordenacion as compa


class OrdenacionShellsort(Ordenacion):

    def __init__(self):
        super().__init__(4)

    def ejecutar(self, data_input, valor_busqueda=None):
        comp(data_input)
        lista = ob.mezclar_aleatorio(data_input)
        return ordenacion_3xmas1shellsort(lista)

    def analizar(self, data_input, analysis, valor_busqueda=None):
        compa(data_input, analysis)
        lista = ob.mezclar_aleatorio_analisis(data_input, analysis)
        return ordenacion_3xmas1shellsort_analisis(lista, analysis)


def ordenacion_3xmas1shellsort(ls):
    n = len(ls)

    h = 1
    while h < n/3:
        h = 3*h + 1

    while h >= 1:
        for i in range(h, n):
            j = i
            while j >= h and ls[j] < ls[j - h]:
                ob.intercambiar(ls, j, j - h)
                j -= 1
        h = h // 3

    return ls


def ordenacion_3xmas1shellsort_analisis(ls, an):
    an.sum_declaracion(2)
    n = len(ls)
    h = 1

    while h < n/3:
        an.sum_co(1)
        an.sum_te(1)
        h = 3*h + 1
    an.sum_co(1)

    while h >= 1:
        an.sum_co(1)

        an.sum_declaracion(1)
        for i in range(h, n):
            an.sum_co(1)

            an.sum_declaracion(1)
            j = i
            while j >= h and ls[j] < ls[j - h]:
                an.sum_co(2)

                an.sum_intercambio_misma_lista(1)
                ob.intercambiar(ls, j, j - h)

                an.sum_te(1)
                j -= 1
            an.sum_co(2)

        an.sum_co(1)

        an.sum_te(2)
        h = h // 3

    an.sum_co(1)

    return ls
