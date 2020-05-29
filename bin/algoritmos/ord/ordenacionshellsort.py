import bin.operaciones_basicas as ob
from bin.algoritmos.ordenacion import Ordenacion
from bin.algoritmos.comprobar import comprobar_ejecucion_ordenacion as comp


class OrdenacionShellsort(Ordenacion):

    def __init__(self):
        super().__init__(4)

    def ejecutar(self, data_input, valor_busqueda=None):
        comp(data_input)
        lista = ob.mezclar_aleatorio(data_input)
        return ordenacion_3xmas1shellsort(lista)

    def analizar(self, data_input, analysis, valor_busqueda=None):
        pass


def ordenacion_3xmas1shellsort(ls):
    n = len(ls)

    h = 1
    while h < n/3:
        h = 3*h + 1

    while h >= 1:
        for i in range(h, n):
            j = i
            while j >= h and ls[j] < ls[j - h]:
                ob.intercambiar(ls, j, j - h)
                j -= 1
        h = h // 3

    return ls
