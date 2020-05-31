import bin.operaciones_basicas as ob
from bin.algoritmos.ordenacion import Ordenacion
from bin.algoritmos.comprobar import comprobar_ejecucion_ordenacion as comp
from bin.algoritmos.comprobar import comprobar_analisis_ordenacion as compa


class OrdenacionBurbuja(Ordenacion):

    def __init__(self):
        super().__init__(2)

    def ejecutar(self, data_input, valor_busqueda=None):
        comp(data_input)
        lista = list(data_input)
        return ordenacion_burbuja(lista)

    def analizar(self, data_input, analysis, valor_busqueda=None):
        compa(data_input, analysis)
        lista = list(data_input)
        return ordenacion_burbuja_analisis(lista, analysis)


def ordenacion_burbuja(lista):
    n = len(lista)
    repetir = True
    while repetir:
        repetir = False
        for i in range(1, n):
            if lista[i - 1] > lista[i]:
                ob.intercambiar(lista, i - 1, i)
                repetir = True
    return lista


def ordenacion_burbuja_analisis(lista, an):
    an.sum_declaracion(2)
    n = len(lista)
    repetir = True

    while repetir:
        an.sum_co(1)

        an.sum_te(1)
        repetir = False

        an.sum_declaracion(1)
        for i in range(1, n):
            an.sum_co(1)

            an.sum_co(1)
            if lista[i - 1] > lista[i]:
                an.sum_intercambio_misma_lista(1)
                ob.intercambiar(lista, i - 1, i)

                an.sum_te(1)
                repetir = True

            an.sum_te(1)
        an.sum_co(1)

    an.sum_co(1)

    return lista
