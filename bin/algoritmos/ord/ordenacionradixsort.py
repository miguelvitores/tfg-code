import math
from bin.algoritmos.ordenacion import Ordenacion
from bin.algoritmos.comprobar import comprobar_ejecucion_ordenacion as comp

base = 10


class OrdenacionRadixsort(Ordenacion):

    def __init__(self):
        super().__init__(6)

    def ejecutar(self, data_input, valor_busqueda=None):
        comp(data_input)
        lista = list(data_input)
        return ordenacion_radixsort(lista)

    def analizar(self, data_input, analysis, valor_busqueda=None):
        pass


def ordenacion_radixsort(ls):
    n = len(ls)
    if n == 1:
        return ls
    digito_base = 1
    res = list(ls)
    valor_maximo = max(ls)

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
