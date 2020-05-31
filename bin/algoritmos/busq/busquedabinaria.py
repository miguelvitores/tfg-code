import bin.excepciones as ex
from bin.algoritmos.busqueda import Busqueda
from bin.algoritmos.comprobar import comprobar_ejecucion_busqueda as comp
from bin.algoritmos.comprobar import comprobar_analisis_busqueda as compa
from bin.algoritmos.comprobar import comprobar_lista_ordenada_busqueda as complo


class BusquedaBinaria(Busqueda):

    def __init__(self):
        super().__init__(1)

    def ejecutar(self, data_input, valor_busqueda):
        comp(data_input, valor_busqueda)
        complo(data_input)
        return busqueda_binaria(data_input, 0, len(data_input)-1, valor_busqueda)

    def analizar(self, data_input, analysis, valor_busqueda):
        compa(data_input, valor_busqueda, analysis)
        complo(data_input)
        return busqueda_binaria_analisis(data_input, 0, len(data_input) - 1, valor_busqueda, analysis)


def busqueda_binaria(lista, minimo, maximo, vb):
    while minimo <= maximo:
        mitad = minimo + (maximo - minimo) // 2
        if lista[mitad] == vb:
            return mitad
        elif lista[mitad] > vb:
            maximo = mitad - 1
        else:
            minimo = mitad + 1
    raise ex.ValorBusquedaNoEncontrado("No se encontró el valor {0} con búsqueda binaria".format(vb))


def busqueda_binaria_analisis(lista, minimo, maximo, vb, an):
    an.sum_eu(2)    # espacio usado por minimo y máximo
    an.sum_eu(1)    # espacio usado por mitad
    while minimo <= maximo:
        an.sum_co(1)

        an.sum_te(1)
        mitad = minimo + (maximo - minimo) // 2

        if lista[mitad] == vb:
            an.sum_co(1)
            return mitad
        elif lista[mitad] > vb:
            an.sum_co(2)
            an.sum_te(1)
            maximo = mitad - 1
        else:
            an.sum_co(2)
            an.sum_te(1)
            minimo = mitad + 1
    an.sum_co(1)

    raise ex.ValorBusquedaNoEncontrado("No se encontró el valor {0} con búsqueda binaria".format(vb))
