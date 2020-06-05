import abc
from bin.algoritmo import Algoritmo
from bin.testdata.comprobar import comprobar_rango as compr
from bin.testdata.rango import RangoTam, RangoVal


class TestData(metaclass=abc.ABCMeta):
    def __init__(self, algoritmo: Algoritmo, rangot: RangoTam, rangov: RangoVal):
        self.algoritmo = algoritmo
        compr(rangot, rangov)
        self.rangot = rangot
        self.rangov = rangov
        self.resultados = {}

    @abc.abstractmethod
    def analizar(self):
        """Se analizarán distintas listas con el tamaño en el rango seleccionado. Estas podrán ser
        de varios tipos"""
