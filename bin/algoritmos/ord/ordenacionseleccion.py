import bin.operaciones_basicas as ob
from bin.algoritmos.ordenacion import Ordenacion
from bin.algoritmos.comprobar import comprobar_ejecucion_ordenacion as comp
from bin.algoritmos.comprobar import comprobar_analisis_ordenacion as compa


class OrdenacionSeleccion(Ordenacion):

    def __init__(self):
        super().__init__(0)

    def ejecutar(self, data_input, valor_busqueda=None):
        comp(data_input)
        lista = list(data_input)
        return ordenacion_seleccion(lista)

    def analizar(self, data_input, analysis, valor_busqueda=None):
        compa(data_input, analysis)
        lista = list(data_input)
        return ordenacion_seleccion_analisis(lista, analysis)


def ordenacion_seleccion(lista):
    n = len(lista)
    for i in range(n - 1):
        minimo = i
        for j in range(i, n):
            if lista[minimo] > lista[j]:
                minimo = j
        if not minimo == i:
            ob.intercambiar(lista, minimo, i)
    return lista


def ordenacion_seleccion_analisis(lista, an):
    an.sum_declaracion(1)
    n = len(lista)

    an.sum_declaracion(1)
    for i in range(n - 1):
        an.sum_co(1)

        an.sum_declaracion(1)
        minimo = i

        an.sum_declaracion(1)
        for j in range(i, n):
            an.sum_co(1)

            an.sum_co(1)
            if lista[minimo] > lista[j]:
                an.sum_te(1)
                minimo = j

            an.sum_te(1)
        an.sum_co(1)

        an.sum_co(1)
        if not minimo == i:
            an.sum_intercambio_misma_lista(1)
            ob.intercambiar(lista, minimo, i)

        an.sum_te(1)
    an.sum_co(1)
    return lista
