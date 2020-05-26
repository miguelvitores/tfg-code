import bin.operaciones_basicas as ob
from bin.algoritmos.ordenacion import Ordenacion
from bin.algoritmos.comprobar import comprobar_ejecucion_ordenacion as comp


class OrdenacionBurbuja(Ordenacion):

    def __init__(self):
        super().__init__(0)

    def ejecutar(self, data_input, valor_busqueda=None):
        comp(data_input)
        lista = list(data_input)
        return ordenacion_burbuja(lista)

    def analizar(self, data_input, analysis, valor_busqueda=None):
        pass


def ordenacion_burbuja(lista):
    n = len(lista)
    repetir = True
    while repetir:
        repetir = False
        for i in range(1, n):
            if lista[i - 1] > lista[i]:
                ob.intercambiar(lista, i - 1, i)
                repetir = True
    return lista
