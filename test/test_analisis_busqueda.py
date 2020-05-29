import unittest
import bin.crear_lista as cl
import bin.excepciones as ex
from bin.algoritmos.busq.busquedalineal import BusquedaLineal
from bin.algoritmos.busq.busquedabinaria import BusquedaBinaria
from bin.algoritmos.busq.busquedasalto import BusquedaSalto
from bin.algoritmos.busq.busquedainterpolacion import BusquedaInterpolacion
from bin.algoritmos.busq.busquedaexponencial import BusquedaExponencial
from bin.algoritmos.busq.busquedafibonacci import BusquedaFibonacci
from bin.analysis import Analysis

tam = 32
min_num = 8
max_num = 16
max_espaciado = 4
la_sr = cl.aleatoria_sin_repeticion(min_num, tam + min_num)
la_cr = cl.aleatoria(min_num, max_num, tam)
loa_sr = cl.ordenada_aleatoria_sin_repeticion(min_num, max_espaciado, tam)
loa_cr = cl.ordenada_aleatoria_con_repeticion(min_num, max_espaciado, tam)


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
    indices = (
        (1, 2),
        (2, 3),
        (3, 8),
        (4, 7),
        (5, 0),
        (6, 9),
        (7, 6),
        (8, 1),
        (9, 4)
    )
    lo1, lo2 = [7], [7, 7]
    indices1 = (
        0, 7
    )
    indices2 = (
        [0, 1], 7
    )

    def test_analisis_busqueda_lineal_lista_desordenada(self):
        """El análisis del algoritmo de búsqueda lineal debe devolver el índice donde se encuentra el elemento buscado
         en la lista conocida. Además el análisis debe tener algunos contadores mayores que 0
         y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        bl = BusquedaLineal()
        for numero, indice in self.indices:
            an = Analysis()
            indice_buscado = bl.analizar(self.lista_desordenada, an, numero)
            self.assertEqual(indice, indice_buscado)
            self.assertIs(an.inicializado_sin_intercambios(), True)

    def test_analisis_busqueda_lineal_un_elemento(self):
        """El análisis del algoritmo de búsqueda lineal debe devolver el índice donde se encuentra el elemento buscado
         en la lista conocida con un solo elemento. Además el análisis debe tener algunos contadores mayores que 0
         y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        bl = BusquedaLineal()
        an = Analysis()
        indice_buscado = bl.analizar(self.lo1, an, self.indices1[1])
        self.assertEqual(self.indices1[0], indice_buscado)
        self.assertIs(an.inicializado_sin_intercambios(), True)

    def test_analisis_busqueda_binaria_un_elemento(self):
        """El análisis del algoritmo de búsqueda binaria debe devolver el índice donde se encuentra el elemento buscado
        en la lista conocida con un solo elemento. Además el análisis debe tener algunos contadores mayores que 0
        y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        bb = BusquedaBinaria()
        an = Analysis()
        indice_buscado = bb.analizar(self.lo1, an, self.indices1[1])
        self.assertEqual(self.indices1[0], indice_buscado)
        self.assertIs(an.inicializado_sin_intercambios(), True)

    def test_analisis_busqueda_salto_un_elemento(self):
        """El análisis del algoritmo de búsqueda salto debe devolver el índice donde se encuentra el elemento buscado
        en la lista conocida con un solo elemento. Además el análisis debe tener algunos contadores mayores que 0
        y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        bs = BusquedaSalto()
        an = Analysis()
        indice_buscado = bs.analizar(self.lo1, an, self.indices1[1])
        self.assertEqual(self.indices1[0], indice_buscado)
        self.assertIs(an.inicializado_sin_intercambios(), True)

    def test_analisis_busqueda_interpolacion_un_elemento(self):
        """El análisis del algoritmo de búsqueda interpolacion debe devolver el índice donde se encuentra el elemento
        en la lista conocida con un solo elemento. Además el análisis debe tener algunos contadores mayores que 0
        y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        bi = BusquedaInterpolacion()
        an = Analysis()
        indice_buscado = bi.analizar(self.lo1, an, self.indices1[1])
        self.assertEqual(self.indices1[0], indice_buscado)
        self.assertIs(an.inicializado_sin_intercambios(), True)

    def test_analisis_busqueda_exponencial_un_elemento(self):
        """El análisis del algoritmo de búsqueda exponencial debe devolver el índice donde se encuentra el elemento
        en la lista conocida con un solo elemento. Además el análisis debe tener algunos contadores mayores que 0
        y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        be = BusquedaExponencial()
        an = Analysis()
        indice_buscado = be.analizar(self.lo1, an, self.indices1[1])
        self.assertEqual(self.indices1[0], indice_buscado)
        self.assertIs(an.inicializado_sin_intercambios(), True)

    def test_analisis_busqueda_fibonacci_un_elemento(self):
        """El análisis del algoritmo de búsqueda fibonacci debe devolver el índice donde se encuentra el elemento
        en la lista conocida con un solo elemento. Además el análisis debe tener algunos contadores mayores que 0
        y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        bf = BusquedaFibonacci()
        an = Analysis()
        indice_buscado = bf.analizar(self.lo1, an, self.indices1[1])
        self.assertEqual(self.indices1[0], indice_buscado)
        self.assertIs(an.inicializado_sin_intercambios(), True)

    def test_analisis_busqueda_lineal_dos_elementos_iguales(self):
        """El análisis del algoritmo de búsqueda lineal debe devolver el índice donde se encuentra el elemento buscado
         en la lista conocida con dos elementos iguales. Además el análisis debe tener algunos contadores mayores que 0
         y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        bl = BusquedaLineal()
        an = Analysis()
        indice_buscado = bl.analizar(self.lo2, an, self.indices2[1])
        self.assertIn(indice_buscado, self.indices2[0])
        self.assertIs(an.inicializado_sin_intercambios(), True)

    def test_analisis_busqueda_binaria_dos_elementos_iguales(self):
        """El análisis del algoritmo de búsqueda binaria debe devolver el índice donde se encuentra el elemento buscado
        en la lista conocida con dos elementos iguales. Además el análisis debe tener algunos contadores mayores que 0
        y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        bb = BusquedaBinaria()
        an = Analysis()
        indice_buscado = bb.analizar(self.lo2, an, self.indices2[1])
        self.assertIn(indice_buscado, self.indices2[0])
        self.assertIs(an.inicializado_sin_intercambios(), True)

    def test_analisis_busqueda_salto_dos_elementos_iguales(self):
        """El análisis del algoritmo de búsqueda salto debe devolver el índice donde se encuentra el elemento buscado
        en la lista conocida con dos elementos iguales. Además el análisis debe tener algunos contadores mayores que 0
        y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        bs = BusquedaSalto()
        an = Analysis()
        indice_buscado = bs.analizar(self.lo2, an, self.indices2[1])
        self.assertIn(indice_buscado, self.indices2[0])
        self.assertIs(an.inicializado_sin_intercambios(), True)

    def test_analisis_busqueda_interpolacion_dos_elementos_iguales(self):
        """El análisis del algoritmo de búsqueda interpolacion debe devolver el índice donde se encuentra el elemento
        en la lista conocida con dos elementos iguales. Además el análisis debe tener algunos contadores mayores que 0
        y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        bi = BusquedaInterpolacion()
        an = Analysis()
        indice_buscado = bi.analizar(self.lo2, an, self.indices2[1])
        self.assertIn(indice_buscado, self.indices2[0])
        self.assertIs(an.inicializado_sin_intercambios(), True)

    def test_analisis_busqueda_exponencial_dos_elementos_iguales(self):
        """El análisis del algoritmo de búsqueda exponencial debe devolver el índice donde se encuentra el elemento
        en la lista conocida con dos elementos iguales. Además el análisis debe tener algunos contadores mayores que 0
        y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        be = BusquedaExponencial()
        an = Analysis()
        indice_buscado = be.analizar(self.lo2, an, self.indices2[1])
        self.assertIn(indice_buscado, self.indices2[0])
        self.assertIs(an.inicializado_sin_intercambios(), True)

    def test_analisis_busqueda_fibonacci_dos_elementos_iguales(self):
        """El análisis del algoritmo de búsqueda fibonacci debe devolver el índice donde se encuentra el elemento
        en la lista conocida con dos elementos iguales. Además el análisis debe tener algunos contadores mayores que 0
        y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        bf = BusquedaFibonacci()
        an = Analysis()
        indice_buscado = bf.analizar(self.lo2, an, self.indices2[1])
        self.assertIn(indice_buscado, self.indices2[0])
        self.assertIs(an.inicializado_sin_intercambios(), True)


class ListaOrdenada(unittest.TestCase):
    indices = [(x, x * 4) for x in range(tam)]
    lista_ordenada = [num for i, num in indices]

    def test_analisis_busqueda_lineal(self):
        """El análisis del algoritmo de búsqueda lineal debe devolver el índice donde se encuentra el elemento buscado
         en la lista ordenada indice * 4 de tamaño tam. Además el análisis debe tener algunos contadores mayores que 0
         y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        bl = BusquedaLineal()
        for indice, numero in self.indices:
            an = Analysis()
            indice_buscado = bl.analizar(self.lista_ordenada, an, numero)
            self.assertEqual(indice, indice_buscado)
            self.assertIs(an.inicializado_sin_intercambios(), True)

    def test_analisis_busqueda_binaria(self):
        """El análisis del algoritmo de búsqueda binaria debe devolver el índice donde se encuentra el elemento buscado
         en la lista ordenada indice * 4 de tamaño tam. Además el análisis debe tener algunos contadores mayores que 0
         y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        bb = BusquedaBinaria()
        for indice, numero in self.indices:
            an = Analysis()
            indice_buscado = bb.analizar(self.lista_ordenada, an, numero)
            self.assertEqual(indice, indice_buscado)
            self.assertIs(an.inicializado_sin_intercambios(), True)

    def test_analisis_busqueda_salto(self):
        """El análisis del algoritmo de búsqueda salto debe devolver el índice donde se encuentra el elemento buscado
         en la lista ordenada indice * 4 de tamaño tam. Además el análisis debe tener algunos contadores mayores que 0
         y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        bs = BusquedaSalto()
        for indice, numero in self.indices:
            an = Analysis()
            indice_buscado = bs.analizar(self.lista_ordenada, an, numero)
            self.assertEqual(indice, indice_buscado)
            self.assertIs(an.inicializado_sin_intercambios(), True)

    def test_analisis_busqueda_interpolacion(self):
        """El análisis del algoritmo de búsqueda interpolacion debe devolver el índice donde se encuentra el elemento
        buscado en la lista ordenada indice * 4 de tamaño tam. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado. """
        bi = BusquedaInterpolacion()
        for indice, numero in self.indices:
            an = Analysis()
            indice_buscado = bi.analizar(self.lista_ordenada, an, numero)
            self.assertEqual(indice, indice_buscado)
            self.assertIs(an.inicializado_sin_intercambios(), True)

    def test_analisis_busqueda_exponencial(self):
        """El análisis del algoritmo de búsqueda exponencial debe devolver el índice donde se encuentra el elemento
        buscado en la lista ordenada indice * 4 de tamaño tam. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado. """
        be = BusquedaExponencial()
        for indice, numero in self.indices:
            an = Analysis()
            indice_buscado = be.analizar(self.lista_ordenada, an, numero)
            self.assertEqual(indice, indice_buscado)
            self.assertIs(an.inicializado_sin_intercambios(), True)

    def test_analisis_busqueda_fibonacci(self):
        """El análisis del algoritmo de búsqueda fibonacci debe devolver el índice donde se encuentra el elemento
        buscado en la lista ordenada indice * 4 de tamaño tam. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado. """
        bf = BusquedaFibonacci()
        for indice, numero in self.indices:
            an = Analysis()
            indice_buscado = bf.analizar(self.lista_ordenada, an, numero)
            self.assertEqual(indice, indice_buscado)
            self.assertIs(an.inicializado_sin_intercambios(), True)


class ListaOrdenadaAleatoriaSinRepeticion(unittest.TestCase):
    diccionario = {k: loa_sr[k] for k in range(tam)}

    def test_analisis_busqueda_lineal(self):
        """El análisis del algoritmo de búsqueda lineal debe devolver el índice donde se encuentra el elemento buscado
         en la lista ordenada aleatoria sin repetición. Además el análisis debe tener algunos contadores mayores que 0
         y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        bl = BusquedaLineal()
        for indice, numero in self.diccionario.items():
            an = Analysis()
            indice_buscado = bl.analizar(loa_sr, an, numero)
            self.assertEqual(indice, indice_buscado)
            self.assertIs(an.inicializado_sin_intercambios(), True)

    def test_analisis_busqueda_binaria(self):
        """El análisis del algoritmo de búsqueda binaria debe devolver el índice donde se encuentra el elemento buscado
         en la lista ordenada aleatoria sin repetición. Además el análisis debe tener algunos contadores mayores que 0
         y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        bb = BusquedaBinaria()
        for indice, numero in self.diccionario.items():
            an = Analysis()
            indice_buscado = bb.analizar(loa_sr, an, numero)
            self.assertEqual(indice, indice_buscado)
            self.assertIs(an.inicializado_sin_intercambios(), True)

    def test_analisis_busqueda_salto(self):
        """El análisis del algoritmo de búsqueda salto debe devolver el índice donde se encuentra el elemento buscado
         en la lista ordenada aleatoria sin repetición. Además el análisis debe tener algunos contadores mayores que 0
         y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        bs = BusquedaSalto()
        for indice, numero in self.diccionario.items():
            an = Analysis()
            indice_buscado = bs.analizar(loa_sr, an, numero)
            self.assertEqual(indice, indice_buscado)
            self.assertIs(an.inicializado_sin_intercambios(), True)

    def test_analisis_busqueda_interpolacion(self):
        """El análisis del algoritmo de búsqueda interpolacion debe devolver el índice donde se encuentra el elemento
        buscado en la lista ordenada aleatoria sin repetición. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado. """
        bi = BusquedaInterpolacion()
        for indice, numero in self.diccionario.items():
            an = Analysis()
            indice_buscado = bi.analizar(loa_sr, an, numero)
            self.assertEqual(indice, indice_buscado)
            self.assertIs(an.inicializado_sin_intercambios(), True)

    def test_analisis_busqueda_exponencial(self):
        """El análisis del algoritmo de búsqueda exponencial debe devolver el índice donde se encuentra el elemento
        buscado en la lista ordenada aleatoria sin repetición. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado. """
        be = BusquedaExponencial()
        for indice, numero in self.diccionario.items():
            an = Analysis()
            indice_buscado = be.analizar(loa_sr, an, numero)
            self.assertEqual(indice, indice_buscado)
            self.assertIs(an.inicializado_sin_intercambios(), True)

    def test_analisis_busqueda_fibonacci(self):
        """El análisis del algoritmo de búsqueda fibonacci debe devolver el índice donde se encuentra el elemento
        buscado en la lista ordenada aleatoria sin repetición. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado. """
        bf = BusquedaFibonacci()
        for indice, numero in self.diccionario.items():
            an = Analysis()
            indice_buscado = bf.analizar(loa_sr, an, numero)
            self.assertEqual(indice, indice_buscado)
            self.assertIs(an.inicializado_sin_intercambios(), True)


class ListaOrdenadaAleatoriaConRepeticion(unittest.TestCase):
    diccionario = {k: [v for v in range(tam) if loa_cr[v] == k] for k in set(loa_cr)}

    def test_analisis_busqueda_lineal(self):
        """El análisis del algoritmo de búsqueda lineal debe devolver el índice donde se encuentra el elemento buscado
         en la lista ordenada aleatoria con repetición. Además el análisis debe tener algunos contadores mayores que 0
         y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        bl = BusquedaLineal()
        for numero, indices_posibles in self.diccionario.items():
            an = Analysis()
            indice_buscado = bl.analizar(loa_cr, an, numero)
            self.assertIn(indice_buscado, indices_posibles)
            self.assertIs(an.inicializado_sin_intercambios(), True)

    def test_analisis_busqueda_binaria(self):
        """El análisis del algoritmo de búsqueda binaria debe devolver el índice donde se encuentra el elemento buscado
         en la lista ordenada aleatoria con repetición. Además el análisis debe tener algunos contadores mayores que 0
         y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        bb = BusquedaBinaria()
        for numero, indices_posibles in self.diccionario.items():
            an = Analysis()
            indice_buscado = bb.analizar(loa_cr, an, numero)
            self.assertIn(indice_buscado, indices_posibles)
            self.assertIs(an.inicializado_sin_intercambios(), True)

    def test_analisis_busqueda_salto(self):
        """El análisis del algoritmo de búsqueda salto debe devolver el índice donde se encuentra el elemento buscado
         en la lista ordenada aleatoria con repetición. Además el análisis debe tener algunos contadores mayores que 0
         y otros deben seguir a 0, dependiendo del algoritmo analizado."""
        bs = BusquedaSalto()
        for numero, indices_posibles in self.diccionario.items():
            an = Analysis()
            indice_buscado = bs.analizar(loa_cr, an, numero)
            self.assertIn(indice_buscado, indices_posibles)
            self.assertIs(an.inicializado_sin_intercambios(), True)

    def test_analisis_busqueda_interpolacion(self):
        """El análisis del algoritmo de búsqueda interpolacion debe devolver el índice donde se encuentra el elemento
        buscado en la lista ordenada aleatoria con repetición. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado. """
        bi = BusquedaInterpolacion()
        for numero, indices_posibles in self.diccionario.items():
            an = Analysis()
            indice_buscado = bi.analizar(loa_cr, an, numero)
            self.assertIn(indice_buscado, indices_posibles)
            self.assertIs(an.inicializado_sin_intercambios(), True)

    def test_analisis_busqueda_exponencial(self):
        """El análisis del algoritmo de búsqueda exponencial debe devolver el índice donde se encuentra el elemento
        buscado en la lista ordenada aleatoria con repetición. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado. """
        be = BusquedaExponencial()
        for numero, indices_posibles in self.diccionario.items():
            an = Analysis()
            indice_buscado = be.analizar(loa_cr, an, numero)
            self.assertIn(indice_buscado, indices_posibles)
            self.assertIs(an.inicializado_sin_intercambios(), True)

    def test_analisis_busqueda_fibonacci(self):
        """El análisis del algoritmo de búsqueda fibonacci debe devolver el índice donde se encuentra el elemento
        buscado en la lista ordenada aleatoria con repetición. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado. """
        bf = BusquedaFibonacci()
        for numero, indices_posibles in self.diccionario.items():
            an = Analysis()
            indice_buscado = bf.analizar(loa_cr, an, numero)
            self.assertIn(indice_buscado, indices_posibles)
            self.assertIs(an.inicializado_sin_intercambios(), True)


class ListaAleatoriaSinRepeticion(unittest.TestCase):
    diccionario = {k: la_sr[k] for k in range(tam)}

    def test_analisis_busqueda_lineal(self):
        """El análisis del algoritmo de búsqueda lineal debe devolver el índice donde se encuentra el elemento
        buscado en la lista aleatoria sin repetición de tamaño tam. Además el análisis debe tener algunos contadores
        mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado. """
        bl = BusquedaLineal()
        for indice, numero in self.diccionario.items():
            an = Analysis()
            indice_buscado = bl.analizar(la_sr, an, numero)
            self.assertEqual(indice, indice_buscado)
            self.assertIs(an.inicializado_sin_intercambios(), True)


class ListaAleatoriaConRepeticion(unittest.TestCase):
    diccionario = {k: [v for v in range(tam) if la_cr[v] == k] for k in set(la_cr)}

    def test_analisis_busqueda_lineal(self):
        """El análisis del algoritmo de búsqueda lineal debe devolver el índice donde se encuentra el elemento
        buscado en la lista aleatoria con posibles repeticiones de tamaño tam. Además el análisis debe tener algunos
        contadores mayores que 0 y otros deben seguir a 0, dependiendo del algoritmo analizado. """
        bl = BusquedaLineal()
        for numero, indices_posibles in self.diccionario.items():
            an = Analysis()
            indice_buscado = bl.analizar(la_cr, an, numero)
            self.assertIn(indice_buscado, indices_posibles)
            self.assertIs(an.inicializado_sin_intercambios(), True)


class EntradasErroneas(unittest.TestCase):
    numero = 0
    lista = [x for x in range(tam)]
    lista_no_ordenada = (
        5,
        8,
        84,
        165,
        2,
        6
    )
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
    no_enteros = (
        (1, 4),
        'm',
        True,
        {1: "value"},
        2.47,
        "cadena",
        [[0, 1], [8, 10]]
    )
    num_negativos = (
        -8,
        -3,
        -999999,
        -1
    )
    no_encuentra = (
        tam,
        tam+1,
        tam*2,
        tam**2
    )

    def test_busqueda_lineal_entrada_no_lista(self):
        """El análisis del algoritmo de búsqueda lineal debe fallar al recibir como entrada un objeto que no sea una
        lista o una secuencia inmutable tuple """
        bl = BusquedaLineal()
        for entrada_erronea in self.no_listas:
            an = Analysis()
            self.assertRaises(ex.EntradaNoLista, bl.analizar, entrada_erronea, an, self.numero)

    def test_busqueda_lineal_variable_busqueda_no_numero(self):
        """El análisis del algoritmo de búsqueda lineal debe fallar al recibir como entrada una variable de búsqueda
        que no sea un número entero"""
        bl = BusquedaLineal()
        for numero in self.no_enteros:
            an = Analysis()
            self.assertRaises(ex.ValorBusquedaNoNumeroEntero, bl.analizar, self.lista, an, numero)

    def test_busqueda_lineal_variable_busqueda_num_negativo(self):
        """El análisis del algoritmo de búsqueda lineal debe fallar al recibir como entrada una variable de búsqueda
        que sea un número entero negativo"""
        bl = BusquedaLineal()
        for numero in self.num_negativos:
            an = Analysis()
            self.assertRaises(ex.ValorBusquedaEnteroNegativo, bl.analizar, self.lista, an, numero)

    def test_busqueda_lineal_variable_busqueda_no_encontrada(self):
        """El análisis del algoritmo de búsqueda lineal debe fallar al no encontrar la variable de búsqueda"""
        bl = BusquedaLineal()
        for numero in self.no_encuentra:
            an = Analysis()
            self.assertRaises(ex.ValorBusquedaNoEncontrado, bl.analizar, self.lista, an, numero)

    def test_busqueda_binaria_entrada_no_lista(self):
        """El análisis del algoritmo de búsqueda binaria debe fallar al recibir como entrada un objeto que no sea
        una lista o una secuencia inmutable tuple"""
        bb = BusquedaBinaria()
        for entrada_erronea in self.no_listas:
            an = Analysis()
            self.assertRaises(ex.EntradaNoLista, bb.analizar, entrada_erronea, an, self.numero)

    def test_busqueda_binaria_variable_busqueda_no_numero(self):
        """El análisis del algoritmo de búsqueda binaria debe fallar al recibir como entrada una variable de búsqueda
        que no sea un número entero"""
        bb = BusquedaBinaria()
        for numero in self.no_enteros:
            an = Analysis()
            self.assertRaises(ex.ValorBusquedaNoNumeroEntero, bb.analizar, self.lista, an, numero)

    def test_busqueda_binaria_variable_busqueda_num_negativo(self):
        """El análisis del algoritmo de búsqueda binaria debe fallar al recibir como entrada una variable de búsqueda
        que sea un número entero negativo"""
        bb = BusquedaBinaria()
        for numero in self.num_negativos:
            an = Analysis()
            self.assertRaises(ex.ValorBusquedaEnteroNegativo, bb.analizar, self.lista, an, numero)

    def test_busqueda_binaria_variable_busqueda_no_encontrada(self):
        """El análisis del algoritmo de búsqueda binaria debe fallar al no encontrar la variable de búsqueda"""
        bb = BusquedaBinaria()
        for numero in self.no_encuentra:
            an = Analysis()
            self.assertRaises(ex.ValorBusquedaNoEncontrado, bb.analizar, self.lista, an, numero)

    def test_busqueda_binaria_lista_no_ordenada(self):
        """El análisis del algoritmo de búsqueda binaria debe fallar si recibe una lista no ordenada"""
        bb = BusquedaBinaria()
        an = Analysis()
        self.assertRaises(ex.ListaNoOrdenada, bb.analizar, self.lista_no_ordenada, an, self.numero)

    def test_busqueda_salto_entrada_no_lista(self):
        """El análisis del algoritmo de búsqueda salto debe fallar al recibir como entrada un objeto que no sea
        una lista o una secuencia inmutable tuple"""
        bs = BusquedaSalto()
        for entrada_erronea in self.no_listas:
            an = Analysis()
            self.assertRaises(ex.EntradaNoLista, bs.analizar, entrada_erronea, an, self.numero)

    def test_busqueda_salto_variable_busqueda_no_numero(self):
        """El análisis del algoritmo de búsqueda salto debe fallar al recibir como entrada una variable de búsqueda
        que no sea un número entero"""
        bs = BusquedaSalto()
        for numero in self.no_enteros:
            an = Analysis()
            self.assertRaises(ex.ValorBusquedaNoNumeroEntero, bs.analizar, self.lista, an, numero)

    def test_busqueda_salto_variable_busqueda_num_negativo(self):
        """El análisis del algoritmo de búsqueda salto debe fallar al recibir como entrada una variable de búsqueda
        que sea un número entero negativo"""
        bs = BusquedaSalto()
        for numero in self.num_negativos:
            an = Analysis()
            self.assertRaises(ex.ValorBusquedaEnteroNegativo, bs.analizar, self.lista, an, numero)

    def test_busqueda_salto_variable_busqueda_no_encontrada(self):
        """El análisis del algoritmo de búsqueda salto debe fallar al no encontrar la variable de búsqueda"""
        bs = BusquedaSalto()
        for numero in self.no_encuentra:
            an = Analysis()
            self.assertRaises(ex.ValorBusquedaNoEncontrado, bs.analizar, self.lista, an, numero)

    def test_busqueda_salto_lista_no_ordenada(self):
        """El análisis del algoritmo de búsqueda salto debe fallar si recibe una lista no ordenada"""
        bs = BusquedaSalto()
        an = Analysis()
        self.assertRaises(ex.ListaNoOrdenada, bs.analizar, self.lista_no_ordenada, an, self.numero)

    def test_busqueda_interpolacion_entrada_no_lista(self):
        """El análisis del algoritmo de búsqueda interpolacion debe fallar al recibir como entrada un objeto que no sea
        una lista o una secuencia inmutable tuple"""
        bi = BusquedaInterpolacion()
        for entrada_erronea in self.no_listas:
            an = Analysis()
            self.assertRaises(ex.EntradaNoLista, bi.analizar, entrada_erronea, an, self.numero)

    def test_busqueda_interpolacion_variable_busqueda_no_numero(self):
        """El análisis del algoritmo de búsqueda interpolacion debe fallar al recibir como entrada una variable de
        búsqueda que no sea un número entero"""
        bi = BusquedaInterpolacion()
        for numero in self.no_enteros:
            an = Analysis()
            self.assertRaises(ex.ValorBusquedaNoNumeroEntero, bi.analizar, self.lista, an, numero)

    def test_busqueda_interpolacion_variable_busqueda_num_negativo(self):
        """El análisis del algoritmo de búsqueda interpolacion debe fallar al recibir como entrada una variable de
        búsqueda que sea un número entero negativo"""
        bi = BusquedaInterpolacion()
        for numero in self.num_negativos:
            an = Analysis()
            self.assertRaises(ex.ValorBusquedaEnteroNegativo, bi.analizar, self.lista, an, numero)

    def test_busqueda_interpolacion_variable_busqueda_no_encontrada(self):
        """El análisis del algoritmo de búsqueda interpolacion debe fallar al no encontrar la variable de búsqueda"""
        bi = BusquedaInterpolacion()
        for numero in self.no_encuentra:
            an = Analysis()
            self.assertRaises(ex.ValorBusquedaNoEncontrado, bi.analizar, self.lista, an, numero)

    def test_busqueda_interpolacion_lista_no_ordenada(self):
        """El análisis del algoritmo de búsqueda interpolacion debe fallar si recibe una lista no ordenada"""
        bi = BusquedaInterpolacion()
        an = Analysis()
        self.assertRaises(ex.ListaNoOrdenada, bi.analizar, self.lista_no_ordenada, an, self.numero)

    def test_busqueda_exponencial_entrada_no_lista(self):
        """El análisis del algoritmo de búsqueda exponencial debe fallar al recibir como entrada un objeto que no sea
        una lista o una secuencia inmutable tuple"""
        be = BusquedaExponencial()
        for entrada_erronea in self.no_listas:
            an = Analysis()
            self.assertRaises(ex.EntradaNoLista, be.analizar, entrada_erronea, an, self.numero)

    def test_busqueda_exponencial_variable_busqueda_no_numero(self):
        """El análisis del algoritmo de búsqueda exponencial debe fallar al recibir como entrada una variable de
        búsqueda que no sea un número entero"""
        be = BusquedaExponencial()
        for numero in self.no_enteros:
            an = Analysis()
            self.assertRaises(ex.ValorBusquedaNoNumeroEntero, be.analizar, self.lista, an, numero)

    def test_busqueda_exponencial_variable_busqueda_num_negativo(self):
        """El análisis del algoritmo de búsqueda exponencial debe fallar al recibir como entrada una variable de
        búsqueda que sea un número entero negativo"""
        be = BusquedaExponencial()
        for numero in self.num_negativos:
            an = Analysis()
            self.assertRaises(ex.ValorBusquedaEnteroNegativo, be.analizar, self.lista, an, numero)

    def test_busqueda_exponencial_variable_busqueda_no_encontrada(self):
        """El análisis del algoritmo de búsqueda exponencial debe fallar al no encontrar la variable de búsqueda"""
        be = BusquedaExponencial()
        for numero in self.no_encuentra:
            an = Analysis()
            self.assertRaises(ex.ValorBusquedaNoEncontrado, be.analizar, self.lista, an, numero)

    def test_busqueda_exponencial_lista_no_ordenada(self):
        """El análisis del algoritmo de búsqueda exponencial debe fallar si recibe una lista no ordenada"""
        be = BusquedaExponencial()
        an = Analysis()
        self.assertRaises(ex.ListaNoOrdenada, be.analizar, self.lista_no_ordenada, an, self.numero)

    def test_busqueda_fibonacci_entrada_no_lista(self):
        """El análisis del algoritmo de búsqueda fibonacci debe fallar al recibir como entrada un objeto que no sea
        una lista o una secuencia inmutable tuple"""
        bf = BusquedaFibonacci()
        for entrada_erronea in self.no_listas:
            an = Analysis()
            self.assertRaises(ex.EntradaNoLista, bf.analizar, entrada_erronea, an, self.numero)

    def test_busqueda_fibonacci_variable_busqueda_no_numero(self):
        """El análisis del algoritmo de búsqueda fibonacci debe fallar al recibir como entrada una variable de
        búsqueda que no sea un número entero"""
        bf = BusquedaFibonacci()
        for numero in self.no_enteros:
            an = Analysis()
            self.assertRaises(ex.ValorBusquedaNoNumeroEntero, bf.analizar, self.lista, an, numero)

    def test_busqueda_fibonacci_variable_busqueda_num_negativo(self):
        """El análisis del algoritmo de búsqueda fibonacci debe fallar al recibir como entrada una variable de
        búsqueda que sea un número entero negativo"""
        bf = BusquedaFibonacci()
        for numero in self.num_negativos:
            an = Analysis()
            self.assertRaises(ex.ValorBusquedaEnteroNegativo, bf.analizar, self.lista, an, numero)

    def test_busqueda_fibonacci_variable_busqueda_no_encontrada(self):
        """El análisis del algoritmo de búsqueda fibonacci debe fallar al no encontrar la variable de búsqueda"""
        bf = BusquedaFibonacci()
        for numero in self.no_encuentra:
            an = Analysis()
            self.assertRaises(ex.ValorBusquedaNoEncontrado, bf.analizar, self.lista, an, numero)

    def test_busqueda_fibonacci_lista_no_ordenada(self):
        """El análisis del algoritmo de búsqueda fibonacci debe fallar si recibe una lista no ordenada"""
        bf = BusquedaFibonacci()
        an = Analysis()
        self.assertRaises(ex.ListaNoOrdenada, bf.analizar, self.lista_no_ordenada, an, self.numero)


if __name__ == '__main__':
    unittest.main()
