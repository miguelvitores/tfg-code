import bin.excepciones as ex
from bin.algoritmos.busqueda import Busqueda
from bin.algoritmos.comprobar import comprobar_ejecucion_busqueda as comp
from bin.algoritmos.comprobar import comprobar_lista_ordenada_busqueda as complo
import math


class BusquedaSalto(Busqueda):

    def __init__(self):
        super().__init__(2)

    def ejecutar(self, data_input, valor_busqueda):
        comp(data_input, valor_busqueda)
        complo(data_input)
        return self.busqueda_salto(data_input, valor_busqueda)

    def analizar(self, data_input, analysis, valor_busqueda):
        pass

    @staticmethod
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
