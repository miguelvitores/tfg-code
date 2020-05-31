import bin.excepciones as ex
import bin.operaciones_basicas as ob
from bin.algoritmos.ordenacion import Ordenacion
from bin.algoritmos.comprobar import comprobar_ejecucion_ordenacion as comp
from bin.algoritmos.comprobar import comprobar_analisis_ordenacion as compa
from bin.algoritmos.ord.ordenacioninsercion import ordenacion_insercion
from bin.algoritmos.ord.ordenacioninsercion import ordenacion_insercion_analisis

k = 10


class OrdenacionQuicksort(Ordenacion):

    def __init__(self):
        super().__init__(3)

    def ejecutar(self, data_input, valor_busqueda=None):
        comp(data_input)
        lista = ob.mezclar_aleatorio(data_input)
        n = len(lista)
        if n <= 1:
            return lista
        return ordenacion_3wayquicksort(lista, 0, n - 1)

    def analizar(self, data_input, analysis, valor_busqueda=None):
        compa(data_input, analysis)
        lista = ob.mezclar_aleatorio_analisis(data_input, analysis)

        analysis.sum_declaracion(1)
        n = len(lista)

        analysis.sum_co(1)
        if n <= 1:
            return lista
        return ordenacion_3wayquicksort_analisis(lista, 0, n - 1, analysis)


def ordenacion_3wayquicksort(ls, pri, ult):
    if ult <= pri:
        return
    elif ult - pri <= k:
        return ordenacion_insercion(ls, pri, ult)
    menos, mas, i = pri, ult, pri
    vert = ls[pri]
    while i <= mas:
        if ls[i] < vert:
            ob.intercambiar(ls, menos, i)
            menos += 1
            i += 1
        elif ls[i] > vert:
            ob.intercambiar(ls, i, mas)
            mas -= 1
        else:
            i += 1
    ordenacion_3wayquicksort(ls, pri, menos - 1)
    ordenacion_3wayquicksort(ls, mas + 1, ult)
    return ls


def ordenacion_3wayquicksort_analisis(ls, pri, ult, an):
    an.sum_eu(2)

    if ult <= pri:
        an.sum_co(1)
        return
    elif ult - pri <= k:
        an.sum_co(2)
        return ordenacion_insercion_analisis(ls, pri, ult, an)

    an.sum_declaracion(4)
    menos, mas, i = pri, ult, pri
    vert = ls[pri]

    while i <= mas:
        an.sum_co(1)

        if ls[i] < vert:
            an.sum_co(1)

            an.sum_intercambio_misma_lista(1)
            ob.intercambiar(ls, menos, i)

            an.sum_te(2)
            menos += 1
            i += 1
        elif ls[i] > vert:
            an.sum_co(2)

            an.sum_intercambio_misma_lista(1)
            ob.intercambiar(ls, i, mas)

            an.sum_te(2)
            mas -= 1
        else:
            an.sum_co(2)

            an.sum_te(1)
            i += 1
    an.sum_co(1)

    ordenacion_3wayquicksort_analisis(ls, pri, menos - 1, an)
    ordenacion_3wayquicksort_analisis(ls, mas + 1, ult, an)
    return ls
