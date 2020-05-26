import bin.operaciones_basicas as ob
from bin.algoritmos.ordenacion import Ordenacion
from bin.algoritmos.comprobar import comprobar_ejecucion_ordenacion as comp


class OrdenacionSeleccion(Ordenacion):

    def __init__(self):
        super().__init__(0)

    def ejecutar(self, data_input, valor_busqueda=None):
        comp(data_input)
        lista = list(data_input)
        return ordenacion_seleccion(lista)

    def analizar(self, data_input, analysis, valor_busqueda=None):
        pass


def ordenacion_seleccion(lista):
    n = len(lista)
    for i in range(n - 1):
        minimo = i
        for j in range(i, n):
            if lista[minimo] > lista[j]:
                minimo = j
        if not minimo == i:
            ob.intercambiar(lista, minimo, i)
    return lista
