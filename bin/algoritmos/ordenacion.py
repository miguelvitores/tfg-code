import abc
from bin.algoritmo import Algoritmo


class Ordenacion(Algoritmo):

    def __init__(self, nombre):
        super().__init__(1, nombre)

    @abc.abstractmethod
    def ejecutar(self, data_input, valor_busqueda=None):
        """Ejecuta el algoritmo de ordenación para un determinado objeto lista.
        NO se analiza"""

    @abc.abstractmethod
    def analizar(self, data_input, analysis, valor_busqueda=None):
        """Ejecuta el algoritmo de ordenación para un determinado objeto lista.
        SÍ se analiza"""
