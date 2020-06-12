import unittest
import random
import bin.excepciones as ex
import bin.testdata.operaciones_rangos as opr

from bin.testdata.td_tipos import TestDataOrdenacionLOEquidistante, TestDataOrdenacionLOACR, TestDataOrdenacionLOASR,\
    TestDataOrdenacionLAleatoria, TestDataOrdenacionLAleatoriaSR

from bin.testdata.rango import RangoVal, RangoTam

from bin.algoritmos.ord.ordenacionseleccion import OrdenacionSeleccion
from bin.algoritmos.ord.ordenacioninsercion import OrdenacionInsercion
from bin.algoritmos.ord.ordenacionburbuja import OrdenacionBurbuja
from bin.algoritmos.ord.ordenacionquicksort import OrdenacionQuicksort
from bin.algoritmos.ord.ordenacionshellsort import OrdenacionShellsort
from bin.algoritmos.ord.ordenacionmergesort import OrdenacionMergesort
from bin.algoritmos.ord.ordenacionradixsort import OrdenacionRadixsort


rangos = (
        (RangoTam(50, 10, 2.7), RangoVal(12, 4, 5)),
        (RangoTam(50, 10, 20), RangoVal(62, 13, 3)),
        (RangoTam(60, 1, 15), RangoVal(4, 0, 7)),
        (RangoTam(160, 48, 4.6), RangoVal(512, 64))
)
N = 4
maxrepe = 8
maxvmin = 32
maxvmax = 444
maxprec = 4
maxtmin = 8
mintmax = 16
maxtmax = 32
maxemax = 6


class ListaOrdenadaEquidistante(unittest.TestCase):

    def test_ordenacion_seleccion_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación seleccion con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        os = OrdenacionSeleccion()
        td = TestDataOrdenacionLOEquidistante(os)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_insercion_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación insercion con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oi = OrdenacionInsercion()
        td = TestDataOrdenacionLOEquidistante(oi)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_burbuja_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación burbuja con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        ob = OrdenacionBurbuja()
        td = TestDataOrdenacionLOEquidistante(ob)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_quicksort_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación quicksort con los rangos por defecto debe devolver unos resultados
         con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oq = OrdenacionQuicksort()
        td = TestDataOrdenacionLOEquidistante(oq)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_shellsort_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación shellsort con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        osh = OrdenacionShellsort()
        td = TestDataOrdenacionLOEquidistante(osh)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_mergesort_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación mergesort con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        om = OrdenacionMergesort()
        td = TestDataOrdenacionLOEquidistante(om)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_radixsort_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación radixsort con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        orx = OrdenacionRadixsort()
        td = TestDataOrdenacionLOEquidistante(orx)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_seleccion_rangos_conocidos(self):
        """El análisis de un testdata de ordenación seleccion con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        os = OrdenacionSeleccion()
        for rt, rv in rangos:
            td = TestDataOrdenacionLOEquidistante(os, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_insercion_rangos_conocidos(self):
        """El análisis de un testdata de ordenación insercion con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oi = OrdenacionInsercion()
        for rt, rv in rangos:
            td = TestDataOrdenacionLOEquidistante(oi, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_burbuja_rangos_conocidos(self):
        """El análisis de un testdata de ordenación burbuja con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        ob = OrdenacionBurbuja()
        for rt, rv in rangos:
            td = TestDataOrdenacionLOEquidistante(ob, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_quicksort_rangos_conocidos(self):
        """El análisis de un testdata de ordenación quicksort con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oq = OrdenacionQuicksort()
        for rt, rv in rangos:
            td = TestDataOrdenacionLOEquidistante(oq, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_shellsort_rangos_conocidos(self):
        """El análisis de un testdata de ordenación shellsort con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        osh = OrdenacionShellsort()
        for rt, rv in rangos:
            td = TestDataOrdenacionLOEquidistante(osh, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_mergesort_rangos_conocidos(self):
        """El análisis de un testdata de ordenación mergesort con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        om = OrdenacionMergesort()
        for rt, rv in rangos:
            td = TestDataOrdenacionLOEquidistante(om, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_radixsort_rangos_conocidos(self):
        """El análisis de un testdata de ordenación radixsort con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        orx = OrdenacionRadixsort()
        for rt, rv in rangos:
            td = TestDataOrdenacionLOEquidistante(orx, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_seleccion_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación seleccion con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        os = OrdenacionSeleccion()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLOEquidistante(os, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_insercion_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación insercion con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oi = OrdenacionInsercion()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLOEquidistante(oi, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_burbuja_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación burbuja con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        ob = OrdenacionBurbuja()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLOEquidistante(ob, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_quicksort_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación quicksort con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oq = OrdenacionQuicksort()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLOEquidistante(oq, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_shellsort_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación shellsort con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        osh = OrdenacionShellsort()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLOEquidistante(osh, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_mergesort_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación mergesort con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        om = OrdenacionMergesort()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLOEquidistante(om, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_radixsort_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación radixsort con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        orx = OrdenacionRadixsort()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLOEquidistante(orx, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)


class ListaOrdenadaAleatoriaConRepeticion(unittest.TestCase):

    def test_ordenacion_seleccion_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación seleccion con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        os = OrdenacionSeleccion()
        td = TestDataOrdenacionLOACR(os)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_insercion_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación insercion con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oi = OrdenacionInsercion()
        td = TestDataOrdenacionLOACR(oi)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_burbuja_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación burbuja con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        ob = OrdenacionBurbuja()
        td = TestDataOrdenacionLOACR(ob)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_quicksort_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación quicksort con los rangos por defecto debe devolver unos resultados
         con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oq = OrdenacionQuicksort()
        td = TestDataOrdenacionLOACR(oq)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_shellsort_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación shellsort con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        osh = OrdenacionShellsort()
        td = TestDataOrdenacionLOACR(osh)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_mergesort_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación mergesort con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        om = OrdenacionMergesort()
        td = TestDataOrdenacionLOACR(om)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_radixsort_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación radixsort con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        orx = OrdenacionRadixsort()
        td = TestDataOrdenacionLOACR(orx)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_seleccion_rangos_conocidos(self):
        """El análisis de un testdata de ordenación seleccion con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        os = OrdenacionSeleccion()
        for rt, rv in rangos:
            td = TestDataOrdenacionLOACR(os, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_insercion_rangos_conocidos(self):
        """El análisis de un testdata de ordenación insercion con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oi = OrdenacionInsercion()
        for rt, rv in rangos:
            td = TestDataOrdenacionLOACR(oi, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_burbuja_rangos_conocidos(self):
        """El análisis de un testdata de ordenación burbuja con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        ob = OrdenacionBurbuja()
        for rt, rv in rangos:
            td = TestDataOrdenacionLOACR(ob, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_quicksort_rangos_conocidos(self):
        """El análisis de un testdata de ordenación quicksort con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oq = OrdenacionQuicksort()
        for rt, rv in rangos:
            td = TestDataOrdenacionLOACR(oq, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_shellsort_rangos_conocidos(self):
        """El análisis de un testdata de ordenación shellsort con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        osh = OrdenacionShellsort()
        for rt, rv in rangos:
            td = TestDataOrdenacionLOACR(osh, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_mergesort_rangos_conocidos(self):
        """El análisis de un testdata de ordenación mergesort con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        om = OrdenacionMergesort()
        for rt, rv in rangos:
            td = TestDataOrdenacionLOACR(om, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_radixsort_rangos_conocidos(self):
        """El análisis de un testdata de ordenación radixsort con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        orx = OrdenacionRadixsort()
        for rt, rv in rangos:
            td = TestDataOrdenacionLOACR(orx, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_seleccion_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación seleccion con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        os = OrdenacionSeleccion()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio_espaciado(maxvmin, maxvmax, maxemax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLOACR(os, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_insercion_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación insercion con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oi = OrdenacionInsercion()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio_espaciado(maxvmin, maxvmax, maxemax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLOACR(oi, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_burbuja_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación burbuja con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        ob = OrdenacionBurbuja()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio_espaciado(maxvmin, maxvmax, maxemax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLOACR(ob, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_quicksort_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación quicksort con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oq = OrdenacionQuicksort()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio_espaciado(maxvmin, maxvmax, maxemax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLOACR(oq, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_shellsort_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación shellsort con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        osh = OrdenacionShellsort()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio_espaciado(maxvmin, maxvmax, maxemax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLOACR(osh, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_mergesort_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación mergesort con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        om = OrdenacionMergesort()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio_espaciado(maxvmin, maxvmax, maxemax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLOACR(om, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_radixsort_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación radixsort con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        orx = OrdenacionRadixsort()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio_espaciado(maxvmin, maxvmax, maxemax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLOACR(orx, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)


class ListaOrdenadaAleatoriaSinRepeticion(unittest.TestCase):

    def test_ordenacion_seleccion_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación seleccion con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        os = OrdenacionSeleccion()
        td = TestDataOrdenacionLOASR(os)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_insercion_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación insercion con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oi = OrdenacionInsercion()
        td = TestDataOrdenacionLOASR(oi)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_burbuja_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación burbuja con los rangos por defecto debe devolver unos resultados con
        un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        ob = OrdenacionBurbuja()
        td = TestDataOrdenacionLOASR(ob)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_quicksort_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación quicksort con los rangos por defecto debe devolver unos resultados
         con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oq = OrdenacionQuicksort()
        td = TestDataOrdenacionLOASR(oq)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_shellsort_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación shellsort con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        osh = OrdenacionShellsort()
        td = TestDataOrdenacionLOASR(osh)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_mergesort_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación mergesort con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        om = OrdenacionMergesort()
        td = TestDataOrdenacionLOASR(om)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_radixsort_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación radixsort con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        orx = OrdenacionRadixsort()
        td = TestDataOrdenacionLOASR(orx)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_seleccion_rangos_conocidos(self):
        """El análisis de un testdata de ordenación seleccion con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        os = OrdenacionSeleccion()
        for rt, rv in rangos:
            td = TestDataOrdenacionLOASR(os, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_insercion_rangos_conocidos(self):
        """El análisis de un testdata de ordenación insercion con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oi = OrdenacionInsercion()
        for rt, rv in rangos:
            td = TestDataOrdenacionLOASR(oi, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_burbuja_rangos_conocidos(self):
        """El análisis de un testdata de ordenación burbuja con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        ob = OrdenacionBurbuja()
        for rt, rv in rangos:
            td = TestDataOrdenacionLOASR(ob, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_quicksort_rangos_conocidos(self):
        """El análisis de un testdata de ordenación quicksort con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oq = OrdenacionQuicksort()
        for rt, rv in rangos:
            td = TestDataOrdenacionLOASR(oq, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_shellsort_rangos_conocidos(self):
        """El análisis de un testdata de ordenación shellsort con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        osh = OrdenacionShellsort()
        for rt, rv in rangos:
            td = TestDataOrdenacionLOASR(osh, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_mergesort_rangos_conocidos(self):
        """El análisis de un testdata de ordenación mergesort con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        om = OrdenacionMergesort()
        for rt, rv in rangos:
            td = TestDataOrdenacionLOASR(om, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_radixsort_rangos_conocidos(self):
        """El análisis de un testdata de ordenación radixsort con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        orx = OrdenacionRadixsort()
        for rt, rv in rangos:
            td = TestDataOrdenacionLOASR(orx, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_seleccion_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación seleccion con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        os = OrdenacionSeleccion()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio_espaciado(maxvmin, maxvmax, maxemax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLOASR(os, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_insercion_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación insercion con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oi = OrdenacionInsercion()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio_espaciado(maxvmin, maxvmax, maxemax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLOASR(oi, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_burbuja_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación burbuja con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        ob = OrdenacionBurbuja()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio_espaciado(maxvmin, maxvmax, maxemax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLOASR(ob, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_quicksort_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación quicksort con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oq = OrdenacionQuicksort()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio_espaciado(maxvmin, maxvmax, maxemax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLOASR(oq, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_shellsort_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación shellsort con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        osh = OrdenacionShellsort()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio_espaciado(maxvmin, maxvmax, maxemax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLOASR(osh, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_mergesort_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación mergesort con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        om = OrdenacionMergesort()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio_espaciado(maxvmin, maxvmax, maxemax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLOASR(om, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_radixsort_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación radixsort con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        orx = OrdenacionRadixsort()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio_espaciado(maxvmin, maxvmax, maxemax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLOASR(orx, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)


class ListaAleatoria(unittest.TestCase):

    def test_ordenacion_seleccion_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación seleccion con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        os = OrdenacionSeleccion()
        td = TestDataOrdenacionLAleatoria(os)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_insercion_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación insercion con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oi = OrdenacionInsercion()
        td = TestDataOrdenacionLAleatoria(oi)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_burbuja_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación burbuja con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        ob = OrdenacionBurbuja()
        td = TestDataOrdenacionLAleatoria(ob)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_quicksort_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación quicksort con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oq = OrdenacionQuicksort()
        td = TestDataOrdenacionLAleatoria(oq)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_shellsort_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación shellsort con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        osh = OrdenacionShellsort()
        td = TestDataOrdenacionLAleatoria(osh)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_mergesort_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación mergesort con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        om = OrdenacionMergesort()
        td = TestDataOrdenacionLAleatoria(om)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_radixsort_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación radixsort con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        orx = OrdenacionRadixsort()
        td = TestDataOrdenacionLAleatoria(orx)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_seleccion_rangos_conocidos(self):
        """El análisis de un testdata de ordenación seleccion con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        os = OrdenacionSeleccion()
        for rt, rv in rangos:
            td = TestDataOrdenacionLAleatoria(os, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_insercion_rangos_conocidos(self):
        """El análisis de un testdata de ordenación insercion con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oi = OrdenacionInsercion()
        for rt, rv in rangos:
            td = TestDataOrdenacionLAleatoria(oi, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_burbuja_rangos_conocidos(self):
        """El análisis de un testdata de ordenación burbuja con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        ob = OrdenacionBurbuja()
        for rt, rv in rangos:
            td = TestDataOrdenacionLAleatoria(ob, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_quicksort_rangos_conocidos(self):
        """El análisis de un testdata de ordenación quicksort con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oq = OrdenacionQuicksort()
        for rt, rv in rangos:
            td = TestDataOrdenacionLAleatoria(oq, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_shellsort_rangos_conocidos(self):
        """El análisis de un testdata de ordenación shellsort con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        osh = OrdenacionShellsort()
        for rt, rv in rangos:
            td = TestDataOrdenacionLAleatoria(osh, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_mergesort_rangos_conocidos(self):
        """El análisis de un testdata de ordenación mergesort con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        om = OrdenacionMergesort()
        for rt, rv in rangos:
            td = TestDataOrdenacionLAleatoria(om, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_radixsort_rangos_conocidos(self):
        """El análisis de un testdata de ordenación radixsort con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        orx = OrdenacionRadixsort()
        for rt, rv in rangos:
            td = TestDataOrdenacionLAleatoria(orx, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_seleccion_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación seleccion con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        os = OrdenacionSeleccion()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLAleatoria(os, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_insercion_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación insercion con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oi = OrdenacionInsercion()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLAleatoria(oi, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_burbuja_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación burbuja con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        ob = OrdenacionBurbuja()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLAleatoria(ob, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_quicksort_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación quicksort con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oq = OrdenacionQuicksort()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLAleatoria(oq, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_shellsort_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación shellsort con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        osh = OrdenacionShellsort()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLAleatoria(osh, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_mergesort_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación mergesort con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        om = OrdenacionMergesort()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLAleatoria(om, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_radixsort_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación radixsort con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        orx = OrdenacionRadixsort()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLAleatoria(orx, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)


class ListaAleatoriaSinRepeticion(unittest.TestCase):

    def test_ordenacion_seleccion_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación seleccion con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        os = OrdenacionSeleccion()
        td = TestDataOrdenacionLAleatoriaSR(os)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_insercion_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación insercion con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oi = OrdenacionInsercion()
        td = TestDataOrdenacionLAleatoriaSR(oi)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_burbuja_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación burbuja con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        ob = OrdenacionBurbuja()
        td = TestDataOrdenacionLAleatoriaSR(ob)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_quicksort_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación quicksort con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oq = OrdenacionQuicksort()
        td = TestDataOrdenacionLAleatoriaSR(oq)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_shellsort_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación shellsort con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        osh = OrdenacionShellsort()
        td = TestDataOrdenacionLAleatoriaSR(osh)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_mergesort_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación mergesort con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        om = OrdenacionMergesort()
        td = TestDataOrdenacionLAleatoriaSR(om)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_radixsort_rangos_por_defecto(self):
        """El análisis de un testdata de ordenación radixsort con los rangos por defecto debe devolver unos resultados
        con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        orx = OrdenacionRadixsort()
        td = TestDataOrdenacionLAleatoriaSR(orx)
        td.analizar()
        self.assertGreater(len(td.resultados), 0)
        self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_seleccion_rangos_conocidos(self):
        """El análisis de un testdata de ordenación seleccion con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        os = OrdenacionSeleccion()
        for rt, rv in rangos:
            td = TestDataOrdenacionLAleatoriaSR(os, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_insercion_rangos_conocidos(self):
        """El análisis de un testdata de ordenación insercion con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oi = OrdenacionInsercion()
        for rt, rv in rangos:
            td = TestDataOrdenacionLAleatoriaSR(oi, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_burbuja_rangos_conocidos(self):
        """El análisis de un testdata de ordenación burbuja con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        ob = OrdenacionBurbuja()
        for rt, rv in rangos:
            td = TestDataOrdenacionLAleatoriaSR(ob, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_quicksort_rangos_conocidos(self):
        """El análisis de un testdata de ordenación quicksort con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oq = OrdenacionQuicksort()
        for rt, rv in rangos:
            td = TestDataOrdenacionLAleatoriaSR(oq, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_shellsort_rangos_conocidos(self):
        """El análisis de un testdata de ordenación shellsort con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        osh = OrdenacionShellsort()
        for rt, rv in rangos:
            td = TestDataOrdenacionLAleatoriaSR(osh, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_mergesort_rangos_conocidos(self):
        """El análisis de un testdata de ordenación mergesort con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        om = OrdenacionMergesort()
        for rt, rv in rangos:
            td = TestDataOrdenacionLAleatoriaSR(om, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_radixsort_rangos_conocidos(self):
        """El análisis de un testdata de ordenación radixsort con una serie de rangos conocidos debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        orx = OrdenacionRadixsort()
        for rt, rv in rangos:
            td = TestDataOrdenacionLAleatoriaSR(orx, rt, rv)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertEqual(len(td.resultados), td.rangot.tam)

    def test_ordenacion_seleccion_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación seleccion con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        os = OrdenacionSeleccion()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLAleatoriaSR(os, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_insercion_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación insercion con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oi = OrdenacionInsercion()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLAleatoriaSR(oi, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_burbuja_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación burbuja con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        ob = OrdenacionBurbuja()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLAleatoriaSR(ob, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_quicksort_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación quicksort con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        oq = OrdenacionQuicksort()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLAleatoriaSR(oq, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_shellsort_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación shellsort con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        osh = OrdenacionShellsort()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLAleatoriaSR(osh, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_mergesort_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación mergesort con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        om = OrdenacionMergesort()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLAleatoriaSR(om, rangot, rangov, nrep)
            td.analizar()
            self.assertGreater(len(td.resultados), 0)
            self.assertTrue(td.rangot.tam <= len(td.resultados) <= td.rangot.tam + 1)

    def test_ordenacion_radixsort_rangos_aleatorios(self):
        """El análisis de un testdata de ordenación radixsort con N rangos y repeticiones aleatorias debe devolver
        unos resultados con un tamaño mayor que 0 e iguales a la variable tam del rangot"""
        orx = OrdenacionRadixsort()
        for i in range(N):
            rangot = opr.rango_tam_aleatorio(maxtmin, mintmax, maxtmax, maxprec)
            rangov = opr.rango_val_aleatorio(maxvmin, maxvmax)
            nrep = random.randint(1, maxrepe)

            td = TestDataOrdenacionLAleatoriaSR(orx, rangot, rangov, nrep)
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

    def test_ordenacion_seleccion_rangos_erroneos(self):
        """El análisis de un testdata de ordenación seleccion debe fallar al recibir rangos erróneos"""
        os = OrdenacionSeleccion()
        for rt, rv in self.rangos_erroneos:
            self.assertRaises(ex.RangoNoValido, TestDataOrdenacionLOASR, os, rt, rv)

    def test_ordenacion_insercion_rangos_erroneos(self):
        """El análisis de un testdata de ordenación insercion debe fallar al recibir rangos erróneos"""
        oi = OrdenacionInsercion()
        for rt, rv in self.rangos_erroneos:
            self.assertRaises(ex.RangoNoValido, TestDataOrdenacionLOASR, oi, rt, rv)

    def test_ordenacion_burbuja_rangos_erroneos(self):
        """El análisis de un testdata de ordenación burbuja debe fallar al recibir rangos erróneos"""
        ob = OrdenacionBurbuja()
        for rt, rv in self.rangos_erroneos:
            self.assertRaises(ex.RangoNoValido, TestDataOrdenacionLOASR, ob, rt, rv)

    def test_ordenacion_quicksort_rangos_erroneos(self):
        """El análisis de un testdata de ordenación quicksort debe fallar al recibir rangos erróneos"""
        oq = OrdenacionQuicksort()
        for rt, rv in self.rangos_erroneos:
            self.assertRaises(ex.RangoNoValido, TestDataOrdenacionLOASR, oq, rt, rv)

    def test_ordenacion_shellsort_rangos_erroneos(self):
        """El análisis de un testdata de ordenación shellsort debe fallar al recibir rangos erróneos"""
        osh = OrdenacionShellsort()
        for rt, rv in self.rangos_erroneos:
            self.assertRaises(ex.RangoNoValido, TestDataOrdenacionLOASR, osh, rt, rv)

    def test_ordenacion_mergesort_rangos_erroneos(self):
        """El análisis de un testdata de ordenación mergesort debe fallar al recibir rangos erróneos"""
        om = OrdenacionMergesort()
        for rt, rv in self.rangos_erroneos:
            self.assertRaises(ex.RangoNoValido, TestDataOrdenacionLOASR, om, rt, rv)

    def test_ordenacion_radixsort_rangos_erroneos(self):
        """El análisis de un testdata de ordenación radixsort debe fallar al recibir rangos erróneos"""
        orx = OrdenacionRadixsort()
        for rt, rv in self.rangos_erroneos:
            self.assertRaises(ex.RangoNoValido, TestDataOrdenacionLOASR, orx, rt, rv)
