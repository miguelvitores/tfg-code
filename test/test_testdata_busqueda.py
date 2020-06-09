import unittest
import random
import bin.excepciones as ex
import bin.testdata.operaciones_rangos as opr

from bin.testdata.td_busq_tipos import BusquedaLOEquidistante, BusquedaLAleatoria, BusquedaLOACR, BusquedaLOASR

from bin.testdata.rango import RangoVal, RangoTam

from bin.algoritmos.busq.busquedalineal import BusquedaLineal
from bin.algoritmos.busq.busquedabinaria import BusquedaBinaria
from bin.algoritmos.busq.busquedasalto import BusquedaSalto
from bin.algoritmos.busq.busquedainterpolacion import BusquedaInterpolacion
from bin.algoritmos.busq.busquedaexponencial import BusquedaExponencial
from bin.algoritmos.busq.busquedafibonacci import BusquedaFibonacci

rangos = (
        (RangoTam(50, 10, 2.7), RangoVal(12, 4)),
        (RangoTam(50, 10, 20), RangoVal(62, 13)),
        (RangoTam(60, 1, 15), RangoVal(4, 0))
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
        for rt, rv in rangos:
            td = BusquedaLOEquidistante(bl, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_binaria_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda binaria con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bb = BusquedaBinaria()
        for rt, rv in rangos:
            td = BusquedaLOEquidistante(bb, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_salto_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda salto con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bs = BusquedaSalto()
        for rt, rv in rangos:
            td = BusquedaLOEquidistante(bs, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_interpolacion_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda interpolacion con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bi = BusquedaInterpolacion()
        for rt, rv in rangos:
            td = BusquedaLOEquidistante(bi, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_exponencial_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda exponencial con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        be = BusquedaExponencial()
        for rt, rv in rangos:
            td = BusquedaLOEquidistante(be, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_fibonacci_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda fibonacci con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bf = BusquedaFibonacci()
        for rt, rv in rangos:
            td = BusquedaLOEquidistante(bf, rt, rv)
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

            td = BusquedaLOEquidistante(bl, rangot, rangov, nrep)
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

            td = BusquedaLOEquidistante(bb, rangot, rangov, nrep)
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

            td = BusquedaLOEquidistante(bs, rangot, rangov, nrep)
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

            td = BusquedaLOEquidistante(bi, rangot, rangov, nrep)
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

            td = BusquedaLOEquidistante(be, rangot, rangov, nrep)
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

            td = BusquedaLOEquidistante(bf, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)


class ListaAleatoria(unittest.TestCase):

    def test_busqueda_lineal_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda lineal con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        td = BusquedaLOEquidistante(bl)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_lineal_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda lineal con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        for rt, rv in rangos:
            td = BusquedaLOEquidistante(bl, rt, rv)
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

            td = BusquedaLAleatoria(bl, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)


class ListaOrdenadaAleatoriaConRepeticion(unittest.TestCase):

    def test_busqueda_lineal_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda lineal con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        td = BusquedaLOACR(bl)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_binaria_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda binaria con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bb = BusquedaBinaria()
        td = BusquedaLOACR(bb)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_salto_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda salto con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bs = BusquedaSalto()
        td = BusquedaLOACR(bs)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_interpolacion_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda interpolacion con los rangos por defecto debe devolver unos resultados
         con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bi = BusquedaInterpolacion()
        td = BusquedaLOACR(bi)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_exponencial_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda exponencial con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        be = BusquedaExponencial()
        td = BusquedaLOACR(be)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_fibonacci_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda fibonacci con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bf = BusquedaFibonacci()
        td = BusquedaLOACR(bf)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_lineal_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda lineal con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        for rt, rv in rangos:
            td = BusquedaLOACR(bl, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_binaria_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda binaria con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bb = BusquedaBinaria()
        for rt, rv in rangos:
            td = BusquedaLOACR(bb, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_salto_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda salto con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bs = BusquedaSalto()
        for rt, rv in rangos:
            td = BusquedaLOACR(bs, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_interpolacion_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda interpolacion con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bi = BusquedaInterpolacion()
        for rt, rv in rangos:
            td = BusquedaLOACR(bi, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_exponencial_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda exponencial con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        be = BusquedaExponencial()
        for rt, rv in rangos:
            td = BusquedaLOACR(be, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_fibonacci_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda fibonacci con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bf = BusquedaFibonacci()
        for rt, rv in rangos:
            td = BusquedaLOACR(bf, rt, rv)
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

            td = BusquedaLOACR(bl, rangot, rangov, nrep)
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

            td = BusquedaLOACR(bb, rangot, rangov, nrep)
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

            td = BusquedaLOACR(bs, rangot, rangov, nrep)
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

            td = BusquedaLOACR(bi, rangot, rangov, nrep)
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

            td = BusquedaLOACR(be, rangot, rangov, nrep)
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

            td = BusquedaLOACR(bf, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)


class ListaOrdenadaAleatoriaSinRepeticion(unittest.TestCase):

    def test_busqueda_lineal_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda lineal con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        td = BusquedaLOASR(bl)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_binaria_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda binaria con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bb = BusquedaBinaria()
        td = BusquedaLOASR(bb)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_salto_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda salto con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bs = BusquedaSalto()
        td = BusquedaLOASR(bs)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_interpolacion_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda interpolacion con los rangos por defecto debe devolver unos resultados
         con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bi = BusquedaInterpolacion()
        td = BusquedaLOASR(bi)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_exponencial_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda exponencial con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        be = BusquedaExponencial()
        td = BusquedaLOASR(be)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_fibonacci_rangos_por_defecto(self):
        """El análisis de un testdata de búsqueda fibonacci con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bf = BusquedaFibonacci()
        td = BusquedaLOASR(bf)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_lineal_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda lineal con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bl = BusquedaLineal()
        for rt, rv in rangos:
            td = BusquedaLOASR(bl, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_binaria_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda binaria con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bb = BusquedaBinaria()
        for rt, rv in rangos:
            td = BusquedaLOASR(bb, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_salto_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda salto con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bs = BusquedaSalto()
        for rt, rv in rangos:
            td = BusquedaLOASR(bs, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_interpolacion_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda interpolacion con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bi = BusquedaInterpolacion()
        for rt, rv in rangos:
            td = BusquedaLOASR(bi, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_exponencial_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda exponencial con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        be = BusquedaExponencial()
        for rt, rv in rangos:
            td = BusquedaLOASR(be, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_busqueda_fibonacci_rangos_conocidos(self):
        """El análisis de un testdata de búsqueda fibonacci con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        bf = BusquedaFibonacci()
        for rt, rv in rangos:
            td = BusquedaLOASR(bf, rt, rv)
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

            td = BusquedaLOASR(bl, rangot, rangov, nrep)
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

            td = BusquedaLOASR(bb, rangot, rangov, nrep)
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

            td = BusquedaLOASR(bs, rangot, rangov, nrep)
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

            td = BusquedaLOASR(bi, rangot, rangov, nrep)
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

            td = BusquedaLOASR(be, rangot, rangov, nrep)
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

            td = BusquedaLOASR(bf, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)
