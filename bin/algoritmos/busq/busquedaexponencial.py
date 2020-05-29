import bin.excepciones as ex
from bin.algoritmos.busqueda import Busqueda
from bin.algoritmos.comprobar import comprobar_ejecucion_busqueda as comp
from bin.algoritmos.comprobar import comprobar_analisis_busqueda as compa
from bin.algoritmos.comprobar import comprobar_lista_ordenada_busqueda as complo
import bin.algoritmos.busq.busquedabinaria as bb


class BusquedaExponencial(Busqueda):

    def __init__(self):
        super().__init__(4)

    def ejecutar(self, data_input, valor_busqueda):
        comp(data_input, valor_busqueda)
        complo(data_input)
        return busqueda_exponencial(data_input, valor_busqueda)

    def analizar(self, data_input, analysis, valor_busqueda):
        compa(data_input, valor_busqueda, analysis)
        complo(data_input)
        return busqueda_exponencial_analisis(data_input, valor_busqueda, analysis)


def busqueda_exponencial(lista, vb):
    n = len(lista)
    if lista[0] == vb:
        return 0
    indice = 1
    while indice < n and lista[indice] <= vb:
        indice = indice * 2
    return bb.busqueda_binaria(lista, indice // 2, min(indice, n - 1), vb)


def busqueda_exponencial_analisis(lista, vb, an):
    an.sum_declaracion(1)
    n = len(lista)

    an.sum_co(1)
    if lista[0] == vb:
        return 0

    an.sum_declaracion(1)
    indice = 1

    while indice < n and lista[indice] <= vb:
        an.sum_co(2)
        an.sum_te(1)
        indice = indice * 2
    an.sum_co(2)

    return bb.busqueda_binaria_analisis(lista, indice // 2, min(indice, n - 1), vb, an)
