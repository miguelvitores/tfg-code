import bin.excepciones as ex
from bin.algoritmos.busqueda import Busqueda
from bin.algoritmos.comprobar import comprobar_ejecucion_busqueda as comp
from bin.algoritmos.comprobar import comprobar_analisis_busqueda as compa
from bin.algoritmos.comprobar import comprobar_lista_ordenada_busqueda as complo
import math


class BusquedaSalto(Busqueda):

    def __init__(self):
        super().__init__(2)

    def ejecutar(self, data_input, valor_busqueda):
        comp(data_input, valor_busqueda)
        complo(data_input)
        return busqueda_salto(data_input, valor_busqueda)

    def analizar(self, data_input, analysis, valor_busqueda):
        compa(data_input, valor_busqueda, analysis)
        complo(data_input)
        return busqueda_salto_analisis(data_input, valor_busqueda, analysis)


def busqueda_salto(lista, vb):
    n = len(lista)
    salto = int(math.sqrt(n))
    izq, der = 0, 0
    bloque_encontrado = False

    while izq < n and lista[izq] <= vb:
        der = min(n - 1, izq + salto)
        if lista[izq] <= vb <= lista[der]:
            bloque_encontrado = True
            break
        izq += salto

    if bloque_encontrado:
        for indice in range(izq, der + 1):
            if lista[indice] == vb:
                return indice

    raise ex.ValorBusquedaNoEncontrado("No se encontró el valor {0} con búsqueda salto".format(vb))


def busqueda_salto_analisis(lista, vb, an):
    an.sum_declaracion(1)
    n = len(lista)

    an.sum_declaracion(1)
    salto = int(math.sqrt(n))

    an.sum_declaracion(2)
    izq, der = 0, 0

    an.sum_declaracion(1)
    bloque_encontrado = False

    while izq < n and lista[izq] <= vb:
        an.sum_co(2)

        an.sum_te(1)
        der = min(n - 1, izq + salto)

        an.sum_co(2)
        if lista[izq] <= vb <= lista[der]:
            an.sum_te(1)
            bloque_encontrado = True
            break
        an.sum_te(1)
        izq += salto
    an.sum_co(2)

    an.sum_co(1)
    if bloque_encontrado:
        an.sum_eu(1)
        for indice in range(izq, der + 1):
            an.sum_te(1)
            an.sum_co(1)
            an.sum_co(1)
            if lista[indice] == vb:
                return indice
        an.sum_te(1)
        an.sum_co(1)

    raise ex.ValorBusquedaNoEncontrado("No se encontró el valor {0} con búsqueda salto".format(vb))
