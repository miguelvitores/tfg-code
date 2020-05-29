import bin.operaciones_basicas as ob
from bin.algoritmos.ordenacion import Ordenacion
from bin.algoritmos.comprobar import comprobar_ejecucion_ordenacion as comp


class OrdenacionInsercion(Ordenacion):

    def __init__(self):
        super().__init__(1)

    def ejecutar(self, data_input, valor_busqueda=None):
        comp(data_input)
        lista = list(data_input)
        return ordenacion_insercion(lista, 0, len(lista) - 1)

    def analizar(self, data_input, analysis, valor_busqueda=None):
        pass


def ordenacion_insercion(lista, inicio, fin):
    for i in range(inicio + 1, fin + 1):
        j = i
        while j > inicio:
            if lista[j] < lista[j - 1]:
                ob.intercambiar(lista, j, j - 1)
                j -= 1
            else:
                break
    return lista
