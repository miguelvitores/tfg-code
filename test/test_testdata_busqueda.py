import unittest
import random
import bin.excepciones as ex
import bin.testdata.operaciones_rangos as opr

from bin.testdata.busquedaLOEquidistante import BusquedaLOEquidistante

from bin.testdata.rango import RangoVal, RangoTam

from bin.algoritmos.busq.busquedalineal import BusquedaLineal
from bin.algoritmos.busq.busquedabinaria import BusquedaBinaria
from bin.algoritmos.busq.busquedasalto import BusquedaSalto
from bin.algoritmos.busq.busquedainterpolacion import BusquedaInterpolacion
from bin.algoritmos.busq.busquedaexponencial import BusquedaExponencial
from bin.algoritmos.busq.busquedafibonacci import BusquedaFibonacci


class ListaOrdenadaEquidistante(unittest.TestCase):
    rangos = (
        (RangoTam(50, 10, 2.7), RangoVal(12, 4)),
        (RangoTam(50, 10, 20), RangoVal(62, 13)),
        (RangoTam(60, 1, 15), RangoVal(4, 0))
    )
    N = 20
    maxtmin = 8
    mintmax = 16
    maxtmax = 32
    maxprec = 4
    maxvmin = 32
    maxvmax = 444
    maxrepe = 8

    def test_busqueda_lineal_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda lineal con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        td = BusquedaLOEquidistante(bl)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_binaria_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda binaria con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bb = BusquedaBinaria()
        td = BusquedaLOEquidistante(bb)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_salto_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda salto con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bs = BusquedaSalto()
        td = BusquedaLOEquidistante(bs)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_interpolacion_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda interpolacion con los rangos por defecto debe devolver unos resultados
         con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bi = BusquedaInterpolacion()
        td = BusquedaLOEquidistante(bi)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_exponencial_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda exponencial con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        be = BusquedaExponencial()
        td = BusquedaLOEquidistante(be)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_fibonacci_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda fibonacci con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bf = BusquedaFibonacci()
        td = BusquedaLOEquidistante(bf)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_lineal_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda lineal con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        for rt, rv in self.rangos:
            td = BusquedaLOEquidistante(bl, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_binaria_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda binaria con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bb = BusquedaBinaria()
        for rt, rv in self.rangos:
            td = BusquedaLOEquidistante(bb, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_salto_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda salto con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bs = BusquedaSalto()
        for rt, rv in self.rangos:
            td = BusquedaLOEquidistante(bs, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_interpolacion_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda interpolacion con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bi = BusquedaInterpolacion()
        for rt, rv in self.rangos:
            td = BusquedaLOEquidistante(bi, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_exponencial_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda exponencial con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        be = BusquedaExponencial()
        for rt, rv in self.rangos:
            td = BusquedaLOEquidistante(be, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_fibonacci_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda fibonacci con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bf = BusquedaFibonacci()
        for rt, rv in self.rangos:
            td = BusquedaLOEquidistante(bf, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_lineal_rangos_aleatorios(self):
        """El análisis de un testdata de búsqueda lineal con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        for i in range(self.N):
            rangot = opr.rango_tam_aleatorio(self.maxtmin, self.mintmax, self.maxtmax, self.maxprec)
            rangov = opr.rango_val_aleatorio(self.maxvmin, self.maxvmax)
            nrep = random.randint(1, self.maxrepe)

            td = BusquedaLOEquidistante(bl, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_binaria_rangos_aleatorios(self):
        """El análisis de un testdata de búsqueda binaria con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bb = BusquedaBinaria()
        for i in range(self.N):
            rangot = opr.rango_tam_aleatorio(self.maxtmin, self.mintmax, self.maxtmax, self.maxprec)
            rangov = opr.rango_val_aleatorio(self.maxvmin, self.maxvmax)
            nrep = random.randint(1, self.maxrepe)

            td = BusquedaLOEquidistante(bb, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_salto_rangos_aleatorios(self):
        """El análisis de un testdata de búsqueda salto con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bs = BusquedaSalto()
        for i in range(self.N):
            rangot = opr.rango_tam_aleatorio(self.maxtmin, self.mintmax, self.maxtmax, self.maxprec)
            rangov = opr.rango_val_aleatorio(self.maxvmin, self.maxvmax)
            nrep = random.randint(1, self.maxrepe)

            td = BusquedaLOEquidistante(bs, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_interpolacion_rangos_aleatorios(self):
        """El análisis de un testdata de búsqueda interpolacion con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bi = BusquedaInterpolacion()
        for i in range(self.N):
            rangot = opr.rango_tam_aleatorio(self.maxtmin, self.mintmax, self.maxtmax, self.maxprec)
            rangov = opr.rango_val_aleatorio(self.maxvmin, self.maxvmax)
            nrep = random.randint(1, self.maxrepe)

            td = BusquedaLOEquidistante(bi, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_exponencial_rangos_aleatorios(self):
        """El análisis de un testdata de búsqueda exponencial con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        be = BusquedaExponencial()
        for i in range(self.N):
            rangot = opr.rango_tam_aleatorio(self.maxtmin, self.mintmax, self.maxtmax, self.maxprec)
            rangov = opr.rango_val_aleatorio(self.maxvmin, self.maxvmax)
            nrep = random.randint(1, self.maxrepe)

            td = BusquedaLOEquidistante(be, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_fibonacci_rangos_aleatorios(self):
        """El análisis de un testdata de búsqueda fibonacci con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bf = BusquedaFibonacci()
        for i in range(self.N):
            rangot = opr.rango_tam_aleatorio(self.maxtmin, self.mintmax, self.maxtmax, self.maxprec)
            rangov = opr.rango_val_aleatorio(self.maxvmin, self.maxvmax)
            nrep = random.randint(1, self.maxrepe)

            td = BusquedaLOEquidistante(bf, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)
