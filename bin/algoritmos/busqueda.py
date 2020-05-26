import abc
from bin.algoritmo import Algoritmo


class Busqueda(Algoritmo):

    def __init__(self, nombre):
        super().__init__(0, nombre)

    @abc.abstractmethod
    def ejecutar(self, data_input, valor_busqueda):
        """Ejecuta el algoritmo de búsqueda  para un determinado objeto lista y un valor a buscar.
        NO se analiza"""

    @abc.abstractmethod
    def analizar(self, data_input, analysis, valor_busqueda):
        """Ejecuta el algoritmo de búsqueda  para un determinado objeto lista y un valor a buscar.
        SÍ se analiza"""
