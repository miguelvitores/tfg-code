import bin.excepciones as ex
from bin.algoritmos.busqueda import Busqueda
from bin.algoritmos.comprobar import comprobar_ejecucion_busqueda as comp
from bin.algoritmos.comprobar import comprobar_lista_ordenada_busqueda as complo
from bin.algoritmos.busq.busquedabinaria import BusquedaBinaria


class BusquedaExponencial(Busqueda):

    def __init__(self):
        super().__init__(4)

    def ejecutar(self, data_input, valor_busqueda):
        comp(data_input, valor_busqueda)
        complo(data_input)
        return self.busqueda_exponencial(data_input, valor_busqueda)

    def analizar(self, data_input, analysis, valor_busqueda):
        pass

    @staticmethod
    def busqueda_exponencial(lista, vb):
        n = len(lista)
        if lista[0] == vb:
            return 0
        indice = 1
        while indice < n and lista[indice] <= vb:
            indice = indice * 2
        return BusquedaBinaria.busqueda_binaria(lista, indice // 2, min(indice, n - 1), vb)
