import unittest
import random
import bin.excepciones as ex
import bin.testdata.operaciones_rangos as opr

from bin.testdata.td_tipos import TestDataLOEquidistante, TestDataLAleatoria, TestDataLOACR, TestDataLOASR

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
        td = TestDataLOEquidistante(bl)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_binaria_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda binaria con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bb = BusquedaBinaria()
        td = TestDataLOEquidistante(bb)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_salto_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda salto con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bs = BusquedaSalto()
        td = TestDataLOEquidistante(bs)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_interpolacion_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda interpolacion con los rangos por defecto debe devolver unos resultados
         con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bi = BusquedaInterpolacion()
        td = TestDataLOEquidistante(bi)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_exponencial_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda exponencial con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        be = BusquedaExponencial()
        td = TestDataLOEquidistante(be)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_fibonacci_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda fibonacci con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bf = BusquedaFibonacci()
        td = TestDataLOEquidistante(bf)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_lineal_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda lineal con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        for rt, rv in rangos:
            td = TestDataLOEquidistante(bl, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_binaria_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda binaria con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bb = BusquedaBinaria()
        for rt, rv in rangos:
            td = TestDataLOEquidistante(bb, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_salto_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda salto con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bs = BusquedaSalto()
        for rt, rv in rangos:
            td = TestDataLOEquidistante(bs, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_interpolacion_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda interpolacion con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bi = BusquedaInterpolacion()
        for rt, rv in rangos:
            td = TestDataLOEquidistante(bi, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_exponencial_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda exponencial con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        be = BusquedaExponencial()
        for rt, rv in rangos:
            td = TestDataLOEquidistante(be, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_fibonacci_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda fibonacci con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bf = BusquedaFibonacci()
        for rt, rv in rangos:
            td = TestDataLOEquidistante(bf, rt, rv)
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

            td = TestDataLOEquidistante(bl, rangot, rangov, nrep)
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

            td = TestDataLOEquidistante(bb, rangot, rangov, nrep)
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

            td = TestDataLOEquidistante(bs, rangot, rangov, nrep)
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

            td = TestDataLOEquidistante(bi, rangot, rangov, nrep)
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

            td = TestDataLOEquidistante(be, rangot, rangov, nrep)
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

            td = TestDataLOEquidistante(bf, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)


class ListaAleatoria(unittest.TestCase):

    def test_busqueda_lineal_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda lineal con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        td = TestDataLAleatoria(bl)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_lineal_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda lineal con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        for rt, rv in rangos:
            td = TestDataLAleatoria(bl, rt, rv)
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

            td = TestDataLAleatoria(bl, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)


class ListaOrdenadaAleatoriaConRepeticion(unittest.TestCase):

    def test_busqueda_lineal_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda lineal con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        td = TestDataLOACR(bl)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_binaria_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda binaria con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bb = BusquedaBinaria()
        td = TestDataLOACR(bb)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_salto_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda salto con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bs = BusquedaSalto()
        td = TestDataLOACR(bs)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_interpolacion_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda interpolacion con los rangos por defecto debe devolver unos resultados
         con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bi = BusquedaInterpolacion()
        td = TestDataLOACR(bi)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_exponencial_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda exponencial con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        be = BusquedaExponencial()
        td = TestDataLOACR(be)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_fibonacci_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda fibonacci con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bf = BusquedaFibonacci()
        td = TestDataLOACR(bf)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_lineal_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda lineal con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        for rt, rv in rangos:
            td = TestDataLOACR(bl, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_binaria_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda binaria con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bb = BusquedaBinaria()
        for rt, rv in rangos:
            td = TestDataLOACR(bb, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_salto_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda salto con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bs = BusquedaSalto()
        for rt, rv in rangos:
            td = TestDataLOACR(bs, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_interpolacion_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda interpolacion con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bi = BusquedaInterpolacion()
        for rt, rv in rangos:
            td = TestDataLOACR(bi, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_exponencial_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda exponencial con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        be = BusquedaExponencial()
        for rt, rv in rangos:
            td = TestDataLOACR(be, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_fibonacci_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda fibonacci con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bf = BusquedaFibonacci()
        for rt, rv in rangos:
            td = TestDataLOACR(bf, rt, rv)
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

            td = TestDataLOACR(bl, rangot, rangov, nrep)
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

            td = TestDataLOACR(bb, rangot, rangov, nrep)
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

            td = TestDataLOACR(bs, rangot, rangov, nrep)
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

            td = TestDataLOACR(bi, rangot, rangov, nrep)
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

            td = TestDataLOACR(be, rangot, rangov, nrep)
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

            td = TestDataLOACR(bf, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)


class ListaOrdenadaAleatoriaSinRepeticion(unittest.TestCase):

    def test_busqueda_lineal_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda lineal con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        td = TestDataLOASR(bl)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_binaria_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda binaria con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bb = BusquedaBinaria()
        td = TestDataLOASR(bb)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_salto_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda salto con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bs = BusquedaSalto()
        td = TestDataLOASR(bs)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_interpolacion_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda interpolacion con los rangos por defecto debe devolver unos resultados
         con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bi = BusquedaInterpolacion()
        td = TestDataLOASR(bi)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_exponencial_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda exponencial con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        be = BusquedaExponencial()
        td = TestDataLOASR(be)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_fibonacci_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda fibonacci con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bf = BusquedaFibonacci()
        td = TestDataLOASR(bf)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_lineal_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda lineal con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        for rt, rv in rangos:
            td = TestDataLOASR(bl, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_binaria_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda binaria con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bb = BusquedaBinaria()
        for rt, rv in rangos:
            td = TestDataLOASR(bb, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_salto_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda salto con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bs = BusquedaSalto()
        for rt, rv in rangos:
            td = TestDataLOASR(bs, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_interpolacion_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda interpolacion con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bi = BusquedaInterpolacion()
        for rt, rv in rangos:
            td = TestDataLOASR(bi, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_exponencial_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda exponencial con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        be = BusquedaExponencial()
        for rt, rv in rangos:
            td = TestDataLOASR(be, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_fibonacci_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda fibonacci con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bf = BusquedaFibonacci()
        for rt, rv in rangos:
            td = TestDataLOASR(bf, rt, rv)
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

            td = TestDataLOASR(bl, rangot, rangov, nrep)
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

            td = TestDataLOASR(bb, rangot, rangov, nrep)
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

            td = TestDataLOASR(bs, rangot, rangov, nrep)
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

            td = TestDataLOASR(bi, rangot, rangov, nrep)
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

            td = TestDataLOASR(be, rangot, rangov, nrep)
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

            td = TestDataLOASR(bf, rangot, rangov, nrep)
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
            self.assertRaises(ex.RangoNoValido, TestDataLOASR, bl, rt, rv)

    def test_busqueda_binaria_rangos_erroneos(self):
        """El análisis de un testdata de búsqueda binaria debe fallar al recibir rangos erróneos"""
        bb = BusquedaBinaria()
        for rt, rv in self.rangos_erroneos:
            self.assertRaises(ex.RangoNoValido, TestDataLOASR, bb, rt, rv)

    def test_busqueda_salto_rangos_erroneos(self):
        """El análisis de un testdata de búsqueda salto debe fallar al recibir rangos erróneos"""
        bs = BusquedaSalto()
        for rt, rv in self.rangos_erroneos:
            self.assertRaises(ex.RangoNoValido, TestDataLOASR, bs, rt, rv)

    def test_busqueda_interpolacion_rangos_erroneos(self):
        """El análisis de un testdata de búsqueda interpolacion debe fallar al recibir rangos erróneos"""
        bi = BusquedaInterpolacion()
        for rt, rv in self.rangos_erroneos:
            self.assertRaises(ex.RangoNoValido, TestDataLOASR, bi, rt, rv)

    def test_busqueda_exponencial_rangos_erroneos(self):
        """El análisis de un testdata de búsqueda exponencial debe fallar al recibir rangos erróneos"""
        be = BusquedaExponencial()
        for rt, rv in self.rangos_erroneos:
            self.assertRaises(ex.RangoNoValido, TestDataLOASR, be, rt, rv)

    def test_busqueda_fibonacci_rangos_erroneos(self):
        """El análisis de un testdata de búsqueda fibonacci debe fallar al recibir rangos erróneos"""
        bf = BusquedaFibonacci()
        for rt, rv in self.rangos_erroneos:
            self.assertRaises(ex.RangoNoValido, TestDataLOASR, bf, rt, rv)
