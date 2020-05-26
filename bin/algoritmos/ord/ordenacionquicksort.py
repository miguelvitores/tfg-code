import bin.excepciones as ex
import bin.operaciones_basicas as ob
from bin.algoritmos.ordenacion import Ordenacion
from bin.algoritmos.comprobar import comprobar_ejecucion_ordenacion as comp
from bin.algoritmos.ord.ordenacioninsercion import ordenacion_insercion

k = 10


class OrdenacionQuicksort(Ordenacion):

    def __init__(self):
        super().__init__(0)

    def ejecutar(self, data_input, valor_busqueda=None):
        comp(data_input)
        lista = ob.mezclar_aleatorio(data_input)
        n = len(lista)
        if n <= 1:
            return lista
        return ordenacion_3wayquicksort(lista, 0, n - 1)

    def analizar(self, data_input, analysis, valor_busqueda=None):
        pass


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
