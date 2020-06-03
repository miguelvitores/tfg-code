import math
from bin.algoritmos.ordenacion import Ordenacion
from bin.algoritmos.comprobar import comprobar_ejecucion_ordenacion as comp
from bin.algoritmos.comprobar import comprobar_analisis_ordenacion as compa

base = 10


class OrdenacionRadixsort(Ordenacion):

    def __init__(self):
        super().__init__(6)

    def ejecutar(self, data_input, valor_busqueda=None):
        comp(data_input)
        lista = list(data_input)
        return ordenacion_radixsort(lista, max(lista))

    def analizar(self, data_input, analysis, valor_busqueda=None):
        compa(data_input, analysis)
        lista = list(data_input)
        return ordenacion_radixsort_analisis(lista, max(lista), analysis)


def ordenacion_radixsort(ls, valor_maximo):
    n = len(ls)

    if n == 1:
        return ls
    digito_base = 1
    res = list(ls)

    while valor_maximo // digito_base > 0:
        conteo = [0] * base
        for i in range(n):
            clave = (ls[i] // digito_base) % base
            conteo[clave] += 1
        for i in range(1, base):
            conteo[i] += conteo[i - 1]
        for i in range(n):
            clave = (ls[n - 1 - i] // digito_base) % base
            res[conteo[clave] - 1] = ls[n - 1 - i]
            conteo[clave] -= 1
        ls = list(res)
        digito_base *= 10

    return res


def ordenacion_radixsort_analisis(ls, valor_maximo, an):
    an.sum_declaracion(1)
    n = len(ls)

    an.sum_co(1)
    if n == 1:
        return ls

    an.sum_declaracion(len(ls) + 1)
    digito_base = 1
    res = list(ls)

    an.sum_eu(base)     # espacio utilizado por el array conteo
    an.sum_eu(1)        # espacio utilizado por la variable i del for
    while valor_maximo // digito_base > 0:
        an.sum_co(1)

        an.sum_te(base)
        conteo = [0] * base

        an.sum_te(1)
        for i in range(n):
            an.sum_co(1)

            an.sum_te(1)
            clave = (ls[i] // digito_base) % base

            an.sum_in(1)
            conteo[clave] += 1

            an.sum_te(1)
        an.sum_co(1)

        an.sum_te(1)
        for i in range(1, base):
            an.sum_co(1)

            an.sum_in(1)
            conteo[i] += conteo[i - 1]

            an.sum_te(1)
        an.sum_co(1)

        an.sum_te(1)
        for i in range(n):
            an.sum_co(1)

            an.sum_te(1)
            clave = (ls[n - 1 - i] // digito_base) % base

            an.sum_in(1)
            res[conteo[clave] - 1] = ls[n - 1 - i]

            an.sum_in(1)
            conteo[clave] -= 1

            an.sum_te(1)
        an.sum_co(1)

        an.sum_te(len(res) + 1)
        ls = list(res)
        digito_base *= 10
    an.sum_co(1)

    return res
