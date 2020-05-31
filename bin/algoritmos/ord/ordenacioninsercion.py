import bin.operaciones_basicas as ob
from bin.algoritmos.ordenacion import Ordenacion
from bin.algoritmos.comprobar import comprobar_ejecucion_ordenacion as comp
from bin.algoritmos.comprobar import comprobar_analisis_ordenacion as compa


class OrdenacionInsercion(Ordenacion):

    def __init__(self):
        super().__init__(1)

    def ejecutar(self, data_input, valor_busqueda=None):
        comp(data_input)
        lista = list(data_input)
        return ordenacion_insercion(lista, 0, len(lista) - 1)

    def analizar(self, data_input, analysis, valor_busqueda=None):
        compa(data_input, analysis)
        lista = list(data_input)
        return ordenacion_insercion_analisis(lista, 0, len(lista) - 1, analysis)


def ordenacion_insercion(lista, inicio, fin):
    for i in range(inicio + 1, fin + 1):
        j = i
        while j > inicio:
            if lista[j] < lista[j - 1]:
                ob.intercambiar(lista, j, j - 1)
                j -= 1
            else:
                break
    return lista


def ordenacion_insercion_analisis(lista, inicio, fin, an):
    an.sum_eu(2)

    an.sum_declaracion(1)
    for i in range(inicio + 1, fin + 1):
        an.sum_co(1)

        an.sum_declaracion(1)
        j = i

        while j > inicio:
            an.sum_co(1)

            an.sum_co(1)
            if lista[j] < lista[j - 1]:
                an.sum_intercambio_misma_lista(1)
                ob.intercambiar(lista, j, j - 1)

                an.sum_te(1)
                j -= 1
            else:
                break
        an.sum_co(1)

        an.sum_te(1)
    an.sum_co(1)
    return lista
