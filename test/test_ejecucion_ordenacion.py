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

    def test_ejecucion_ordenacion_seleccion(self):
        """La ejecución del algoritmo de ordenación selección debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida"""
        os = OrdenacionSeleccion()
        res = os.ejecutar(self.lista_desordenada)
        self.assertListEqual(self.lista_ordenada, res)

    def test_ejecucion_ordenacion_insercion(self):
        """La ejecución del algoritmo de ordenación inserción debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida"""
        oi = OrdenacionInsercion()
        res = oi.ejecutar(self.lista_desordenada)
        self.assertListEqual(self.lista_ordenada, res)

    def test_ejecucion_ordenacion_burbuja(self):
        """La ejecución del algoritmo de ordenación burbuja debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida"""
        ob = OrdenacionBurbuja()
        res = ob.ejecutar(self.lista_desordenada)
        self.assertListEqual(self.lista_ordenada, res)

    def test_ejecucion_ordenacion_quicksort(self):
        """La ejecución del algoritmo de ordenación quicksort debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida"""
        oq = OrdenacionQuicksort()
        res = oq.ejecutar(self.lista_desordenada)
        self.assertListEqual(self.lista_ordenada, res)

    def test_ejecucion_ordenacion_shellsort(self):
        """La ejecución del algoritmo de ordenación shellsort debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida"""
        osh = OrdenacionShellsort()
        res = osh.ejecutar(self.lista_desordenada)
        self.assertListEqual(self.lista_ordenada, res)

    def test_ejecucion_ordenacion_mergesort(self):
        """La ejecución del algoritmo de ordenación mergesort debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida"""
        om = OrdenacionMergesort()
        res = om.ejecutar(self.lista_desordenada)
        self.assertListEqual(self.lista_ordenada, res)

    def test_ejecucion_ordenacion_radixsort(self):
        """La ejecución del algoritmo de ordenación radixsort debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida"""
        orx = OrdenacionRadixsort()
        res = orx.ejecutar(self.lista_desordenada)
        self.assertListEqual(self.lista_ordenada, res)

    def test_ejecucion_ordenacion_seleccion_un_elemento(self):
        """La ejecución del algoritmo de ordenación selección debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida con un solo elemento"""
        os = OrdenacionSeleccion()
        res = os.ejecutar(self.lo1)
        self.assertListEqual(self.lo1_ordenada, res)

    def test_ejecucion_ordenacion_insercion_un_elemento(self):
        """La ejecución del algoritmo de ordenación inserción debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida con un solo elemento"""
        oi = OrdenacionInsercion()
        res = oi.ejecutar(self.lo1)
        self.assertListEqual(self.lo1_ordenada, res)

    def test_ejecucion_ordenacion_burbuja_un_elemento(self):
        """La ejecución del algoritmo de ordenación burbuja debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida con un solo elemento"""
        ob = OrdenacionBurbuja()
        res = ob.ejecutar(self.lo1)
        self.assertListEqual(self.lo1_ordenada, res)

    def test_ejecucion_ordenacion_quicksort_un_elemento(self):
        """La ejecución del algoritmo de ordenación quicksort debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida con un solo elemento"""
        oq = OrdenacionQuicksort()
        res = oq.ejecutar(self.lo1)
        self.assertListEqual(self.lo1_ordenada, res)

    def test_ejecucion_ordenacion_shellsort_un_elemento(self):
        """La ejecución del algoritmo de ordenación shellsort debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida con un solo elemento"""
        osh = OrdenacionShellsort()
        res = osh.ejecutar(self.lo1)
        self.assertListEqual(self.lo1_ordenada, res)

    def test_ejecucion_ordenacion_mergesort_un_elemento(self):
        """La ejecución del algoritmo de ordenación mergesort debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida con un solo elemento"""
        om = OrdenacionMergesort()
        res = om.ejecutar(self.lo1)
        self.assertListEqual(self.lo1_ordenada, res)

    def test_ejecucion_ordenacion_radixsort_un_elemento(self):
        """La ejecución del algoritmo de ordenación radixsort debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida con un solo elemento"""
        orx = OrdenacionRadixsort()
        res = orx.ejecutar(self.lo1)
        self.assertListEqual(self.lo1_ordenada, res)

    def test_ejecucion_ordenacion_seleccion_casi_ordenada(self):
        """La ejecución del algoritmo de ordenación selección debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida casi ordenada"""
        os = OrdenacionSeleccion()
        res = os.ejecutar(self.lista_casi_ordenada)
        self.assertListEqual(self.lista_ordenada, res)

    def test_ejecucion_ordenacion_insercion_casi_ordenada(self):
        """La ejecución del algoritmo de ordenación inserción debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida casi ordenada"""
        oi = OrdenacionInsercion()
        res = oi.ejecutar(self.lista_casi_ordenada)
        self.assertListEqual(self.lista_ordenada, res)

    def test_ejecucion_ordenacion_burbuja_casi_ordenada(self):
        """La ejecución del algoritmo de ordenación burbuja debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida casi ordenada"""
        ob = OrdenacionBurbuja()
        res = ob.ejecutar(self.lista_casi_ordenada)
        self.assertListEqual(self.lista_ordenada, res)

    def test_ejecucion_ordenacion_quicksort_casi_ordenada(self):
        """La ejecución del algoritmo de ordenación quicksort debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida casi ordenada"""
        oq = OrdenacionQuicksort()
        res = oq.ejecutar(self.lista_casi_ordenada)
        self.assertListEqual(self.lista_ordenada, res)

    def test_ejecucion_ordenacion_shellsort_casi_ordenada(self):
        """La ejecución del algoritmo de ordenación shellsort debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida casi ordenada"""
        osh = OrdenacionShellsort()
        res = osh.ejecutar(self.lista_casi_ordenada)
        self.assertListEqual(self.lista_ordenada, res)

    def test_ejecucion_ordenacion_mergesort_casi_ordenada(self):
        """La ejecución del algoritmo de ordenación mergesort debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida casi ordenada"""
        om = OrdenacionMergesort()
        res = om.ejecutar(self.lista_casi_ordenada)
        self.assertListEqual(self.lista_ordenada, res)

    def test_ejecucion_ordenacion_radixsort_casi_ordenada(self):
        """La ejecución del algoritmo de ordenación radixsort debe devolver la lista ordenada, recibiendo como entrada
            una lista conocida casi ordenada"""
        orx = OrdenacionRadixsort()
        res = orx.ejecutar(self.lista_casi_ordenada)
        self.assertListEqual(self.lista_ordenada, res)


class ListaAleatoriaSinRepeticion(unittest.TestCase):
    la_sr = cl.aleatoria_sin_repeticion(min_num, min_num + tam)
    lista_ordenada = sorted(list(la_sr))

    def test_ejecucion_ordenacion_seleccion(self):
        """La ejecución del algoritmo de ordenación selección debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria sin repetición"""
        os = OrdenacionSeleccion()
        res = os.ejecutar(self.la_sr)
        self.assertListEqual(self.lista_ordenada, res)

    def test_ejecucion_ordenacion_insercion(self):
        """La ejecución del algoritmo de ordenación selección debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria sin repetición"""
        oi = OrdenacionInsercion()
        res = oi.ejecutar(self.la_sr)
        self.assertListEqual(self.lista_ordenada, res)

    def test_ejecucion_ordenacion_burbuja(self):
        """La ejecución del algoritmo de ordenación burbuja debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria sin repetición"""
        ob = OrdenacionBurbuja()
        res = ob.ejecutar(self.la_sr)
        self.assertListEqual(self.lista_ordenada, res)

    def test_ejecucion_ordenacion_quicksort(self):
        """La ejecución del algoritmo de ordenación quicksort debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria sin repetición"""
        oq = OrdenacionQuicksort()
        res = oq.ejecutar(self.la_sr)
        self.assertListEqual(self.lista_ordenada, res)

    def test_ejecucion_ordenacion_shellsort(self):
        """La ejecución del algoritmo de ordenación shellsort debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria sin repetición"""
        osh = OrdenacionShellsort()
        res = osh.ejecutar(self.la_sr)
        self.assertListEqual(self.lista_ordenada, res)

    def test_ejecucion_ordenacion_mergesort(self):
        """La ejecución del algoritmo de ordenación mergesort debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria sin repetición"""
        om = OrdenacionMergesort()
        res = om.ejecutar(self.la_sr)
        self.assertListEqual(self.lista_ordenada, res)

    def test_ejecucion_ordenacion_radixsort(self):
        """La ejecución del algoritmo de ordenación radixsort debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria sin repetición"""
        orx = OrdenacionRadixsort()
        res = orx.ejecutar(self.la_sr)
        self.assertListEqual(self.lista_ordenada, res)


class ListaAleatoriaConRepeticion(unittest.TestCase):
    la_cr = cl.aleatoria(min_num, max_num, tam)
    lista_ordenada = sorted(list(la_cr))

    def test_ejecucion_ordenacion_seleccion(self):
        """La ejecución del algoritmo de ordenación selección debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria con repetición"""
        os = OrdenacionSeleccion()
        res = os.ejecutar(self.la_cr)
        self.assertListEqual(self.lista_ordenada, res)

    def test_ejecucion_ordenacion_insercion(self):
        """La ejecución del algoritmo de ordenación inserción debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria con repetición"""
        oi = OrdenacionInsercion()
        res = oi.ejecutar(self.la_cr)
        self.assertListEqual(self.lista_ordenada, res)

    def test_ejecucion_ordenacion_burbuja(self):
        """La ejecución del algoritmo de ordenación burbuja debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria con repetición"""
        ob = OrdenacionBurbuja()
        res = ob.ejecutar(self.la_cr)
        self.assertListEqual(self.lista_ordenada, res)

    def test_ejecucion_ordenacion_quicksort(self):
        """La ejecución del algoritmo de ordenación quicksort debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria con repetición"""
        oq = OrdenacionQuicksort()
        res = oq.ejecutar(self.la_cr)
        self.assertListEqual(self.lista_ordenada, res)

    def test_ejecucion_ordenacion_shellsort(self):
        """La ejecución del algoritmo de ordenación shellsort debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria con repetición"""
        osh = OrdenacionShellsort()
        res = osh.ejecutar(self.la_cr)
        self.assertListEqual(self.lista_ordenada, res)

    def test_ejecucion_ordenacion_mergesort(self):
        """La ejecución del algoritmo de ordenación mergesort debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria con repetición"""
        om = OrdenacionMergesort()
        res = om.ejecutar(self.la_cr)
        self.assertListEqual(self.lista_ordenada, res)

    def test_ejecucion_ordenacion_radixsort(self):
        """La ejecución del algoritmo de ordenación radixsort debe devolver la lista ordenada, recibiendo como entrada
            una lista aleatoria con repetición"""
        orx = OrdenacionRadixsort()
        res = orx.ejecutar(self.la_cr)
        self.assertListEqual(self.lista_ordenada, res)


class ListaYaOrdenada(unittest.TestCase):
    lo = cl.ordenada(min_num, min_num + tam)

    def test_ejecucion_ordenacion_seleccion(self):
        """La ejecución del algoritmo de ordenación selección debe devolver la lista ordenada, recibiendo como entrada
            una lista ya ordenada"""
        os = OrdenacionSeleccion()
        res = os.ejecutar(self.lo)
        self.assertListEqual(self.lo, res)

    def test_ejecucion_ordenacion_insercion(self):
        """La ejecución del algoritmo de ordenación inserción debe devolver la lista ordenada, recibiendo como entrada
            una lista ya ordenada"""
        oi = OrdenacionInsercion()
        res = oi.ejecutar(self.lo)
        self.assertListEqual(self.lo, res)

    def test_ejecucion_ordenacion_burbuja(self):
        """La ejecución del algoritmo de ordenación burbuja debe devolver la lista ordenada, recibiendo como entrada
            una lista ya ordenada"""
        ob = OrdenacionBurbuja()
        res = ob.ejecutar(self.lo)
        self.assertListEqual(self.lo, res)

    def test_ejecucion_ordenacion_quicksort(self):
        """La ejecución del algoritmo de ordenación quicksort debe devolver la lista ordenada, recibiendo como entrada
            una lista ya ordenada"""
        oq = OrdenacionQuicksort()
        res = oq.ejecutar(self.lo)
        self.assertListEqual(self.lo, res)

    def test_ejecucion_ordenacion_shellsort(self):
        """La ejecución del algoritmo de ordenación shellsort debe devolver la lista ordenada, recibiendo como entrada
            una lista ya ordenada"""
        osh = OrdenacionShellsort()
        res = osh.ejecutar(self.lo)
        self.assertListEqual(self.lo, res)

    def test_ejecucion_ordenacion_mergesort(self):
        """La ejecución del algoritmo de ordenación mergesort debe devolver la lista ordenada, recibiendo como entrada
            una lista ya ordenada"""
        om = OrdenacionMergesort()
        res = om.ejecutar(self.lo)
        self.assertListEqual(self.lo, res)

    def test_ejecucion_ordenacion_radixsort(self):
        """La ejecución del algoritmo de ordenación radixsort debe devolver la lista ordenada, recibiendo como entrada
            una lista ya ordenada"""
        orx = OrdenacionRadixsort()
        res = orx.ejecutar(self.lo)
        self.assertListEqual(self.lo, res)


class EntradasErroneas(unittest.TestCase):
    no_listas = (
        1,
        'm',
        True,
        None,
        {1: "value"},
        2.47,
        -9,
        "cadena",
        [[0, 1], [8, 10]],
        []
    )

    def test_ordenacion_seleccion_entrada_no_lista(self):
        """La ejecución del algoritmo de ordenación selección debe fallar al recibir como entrada
         un objeto que no sea una lista o una secuencia inmutable tuple """
        os = OrdenacionSeleccion()
        for entrada_erronea in self.no_listas:
            self.assertRaises(ex.EntradaNoLista, os.ejecutar, entrada_erronea)

    def test_ordenacion_insercion_entrada_no_lista(self):
        """La ejecución del algoritmo de ordenación inserción debe fallar al recibir como entrada
         un objeto que no sea una lista o una secuencia inmutable tuple """
        oi = OrdenacionInsercion()
        for entrada_erronea in self.no_listas:
            self.assertRaises(ex.EntradaNoLista, oi.ejecutar, entrada_erronea)

    def test_ordenacion_burbuja_entrada_no_lista(self):
        """La ejecución del algoritmo de ordenación burbuja debe fallar al recibir como entrada
         un objeto que no sea una lista o una secuencia inmutable tuple """
        ob = OrdenacionBurbuja()
        for entrada_erronea in self.no_listas:
            self.assertRaises(ex.EntradaNoLista, ob.ejecutar, entrada_erronea)

    def test_ordenacion_quicksort_entrada_no_lista(self):
        """La ejecución del algoritmo de ordenación quicksort debe fallar al recibir como entrada
         un objeto que no sea una lista o una secuencia inmutable tuple """
        oq = OrdenacionQuicksort()
        for entrada_erronea in self.no_listas:
            self.assertRaises(ex.EntradaNoLista, oq.ejecutar, entrada_erronea)

    def test_ordenacion_shellsort_entrada_no_lista(self):
        """La ejecución del algoritmo de ordenación shellsort debe fallar al recibir como entrada
         un objeto que no sea una lista o una secuencia inmutable tuple """
        osh = OrdenacionShellsort()
        for entrada_erronea in self.no_listas:
            self.assertRaises(ex.EntradaNoLista, osh.ejecutar, entrada_erronea)

    def test_ordenacion_mergesort_entrada_no_lista(self):
        """La ejecución del algoritmo de ordenación mergesort debe fallar al recibir como entrada
         un objeto que no sea una lista o una secuencia inmutable tuple """
        om = OrdenacionMergesort()
        for entrada_erronea in self.no_listas:
            self.assertRaises(ex.EntradaNoLista, om.ejecutar, entrada_erronea)

    def test_ordenacion_radixsort_entrada_no_lista(self):
        """La ejecución del algoritmo de ordenación radixsort debe fallar al recibir como entrada
         un objeto que no sea una lista o una secuencia inmutable tuple """
        orx = OrdenacionRadixsort()
        for entrada_erronea in self.no_listas:
            self.assertRaises(ex.EntradaNoLista, orx.ejecutar, entrada_erronea)


if __name__ == '__main__':
    unittest.main()
