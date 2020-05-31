import unittest
import bin.crear_lista as cl
import bin.excepciones as ex
from bin.algoritmos.ord.ordenacionseleccion import OrdenacionSeleccion
from bin.algoritmos.ord.ordenacioninsercion import OrdenacionInsercion
from bin.algoritmos.ord.ordenacionburbuja import OrdenacionBurbuja
from bin.algoritmos.ord.ordenacionquicksort import OrdenacionQuicksort
from bin.algoritmos.ord.ordenacionshellsort import OrdenacionShellsort
from bin.algoritmos.ord.ordenacionmergesort import OrdenacionMergesort
from bin.algoritmos.ord.ordenacionradixsort import OrdenacionRadixsort
from bin.analysis import Analysis

tam = 32
min_num = 8
max_num = 16


class ValoresConocidos(unittest.TestCase):
    lista_desordenada = (
        5,
        8,
        1,
        2,
        9,
        0,
        7,
        4,
        3,
        6
    )
    lista_casi_ordenada = (
        0,
        1,
        2,
        4,
        3,
        5,
        6,
        7,
        8,
        9
    )
    lo1 = [7]
    lista_ordenada = sorted(list(lista_desordenada))
    lo1_ordenada = [7]

    def test_analisis_ordenacion_seleccion(self):
        """El analisis del algoritmo de ordenación selección debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        os = OrdenacionSeleccion()
        an = Analysis()
        res = os.analizar(self.lista_desordenada, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_insercion(self):
        """El analisis del algoritmo de ordenación inserción debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        oi = OrdenacionInsercion()
        an = Analysis()
        res = oi.analizar(self.lista_desordenada, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_burbuja(self):
        """El analisis del algoritmo de ordenación burbuja debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        ob = OrdenacionBurbuja()
        an = Analysis()
        res = ob.analizar(self.lista_desordenada, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_quicksort(self):
        """El analisis del algoritmo de ordenación quicksort debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        oq = OrdenacionQuicksort()
        an = Analysis()
        res = oq.analizar(self.lista_desordenada, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_shellsort(self):
        """El analisis del algoritmo de ordenación shellsort debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        osh = OrdenacionShellsort()
        an = Analysis()
        res = osh.analizar(self.lista_desordenada, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_mergesort(self):
        """El analisis del algoritmo de ordenación mergesort debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        om = OrdenacionMergesort()
        an = Analysis()
        res = om.analizar(self.lista_desordenada, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_radixsort(self):
        """El analisis del algoritmo de ordenación radixsort debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        orx = OrdenacionRadixsort()
        an = Analysis()
        res = orx.analizar(self.lista_desordenada, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado_sin_comparaciones(), False)

    def test_analisis_ordenacion_seleccion_un_elemento(self):
        """El analisis del algoritmo de ordenación selección debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida con un solo elemento. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        os = OrdenacionSeleccion()
        an = Analysis()
        res = os.analizar(self.lo1, an)
        self.assertListEqual(self.lo1_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_insercion_un_elemento(self):
        """El analisis del algoritmo de ordenación inserción debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida con un solo elemento. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        oi = OrdenacionInsercion()
        an = Analysis()
        res = oi.analizar(self.lo1, an)
        self.assertListEqual(self.lo1_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_burbuja_un_elemento(self):
        """El analisis del algoritmo de ordenación burbuja debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida con un solo elemento. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        ob = OrdenacionBurbuja()
        an = Analysis()
        res = ob.analizar(self.lo1, an)
        self.assertListEqual(self.lo1_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_quicksort_un_elemento(self):
        """El analisis del algoritmo de ordenación quicksort debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida con un solo elemento. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        oq = OrdenacionQuicksort()
        an = Analysis()
        res = oq.analizar(self.lo1, an)
        self.assertListEqual(self.lo1_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_shellsort_un_elemento(self):
        """El analisis del algoritmo de ordenación shellsort debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida con un solo elemento. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        osh = OrdenacionShellsort()
        an = Analysis()
        res = osh.analizar(self.lo1, an)
        self.assertListEqual(self.lo1_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_mergesort_un_elemento(self):
        """El analisis del algoritmo de ordenación mergesort debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida con un solo elemento. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        om = OrdenacionMergesort()
        an = Analysis()
        res = om.analizar(self.lo1, an)
        self.assertListEqual(self.lo1_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_radixsort_un_elemento(self):
        """El analisis del algoritmo de ordenación radixsort debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida con un solo elemento. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        orx = OrdenacionRadixsort()
        an = Analysis()
        res = orx.analizar(self.lo1, an)
        self.assertListEqual(self.lo1_ordenada, res)
        self.assertIs(an.inicializado_sin_comparaciones(), False)

    def test_analisis_ordenacion_seleccion_casi_ordenada(self):
        """El analisis del algoritmo de ordenación selección debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida casi ordenada. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        os = OrdenacionSeleccion()
        an = Analysis()
        res = os.analizar(self.lista_casi_ordenada, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_insercion_casi_ordenada(self):
        """El analisis del algoritmo de ordenación inserción debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida casi ordenada. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        oi = OrdenacionInsercion()
        an = Analysis()
        res = oi.analizar(self.lista_casi_ordenada, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_burbuja_casi_ordenada(self):
        """El analisis del algoritmo de ordenación burbuja debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida casi ordenada. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        ob = OrdenacionBurbuja()
        an = Analysis()
        res = ob.analizar(self.lista_casi_ordenada, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_quicksort_casi_ordenada(self):
        """El analisis del algoritmo de ordenación quicksort debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida casi ordenada. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        oq = OrdenacionQuicksort()
        an = Analysis()
        res = oq.analizar(self.lista_casi_ordenada, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_shellsort_casi_ordenada(self):
        """El analisis del algoritmo de ordenación shellsort debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida casi ordenada. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        osh = OrdenacionShellsort()
        an = Analysis()
        res = osh.analizar(self.lista_casi_ordenada, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_mergesort_casi_ordenada(self):
        """El analisis del algoritmo de ordenación mergesort debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida casi ordenada. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        om = OrdenacionMergesort()
        an = Analysis()
        res = om.analizar(self.lista_casi_ordenada, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_radixsort_casi_ordenada(self):
        """El analisis del algoritmo de ordenación radixsort debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida casi ordenada. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        orx = OrdenacionRadixsort()
        an = Analysis()
        res = orx.analizar(self.lista_casi_ordenada, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado_sin_comparaciones(), False)


class ListaAleatoriaSinRepeticion(unittest.TestCase):
    la_sr = cl.aleatoria_sin_repeticion(min_num, min_num + tam)
    lista_ordenada = sorted(list(la_sr))

    def test_analisis_ordenacion_seleccion(self):
        """El analisis del algoritmo de ordenación selección debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria sin repetición. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        os = OrdenacionSeleccion()
        an = Analysis()
        res = os.analizar(self.la_sr, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_insercion(self):
        """El analisis del algoritmo de ordenación selección debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria sin repetición. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        oi = OrdenacionInsercion()
        an = Analysis()
        res = oi.analizar(self.la_sr, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_burbuja(self):
        """El analisis del algoritmo de ordenación burbuja debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria sin repetición. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        ob = OrdenacionBurbuja()
        an = Analysis()
        res = ob.analizar(self.la_sr, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_quicksort(self):
        """El analisis del algoritmo de ordenación quicksort debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria sin repetición. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        oq = OrdenacionQuicksort()
        an = Analysis()
        res = oq.analizar(self.la_sr, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_shellsort(self):
        """El analisis del algoritmo de ordenación shellsort debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria sin repetición. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        osh = OrdenacionShellsort()
        an = Analysis()
        res = osh.analizar(self.la_sr, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_mergesort(self):
        """El analisis del algoritmo de ordenación mergesort debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria sin repetición. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        om = OrdenacionMergesort()
        an = Analysis()
        res = om.analizar(self.la_sr, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_radixsort(self):
        """El analisis del algoritmo de ordenación radixsort debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria sin repetición. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        orx = OrdenacionRadixsort()
        an = Analysis()
        res = orx.analizar(self.la_sr, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado_sin_comparaciones(), False)


class ListaAleatoriaConRepeticion(unittest.TestCase):
    la_cr = cl.aleatoria(min_num, max_num, tam)
    lista_ordenada = sorted(list(la_cr))

    def test_analisis_ordenacion_seleccion(self):
        """El analisis del algoritmo de ordenación selección debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria con repetición. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        os = OrdenacionSeleccion()
        an = Analysis()
        res = os.analizar(self.la_cr, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_insercion(self):
        """El analisis del algoritmo de ordenación inserción debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria con repetición. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        oi = OrdenacionInsercion()
        an = Analysis()
        res = oi.analizar(self.la_cr, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_burbuja(self):
        """El analisis del algoritmo de ordenación burbuja debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria con repetición. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        ob = OrdenacionBurbuja()
        an = Analysis()
        res = ob.analizar(self.la_cr, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_quicksort(self):
        """El analisis del algoritmo de ordenación quicksort debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria con repetición. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        oq = OrdenacionQuicksort()
        an = Analysis()
        res = oq.analizar(self.la_cr, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_shellsort(self):
        """El analisis del algoritmo de ordenación shellsort debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria con repetición. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        osh = OrdenacionShellsort()
        an = Analysis()
        res = osh.analizar(self.la_cr, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_mergesort(self):
        """El analisis del algoritmo de ordenación mergesort debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria con repetición. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        om = OrdenacionMergesort()
        an = Analysis()
        res = om.analizar(self.la_cr, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_radixsort(self):
        """El analisis del algoritmo de ordenación radixsort debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria con repetición. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        orx = OrdenacionRadixsort()
        an = Analysis()
        res = orx.analizar(self.la_cr, an)
        self.assertListEqual(self.lista_ordenada, res)
        self.assertIs(an.inicializado_sin_comparaciones(), False)


class ListaYaOrdenada(unittest.TestCase):
    lo = cl.ordenada(min_num, min_num + tam)

    def test_analisis_ordenacion_seleccion(self):
        """El analisis del algoritmo de ordenación selección debe devolver la lista ordenada, recibiendo como entrada
            una lista ya ordenada. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        os = OrdenacionSeleccion()
        an = Analysis()
        res = os.analizar(self.lo, an)
        self.assertListEqual(self.lo, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_insercion(self):
        """El analisis del algoritmo de ordenación inserción debe devolver la lista ordenada, recibiendo como entrada
            una lista ya ordenada. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        oi = OrdenacionInsercion()
        an = Analysis()
        res = oi.analizar(self.lo, an)
        self.assertListEqual(self.lo, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_burbuja(self):
        """El analisis del algoritmo de ordenación burbuja debe devolver la lista ordenada, recibiendo como entrada
            una lista ya ordenada. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        ob = OrdenacionBurbuja()
        an = Analysis()
        res = ob.analizar(self.lo, an)
        self.assertListEqual(self.lo, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_quicksort(self):
        """El analisis del algoritmo de ordenación quicksort debe devolver la lista ordenada, recibiendo como entrada
            una lista ya ordenada. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        oq = OrdenacionQuicksort()
        an = Analysis()
        res = oq.analizar(self.lo, an)
        self.assertListEqual(self.lo, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_shellsort(self):
        """El analisis del algoritmo de ordenación shellsort debe devolver la lista ordenada, recibiendo como entrada
            una lista ya ordenada. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        osh = OrdenacionShellsort()
        an = Analysis()
        res = osh.analizar(self.lo, an)
        self.assertListEqual(self.lo, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_mergesort(self):
        """El analisis del algoritmo de ordenación mergesort debe devolver la lista ordenada, recibiendo como entrada
            una lista ya ordenada. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        om = OrdenacionMergesort()
        an = Analysis()
        res = om.analizar(self.lo, an)
        self.assertListEqual(self.lo, res)
        self.assertIs(an.inicializado(), False)

    def test_analisis_ordenacion_radixsort(self):
        """El analisis del algoritmo de ordenación radixsort debe devolver la lista ordenada, recibiendo como entrada
            una lista ya ordenada. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        orx = OrdenacionRadixsort()
        an = Analysis()
        res = orx.analizar(self.lo, an)
        self.assertListEqual(self.lo, res)
        self.assertIs(an.inicializado_sin_comparaciones(), False)


class EntradasErroneas(unittest.TestCase):
    no_listas = (
        1,
        'm',
        False,
        None,
        {1: "value"},
        2.47,
        -9,
        "cadena",
        [[0, 1], [8, 10]],
        []
    )

    def test_ordenacion_seleccion_entrada_no_lista(self):
        """El analisis del algoritmo de ordenación selección debe fallar al recibir como entrada
         un objeto que no sea una lista o una secuencia inmutable tuple."""
        os = OrdenacionSeleccion()
        for entrada_erronea in self.no_listas:
            an = Analysis()
            self.assertRaises(ex.EntradaNoLista, os.analizar, entrada_erronea, an)

    def test_ordenacion_insercion_entrada_no_lista(self):
        """El analisis del algoritmo de ordenación inserción debe fallar al recibir como entrada
         un objeto que no sea una lista o una secuencia inmutable tuple."""
        oi = OrdenacionInsercion()
        for entrada_erronea in self.no_listas:
            an = Analysis()
            self.assertRaises(ex.EntradaNoLista, oi.analizar, entrada_erronea, an)

    def test_ordenacion_burbuja_entrada_no_lista(self):
        """El analisis del algoritmo de ordenación burbuja debe fallar al recibir como entrada
         un objeto que no sea una lista o una secuencia inmutable tuple."""
        ob = OrdenacionBurbuja()
        for entrada_erronea in self.no_listas:
            an = Analysis()
            self.assertRaises(ex.EntradaNoLista, ob.analizar, entrada_erronea, an)

    def test_ordenacion_quicksort_entrada_no_lista(self):
        """El analisis del algoritmo de ordenación quicksort debe fallar al recibir como entrada
         un objeto que no sea una lista o una secuencia inmutable tuple."""
        oq = OrdenacionQuicksort()
        for entrada_erronea in self.no_listas:
            an = Analysis()
            self.assertRaises(ex.EntradaNoLista, oq.analizar, entrada_erronea, an)

    def test_ordenacion_shellsort_entrada_no_lista(self):
        """El analisis del algoritmo de ordenación shellsort debe fallar al recibir como entrada
         un objeto que no sea una lista o una secuencia inmutable tuple."""
        osh = OrdenacionShellsort()
        for entrada_erronea in self.no_listas:
            an = Analysis()
            self.assertRaises(ex.EntradaNoLista, osh.analizar, entrada_erronea, an)

    def test_ordenacion_mergesort_entrada_no_lista(self):
        """El analisis del algoritmo de ordenación mergesort debe fallar al recibir como entrada
         un objeto que no sea una lista o una secuencia inmutable tuple."""
        om = OrdenacionMergesort()
        for entrada_erronea in self.no_listas:
            an = Analysis()
            self.assertRaises(ex.EntradaNoLista, om.analizar, entrada_erronea, an)

    def test_ordenacion_radixsort_entrada_no_lista(self):
        """El analisis del algoritmo de ordenación radixsort debe fallar al recibir como entrada
         un objeto que no sea una lista o una secuencia inmutable tuple."""
        orx = OrdenacionRadixsort()
        for entrada_erronea in self.no_listas:
            an = Analysis()
            self.assertRaises(ex.EntradaNoLista, orx.analizar, entrada_erronea, an)


if __name__ == '__main__':
    unittest.main()
