import bin.excepciones as ex
from bin.algoritmos.busqueda import Busqueda
from bin.algoritmos.comprobar import comprobar_ejecucion_busqueda as comp
from bin.algoritmos.comprobar import comprobar_analisis_busqueda as compa


class BusquedaLineal(Busqueda):

    def __init__(self):
        super().__init__(0)

    def ejecutar(self, data_input, valor_busqueda):
        comp(data_input, valor_busqueda)
        return busqueda_lineal(data_input, valor_busqueda)

    def analizar(self, data_input, analysis, valor_busqueda):
        compa(data_input, valor_busqueda, analysis)
        return busqueda_lineal_analisis(data_input, valor_busqueda, analysis)


def busqueda_lineal(lista, vb):
    for i in range(len(lista)):
        if lista[i] == vb:
            return i
    raise ex.ValorBusquedaNoEncontrado("No se encontró el valor {0} con búsqueda lineal".format(vb))


def busqueda_lineal_analisis(lista, vb, an):
    an.sum_declaracion(1)
    n = len(lista)

    an.sum_declaracion(1)
    for i in range(n):
        an.sum_co(1)

        an.sum_co(1)
        if lista[i] == vb:
            return i

        an.sum_te(1)
    an.sum_co(1)

    raise ex.ValorBusquedaNoEncontrado("No se encontró el valor {0} con búsqueda lineal".format(vb))
