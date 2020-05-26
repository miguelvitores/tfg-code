import abc


class Algoritmo(metaclass=abc.ABCMeta):

    def __init__(self, tipo, nombre):
        self.tipo = tipo
        self.nombre = nombre

    @abc.abstractmethod
    def ejecutar(self, data_input, valor_busqueda):
        """Ejecuta el algoritmo de búsqueda u ordenación correspondiente para un determinado objeto lista.
        NO se analiza"""

    @abc.abstractmethod
    def analizar(self, data_input, analysis, valor_busqueda):
        """Ejecuta el algoritmo de búsqueda u ordenación correspondiente para un determinado objeto lista.
        SÍ se analiza"""
