import bin.excepciones as ex
from bin.algoritmos.busqueda import Busqueda
from bin.algoritmos.comprobar import comprobar_ejecucion_busqueda as comp
from bin.algoritmos.comprobar import comprobar_lista_ordenada_busqueda as complo
import math


class BusquedaFibonacci(Busqueda):

    def __init__(self):
        super().__init__(5)

    def ejecutar(self, data_input, valor_busqueda):
        comp(data_input, valor_busqueda)
        complo(data_input)
        return self.busqueda_fibonacci(data_input, valor_busqueda)

    def analizar(self, data_input, analysis, valor_busqueda):
        pass

    @staticmethod
    def busqueda_fibonacci(lista, vb):
        n = len(lista)
        fbm2 = 0
        fbm1 = 1
        fbm = fbm2 + fbm1
        compensacion = -1

        while fbm < n:
            fbm2 = fbm1
            fbm1 = fbm
            fbm = fbm2 + fbm1

        while fbm > 1:
            i = min(compensacion + fbm2, n - 1)
            if lista[i] < vb:
                fbm = fbm1
                fbm1 = fbm2
                fbm2 = fbm - fbm1
                compensacion = i
            elif lista[i] > vb:
                fbm = fbm2
                fbm1 = fbm1 - fbm
                fbm2 = fbm - fbm1
            else:
                return i

        if lista[0] == vb:
            return 0

        raise ex.ValorBusquedaNoEncontrado("No se encontró el valor {0} con búsqueda fibonacci".format(vb))
