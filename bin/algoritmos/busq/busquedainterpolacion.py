import bin.excepciones as ex
from bin.algoritmos.busqueda import Busqueda
from bin.algoritmos.comprobar import comprobar_ejecucion_busqueda as comp
from bin.algoritmos.comprobar import comprobar_analisis_busqueda as compa
from bin.algoritmos.comprobar import comprobar_lista_ordenada_busqueda as complo
import math


class BusquedaInterpolacion(Busqueda):

    def __init__(self):
        super().__init__(3)

    def ejecutar(self, data_input, valor_busqueda):
        comp(data_input, valor_busqueda)
        complo(data_input)
        return busqueda_interpolacion(data_input, valor_busqueda)

    def analizar(self, data_input, analysis, valor_busqueda):
        compa(data_input, valor_busqueda, analysis)
        complo(data_input)
        return busqueda_interpolacion_analisis(data_input, valor_busqueda, analysis)


def busqueda_interpolacion(lista, vb):
    n = len(lista)
    izq, der = 0, n - 1

    while lista[izq] < vb < lista[der]:
        indice = izq + (der - izq) * (vb - lista[izq]) // (lista[der] - lista[izq])
        if lista[indice] == vb:
            return indice
        elif lista[indice] < vb:
            izq = indice + 1
        else:
            der = indice - 1

    if lista[izq] == vb:
        return izq
    if lista[der] == vb:
        return der

    raise ex.ValorBusquedaNoEncontrado("No se encontró el valor {0} con búsqueda interpolación".format(vb))


def busqueda_interpolacion_analisis(lista, vb, an):
    an.sum_declaracion(1)
    n = len(lista)

    an.sum_declaracion(2)
    izq, der = 0, n - 1

    while lista[izq] < vb < lista[der]:
        an.sum_co(2)

        an.sum_declaracion(1)
        indice = izq + (der - izq) * (vb - lista[izq]) // (lista[der] - lista[izq])

        if lista[indice] == vb:
            an.sum_co(1)
            return indice
        elif lista[indice] < vb:
            an.sum_co(2)
            an.sum_te(1)
            izq = indice + 1
        else:
            an.sum_co(2)
            an.sum_te(1)
            der = indice - 1

    if lista[izq] == vb:
        an.sum_co(1)
        return izq
    if lista[der] == vb:
        an.sum_co(1)
        return der

    an.sum_co(2)
    raise ex.ValorBusquedaNoEncontrado("No se encontró el valor {0} con búsqueda interpolación".format(vb))
