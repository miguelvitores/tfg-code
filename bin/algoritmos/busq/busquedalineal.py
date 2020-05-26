import bin.excepciones as ex
from bin.algoritmos.busqueda import Busqueda
from bin.algoritmos.comprobar import comprobar_ejecucion_busqueda as comp


class BusquedaLineal(Busqueda):

    def __init__(self):
        super().__init__(0)

    def ejecutar(self, data_input, valor_busqueda):
        comp(data_input, valor_busqueda)
        return busqueda_lineal(data_input, valor_busqueda)

    def analizar(self, data_input, analysis, valor_busqueda):
        pass


def busqueda_lineal(lista, vb):
    for i in range(len(lista)):
        if lista[i] == vb:
            return i
    raise ex.ValorBusquedaNoEncontrado("No se encontró el valor {0} con búsqueda lineal".format(valor_busqueda))
