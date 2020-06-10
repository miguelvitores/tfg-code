import unittest
import random
import bin.excepciones as ex
import bin.testdata.operaciones_rangos as opr

from bin.testdata.td_tipos import TestDataBusquedaLOEquidistante, TestDataBusquedaLAleatoria, \
    TestDataBusquedaLOACR, TestDataBusquedaLOASR

from bin.testdata.rango import RangoVal, RangoTam

from bin.algoritmos.busq.busquedalineal import BusquedaLineal
from bin.algoritmos.busq.busquedabinaria import BusquedaBinaria
from bin.algoritmos.busq.busquedasalto import BusquedaSalto
from bin.algoritmos.busq.busquedainterpolacion import BusquedaInterpolacion
from bin.algoritmos.busq.busquedaexponencial import BusquedaExponencial
from bin.algoritmos.busq.busquedafibonacci import BusquedaFibonacci

rangos = (
        (RangoTam(50, 10, 2.7), RangoVal(12, 4, 5)),
        (RangoTam(50, 10, 20), RangoVal(62, 13, 3)),
        (RangoTam(60, 1, 15), RangoVal(4, 0, 7))
    )
N = 20
maxrepe = 8
maxvmin = 32
maxvmax = 444
maxprec = 4
maxtmin = 8
mintmax = 16
maxtmax = 32
maxemax = 6


class ListaOrdenadaEquidistante(unittest.TestCase):

    def test_busqueda_lineal_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda lineal con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        td = TestDataBusquedaLOEquidistante(bl)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_binaria_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda binaria con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bb = BusquedaBinaria()
        td = TestDataBusquedaLOEquidistante(bb)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_salto_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda salto con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bs = BusquedaSalto()
        td = TestDataBusquedaLOEquidistante(bs)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_interpolacion_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda interpolacion con los rangos por defecto debe devolver unos resultados
         con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bi = BusquedaInterpolacion()
        td = TestDataBusquedaLOEquidistante(bi)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_exponencial_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda exponencial con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        be = BusquedaExponencial()
        td = TestDataBusquedaLOEquidistante(be)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_fibonacci_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda fibonacci con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bf = BusquedaFibonacci()
        td = TestDataBusquedaLOEquidistante(bf)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_lineal_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda lineal con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        for rt, rv in rangos:
            td = TestDataBusquedaLOEquidistante(bl, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_binaria_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda binaria con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bb = BusquedaBinaria()
        for rt, rv in rangos:
            td = TestDataBusquedaLOEquidistante(bb, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_salto_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda salto con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bs = BusquedaSalto()
        for rt, rv in rangos:
            td = TestDataBusquedaLOEquidistante(bs, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_interpolacion_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda interpolacion con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bi = BusquedaInterpolacion()
        for rt, rv in rangos:
            td = TestDataBusquedaLOEquidistante(bi, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_exponencial_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda exponencial con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        be = BusquedaExponencial()
        for rt, rv in rangos:
            td = TestDataBusquedaLOEquidistante(be, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_fibonacci_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda fibonacci con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bf = BusquedaFibonacci()
        for rt, rv in rangos:
            td = TestDataBusquedaLOEquidistante(bf, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_lineal_rangos_aleatorios(self):
        """El análisis de un testdata de búsqueda lineal con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataBusquedaLOEquidistante(bl, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_busqueda_binaria_rangos_aleatorios(self):
        """El análisis de un testdata de búsqueda binaria con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bb = BusquedaBinaria()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataBusquedaLOEquidistante(bb, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_busqueda_salto_rangos_aleatorios(self):
        """El análisis de un testdata de búsqueda salto con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bs = BusquedaSalto()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataBusquedaLOEquidistante(bs, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_busqueda_interpolacion_rangos_aleatorios(self):
        """El análisis de un testdata de búsqueda interpolacion con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bi = BusquedaInterpolacion()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataBusquedaLOEquidistante(bi, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_busqueda_exponencial_rangos_aleatorios(self):
        """El análisis de un testdata de búsqueda exponencial con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        be = BusquedaExponencial()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataBusquedaLOEquidistante(be, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_busqueda_fibonacci_rangos_aleatorios(self):
        """El análisis de un testdata de búsqueda fibonacci con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bf = BusquedaFibonacci()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataBusquedaLOEquidistante(bf, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)


class ListaOrdenadaAleatoriaConRepeticion(unittest.TestCase):

    def test_busqueda_lineal_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda lineal con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        td = TestDataBusquedaLOACR(bl)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_binaria_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda binaria con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bb = BusquedaBinaria()
        td = TestDataBusquedaLOACR(bb)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_salto_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda salto con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bs = BusquedaSalto()
        td = TestDataBusquedaLOACR(bs)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_interpolacion_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda interpolacion con los rangos por defecto debe devolver unos resultados
         con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bi = BusquedaInterpolacion()
        td = TestDataBusquedaLOACR(bi)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_exponencial_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda exponencial con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        be = BusquedaExponencial()
        td = TestDataBusquedaLOACR(be)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_fibonacci_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda fibonacci con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bf = BusquedaFibonacci()
        td = TestDataBusquedaLOACR(bf)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_lineal_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda lineal con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        for rt, rv in rangos:
            td = TestDataBusquedaLOACR(bl, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_binaria_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda binaria con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bb = BusquedaBinaria()
        for rt, rv in rangos:
            td = TestDataBusquedaLOACR(bb, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_salto_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda salto con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bs = BusquedaSalto()
        for rt, rv in rangos:
            td = TestDataBusquedaLOACR(bs, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_interpolacion_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda interpolacion con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bi = BusquedaInterpolacion()
        for rt, rv in rangos:
            td = TestDataBusquedaLOACR(bi, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_exponencial_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda exponencial con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        be = BusquedaExponencial()
        for rt, rv in rangos:
            td = TestDataBusquedaLOACR(be, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_fibonacci_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda fibonacci con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bf = BusquedaFibonacci()
        for rt, rv in rangos:
            td = TestDataBusquedaLOACR(bf, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_lineal_rangos_aleatorios(self):
        """El análisis de un testdata de búsqueda lineal con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio_espaciado(maxvmin, maxvmax, maxemax)
            nrep = random.randint(1, maxrepe)

            td = TestDataBusquedaLOACR(bl, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_busqueda_binaria_rangos_aleatorios(self):
        """El análisis de un testdata de búsqueda binaria con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bb = BusquedaBinaria()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio_espaciado(maxvmin, maxvmax, maxemax)
            nrep = random.randint(1, maxrepe)

            td = TestDataBusquedaLOACR(bb, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_busqueda_salto_rangos_aleatorios(self):
        """El análisis de un testdata de búsqueda salto con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bs = BusquedaSalto()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio_espaciado(maxvmin, maxvmax, maxemax)
            nrep = random.randint(1, maxrepe)

            td = TestDataBusquedaLOACR(bs, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_busqueda_interpolacion_rangos_aleatorios(self):
        """El análisis de un testdata de búsqueda interpolacion con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bi = BusquedaInterpolacion()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio_espaciado(maxvmin, maxvmax, maxemax)
            nrep = random.randint(1, maxrepe)

            td = TestDataBusquedaLOACR(bi, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_busqueda_exponencial_rangos_aleatorios(self):
        """El análisis de un testdata de búsqueda exponencial con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        be = BusquedaExponencial()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio_espaciado(maxvmin, maxvmax, maxemax)
            nrep = random.randint(1, maxrepe)

            td = TestDataBusquedaLOACR(be, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_busqueda_fibonacci_rangos_aleatorios(self):
        """El análisis de un testdata de búsqueda fibonacci con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bf = BusquedaFibonacci()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio_espaciado(maxvmin, maxvmax, maxemax)
            nrep = random.randint(1, maxrepe)

            td = TestDataBusquedaLOACR(bf, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)


class ListaOrdenadaAleatoriaSinRepeticion(unittest.TestCase):

    def test_busqueda_lineal_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda lineal con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        td = TestDataBusquedaLOASR(bl)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_binaria_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda binaria con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bb = BusquedaBinaria()
        td = TestDataBusquedaLOASR(bb)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_salto_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda salto con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bs = BusquedaSalto()
        td = TestDataBusquedaLOASR(bs)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_interpolacion_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda interpolacion con los rangos por defecto debe devolver unos resultados
         con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bi = BusquedaInterpolacion()
        td = TestDataBusquedaLOASR(bi)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_exponencial_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda exponencial con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        be = BusquedaExponencial()
        td = TestDataBusquedaLOASR(be)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_fibonacci_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda fibonacci con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bf = BusquedaFibonacci()
        td = TestDataBusquedaLOASR(bf)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_lineal_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda lineal con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        for rt, rv in rangos:
            td = TestDataBusquedaLOASR(bl, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_binaria_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda binaria con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bb = BusquedaBinaria()
        for rt, rv in rangos:
            td = TestDataBusquedaLOASR(bb, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_salto_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda salto con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bs = BusquedaSalto()
        for rt, rv in rangos:
            td = TestDataBusquedaLOASR(bs, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_interpolacion_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda interpolacion con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bi = BusquedaInterpolacion()
        for rt, rv in rangos:
            td = TestDataBusquedaLOASR(bi, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_exponencial_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda exponencial con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        be = BusquedaExponencial()
        for rt, rv in rangos:
            td = TestDataBusquedaLOASR(be, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_fibonacci_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda fibonacci con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bf = BusquedaFibonacci()
        for rt, rv in rangos:
            td = TestDataBusquedaLOASR(bf, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_lineal_rangos_aleatorios(self):
        """El análisis de un testdata de búsqueda lineal con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio_espaciado(maxvmin, maxvmax, maxemax)
            nrep = random.randint(1, maxrepe)

            td = TestDataBusquedaLOASR(bl, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_busqueda_binaria_rangos_aleatorios(self):
        """El análisis de un testdata de búsqueda binaria con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bb = BusquedaBinaria()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio_espaciado(maxvmin, maxvmax, maxemax)
            nrep = random.randint(1, maxrepe)

            td = TestDataBusquedaLOASR(bb, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_busqueda_salto_rangos_aleatorios(self):
        """El análisis de un testdata de búsqueda salto con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bs = BusquedaSalto()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio_espaciado(maxvmin, maxvmax, maxemax)
            nrep = random.randint(1, maxrepe)

            td = TestDataBusquedaLOASR(bs, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_busqueda_interpolacion_rangos_aleatorios(self):
        """El análisis de un testdata de búsqueda interpolacion con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bi = BusquedaInterpolacion()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio_espaciado(maxvmin, maxvmax, maxemax)
            nrep = random.randint(1, maxrepe)

            td = TestDataBusquedaLOASR(bi, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_busqueda_exponencial_rangos_aleatorios(self):
        """El análisis de un testdata de búsqueda exponencial con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        be = BusquedaExponencial()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio_espaciado(maxvmin, maxvmax, maxemax)
            nrep = random.randint(1, maxrepe)

            td = TestDataBusquedaLOASR(be, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_busqueda_fibonacci_rangos_aleatorios(self):
        """El análisis de un testdata de búsqueda fibonacci con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bf = BusquedaFibonacci()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio_espaciado(maxvmin, maxvmax, maxemax)
            nrep = random.randint(1, maxrepe)

            td = TestDataBusquedaLOASR(bf, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)


class ListaAleatoria(unittest.TestCase):

    def test_busqueda_lineal_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda lineal con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        td = TestDataBusquedaLAleatoria(bl)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_lineal_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda lineal con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        for rt, rv in rangos:
            td = TestDataBusquedaLAleatoria(bl, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_lineal_rangos_aleatorios(self):
        """El análisis de un testdata de búsqueda lineal con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataBusquedaLAleatoria(bl, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)


class EntradasErroneas(unittest.TestCase):
    rangos_erroneos = (
        (RangoTam(5, 10, 2.7), RangoVal(12, 4, 5)),
        (RangoTam(50, 10, -20), RangoVal(62, 13, 3)),
        (RangoTam(1, 0, 15), RangoVal(4, 0, 7)),
        (RangoTam(1, 1, 5), RangoVal(4, 0, 7)),
        (RangoTam(50, 10, 5), RangoVal(5, 10, 3)),
        (RangoTam(50, 10, 5), RangoVal(15, -1, 3))
    )
    num_rep = (
        0,
        -1,
        65,
        152,
        -54
    )
    rangot_pd = RangoTam(32)
    rangov_pd = RangoVal(16)

    def test_busqueda_lineal_rangos_erroneos(self):
        """El análisis de un testdata de búsqueda lineal debe fallar al recibir rangos erróneos"""
        bl = BusquedaLineal()
        for rt, rv in self.rangos_erroneos:
            self.assertRaises(ex.RangoNoValido, TestDataBusquedaLOASR, bl, rt, rv)

    def test_busqueda_binaria_rangos_erroneos(self):
        """El análisis de un testdata de búsqueda binaria debe fallar al recibir rangos erróneos"""
        bb = BusquedaBinaria()
        for rt, rv in self.rangos_erroneos:
            self.assertRaises(ex.RangoNoValido, TestDataBusquedaLOASR, bb, rt, rv)

    def test_busqueda_salto_rangos_erroneos(self):
        """El análisis de un testdata de búsqueda salto debe fallar al recibir rangos erróneos"""
        bs = BusquedaSalto()
        for rt, rv in self.rangos_erroneos:
            self.assertRaises(ex.RangoNoValido, TestDataBusquedaLOASR, bs, rt, rv)

    def test_busqueda_interpolacion_rangos_erroneos(self):
        """El análisis de un testdata de búsqueda interpolacion debe fallar al recibir rangos erróneos"""
        bi = BusquedaInterpolacion()
        for rt, rv in self.rangos_erroneos:
            self.assertRaises(ex.RangoNoValido, TestDataBusquedaLOASR, bi, rt, rv)

    def test_busqueda_exponencial_rangos_erroneos(self):
        """El análisis de un testdata de búsqueda exponencial debe fallar al recibir rangos erróneos"""
        be = BusquedaExponencial()
        for rt, rv in self.rangos_erroneos:
            self.assertRaises(ex.RangoNoValido, TestDataBusquedaLOASR, be, rt, rv)

    def test_busqueda_fibonacci_rangos_erroneos(self):
        """El análisis de un testdata de búsqueda fibonacci debe fallar al recibir rangos erróneos"""
        bf = BusquedaFibonacci()
        for rt, rv in self.rangos_erroneos:
            self.assertRaises(ex.RangoNoValido, TestDataBusquedaLOASR, bf, rt, rv)
