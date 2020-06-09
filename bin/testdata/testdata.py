import abc
import math
import random
from bin.algoritmo import Algoritmo
from bin.analysis import Analysis
from bin.testdata.comprobar import comprobar_rango as compr
from bin.testdata.comprobar import comprobar_repeticiones as comprep
from bin.testdata.rango import RangoTam, RangoVal


class TestData(metaclass=abc.ABCMeta):
    def __init__(self, algoritmo: Algoritmo, rangot: RangoTam, rangov: RangoVal, repet=1):
        self.algoritmo = algoritmo
        comprep(repet)
        self.repet = repet
        compr(rangot, rangov)
        self.rangot = rangot
        self.rangov = rangov
        self.resultados = {}

    def analizar(self):
        """Se analizarán distintas listas con el tamaño en el rango seleccionado. Estas podrán ser
        de varios tipos"""
        suma = self.rangot.tmin
        while suma < self.rangot.tmax + 1:
            n = math.floor(suma)
            an = Analysis()
            lista = self.crear_lista(n)

            for i in range(self.repet):
                r = random.randint(0, n - 1)
                self.algoritmo.analizar(lista, an, lista[r])

            an.media(self.repet)
            self.resultados[n] = an
            suma += self.rangot.prec

    @abc.abstractmethod
    def crear_lista(self, n):
        """Se creará una lista de distinto tipo de tamaño n para analizarla"""
