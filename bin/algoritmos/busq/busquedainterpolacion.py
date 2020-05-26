import bin.excepciones as ex
from bin.algoritmos.busqueda import Busqueda
from bin.algoritmos.comprobar import comprobar_ejecucion_busqueda as comp
from bin.algoritmos.comprobar import comprobar_lista_ordenada_busqueda as complo
import math


class BusquedaInterpolacion(Busqueda):

    def __init__(self):
        super().__init__(3)

    def ejecutar(self, data_input, valor_busqueda):
        comp(data_input, valor_busqueda)
        complo(data_input)
        return self.busqueda_interpolacion(data_input, valor_busqueda)

    def analizar(self, data_input, analysis, valor_busqueda):
        pass

    @staticmethod
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
