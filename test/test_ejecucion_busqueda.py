import unittest
import bin.crear_lista as cl
import bin.excepciones as ex
from bin.algoritmos.busq.busquedalineal import BusquedaLineal
from bin.algoritmos.busq.busquedabinaria import BusquedaBinaria
from bin.algoritmos.busq.busquedasalto import BusquedaSalto
from bin.algoritmos.busq.busquedainterpolacion import BusquedaInterpolacion
from bin.algoritmos.busq.busquedaexponencial import BusquedaExponencial
from bin.algoritmos.busq.busquedafibonacci import BusquedaFibonacci

tam = 256
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

    def test_ejecucion_busqueda_lineal_lista_desordenada(self):
        """La ejecución del algoritmo de búsqueda lineal debe devolver el índice donde se encuentra el elemento buscado
         en la lista conocida"""
        bl = BusquedaLineal()
        for numero, indice in self.indices:
            indice_buscado = bl.ejecutar(self.lista_desordenada, numero)
            self.assertEqual(indice, indice_buscado)

    def test_ejecucion_busqueda_lineal_un_elemento(self):
        """La ejecución del algoritmo de búsqueda lineal debe devolver el índice donde se encuentra el elemento buscado
         en la lista conocida con un solo elemento"""
        bl = BusquedaLineal()
        indice_buscado = bl.ejecutar(self.lo1, self.indices1[1])
        self.assertEqual(self.indices1[0], indice_buscado)

    def test_ejecucion_busqueda_binaria_un_elemento(self):
        """La ejecución del algoritmo de búsqueda binaria debe devolver el índice donde se encuentra el elemento buscado
        en la lista conocida con un solo elemento"""
        bb = BusquedaBinaria()
        indice_buscado = bb.ejecutar(self.lo1, self.indices1[1])
        self.assertEqual(self.indices1[0], indice_buscado)

    def test_ejecucion_busqueda_salto_un_elemento(self):
        """La ejecución del algoritmo de búsqueda salto debe devolver el índice donde se encuentra el elemento buscado
        en la lista conocida con un solo elemento"""
        bs = BusquedaSalto()
        indice_buscado = bs.ejecutar(self.lo1, self.indices1[1])
        self.assertEqual(self.indices1[0], indice_buscado)

    def test_ejecucion_busqueda_interpolacion_un_elemento(self):
        """La ejecución del algoritmo de búsqueda interpolacion debe devolver el índice donde se encuentra el elemento
        en la lista conocida con un solo elemento"""
        bi = BusquedaInterpolacion()
        indice_buscado = bi.ejecutar(self.lo1, self.indices1[1])
        self.assertEqual(self.indices1[0], indice_buscado)

    def test_ejecucion_busqueda_exponencial_un_elemento(self):
        """La ejecución del algoritmo de búsqueda exponencial debe devolver el índice donde se encuentra el elemento
        en la lista conocida con un solo elemento"""
        be = BusquedaExponencial()
        indice_buscado = be.ejecutar(self.lo1, self.indices1[1])
        self.assertEqual(self.indices1[0], indice_buscado)

    def test_ejecucion_busqueda_fibonacci_un_elemento(self):
        """La ejecución del algoritmo de búsqueda fibonacci debe devolver el índice donde se encuentra el elemento
        en la lista conocida con un solo elemento"""
        bf = BusquedaFibonacci()
        indice_buscado = bf.ejecutar(self.lo1, self.indices1[1])
        self.assertEqual(self.indices1[0], indice_buscado)

    def test_ejecucion_busqueda_lineal_dos_elementos_iguales(self):
        """La ejecución del algoritmo de búsqueda lineal debe devolver el índice donde se encuentra el elemento buscado
         en la lista conocida con dos elementos iguales"""
        bl = BusquedaLineal()
        indice_buscado = bl.ejecutar(self.lo2, self.indices2[1])
        self.assertIn(indice_buscado, self.indices2[0])

    def test_ejecucion_busqueda_binaria_dos_elementos_iguales(self):
        """La ejecución del algoritmo de búsqueda binaria debe devolver el índice donde se encuentra el elemento buscado
        en la lista conocida con dos elementos iguales"""
        bb = BusquedaBinaria()
        indice_buscado = bb.ejecutar(self.lo2, self.indices2[1])
        self.assertIn(indice_buscado, self.indices2[0])

    def test_ejecucion_busqueda_salto_dos_elementos_iguales(self):
        """La ejecución del algoritmo de búsqueda salto debe devolver el índice donde se encuentra el elemento buscado
        en la lista conocida con dos elementos iguales"""
        bs = BusquedaSalto()
        indice_buscado = bs.ejecutar(self.lo2, self.indices2[1])
        self.assertIn(indice_buscado, self.indices2[0])

    def test_ejecucion_busqueda_interpolacion_dos_elementos_iguales(self):
        """La ejecución del algoritmo de búsqueda interpolacion debe devolver el índice donde se encuentra el elemento
        en la lista conocida con dos elementos iguales"""
        bi = BusquedaInterpolacion()
        indice_buscado = bi.ejecutar(self.lo2, self.indices2[1])
        self.assertIn(indice_buscado, self.indices2[0])

    def test_ejecucion_busqueda_exponencial_dos_elementos_iguales(self):
        """La ejecución del algoritmo de búsqueda exponencial debe devolver el índice donde se encuentra el elemento
        en la lista conocida con dos elementos iguales"""
        be = BusquedaExponencial()
        indice_buscado = be.ejecutar(self.lo2, self.indices2[1])
        self.assertIn(indice_buscado, self.indices2[0])

    def test_ejecucion_busqueda_fibonacci_dos_elementos_iguales(self):
        """La ejecución del algoritmo de búsqueda fibonacci debe devolver el índice donde se encuentra el elemento
        en la lista conocida con dos elementos iguales"""
        bf = BusquedaFibonacci()
        indice_buscado = bf.ejecutar(self.lo2, self.indices2[1])
        self.assertIn(indice_buscado, self.indices2[0])


class ListaOrdenada(unittest.TestCase):
    indices = [(x, x * 4) for x in range(tam)]
    lista_ordenada = [num for i, num in indices]

    def test_ejecucion_busqueda_lineal(self):
        """La ejecución del algoritmo de búsqueda lineal debe devolver el índice donde se encuentra el elemento buscado
         en la lista ordenada indice * 4 de tamaño tam"""
        bl = BusquedaLineal()
        for indice, numero in self.indices:
            indice_buscado = bl.ejecutar(self.lista_ordenada, numero)
            self.assertEqual(indice, indice_buscado)

    def test_ejecucion_busqueda_binaria(self):
        """La ejecución del algoritmo de búsqueda binaria debe devolver el índice donde se encuentra el elemento buscado
         en la lista ordenada indice * 4 de tamaño tam"""
        bb = BusquedaBinaria()
        for indice, numero in self.indices:
            indice_buscado = bb.ejecutar(self.lista_ordenada, numero)
            self.assertEqual(indice, indice_buscado)

    def test_ejecucion_busqueda_salto(self):
        """La ejecución del algoritmo de búsqueda salto debe devolver el índice donde se encuentra el elemento buscado
         en la lista ordenada indice * 4 de tamaño tam"""
        bs = BusquedaSalto()
        for indice, numero in self.indices:
            indice_buscado = bs.ejecutar(self.lista_ordenada, numero)
            self.assertEqual(indice, indice_buscado)

    def test_ejecucion_busqueda_interpolacion(self):
        """La ejecución del algoritmo de búsqueda interpolacion debe devolver el índice donde se encuentra el elemento
        buscado en la lista ordenada indice * 4 de tamaño tam"""
        bi = BusquedaInterpolacion()
        for indice, numero in self.indices:
            indice_buscado = bi.ejecutar(self.lista_ordenada, numero)
            self.assertEqual(indice, indice_buscado)

    def test_ejecucion_busqueda_exponencial(self):
        """La ejecución del algoritmo de búsqueda exponencial debe devolver el índice donde se encuentra el elemento
        buscado en la lista ordenada indice * 4 de tamaño tam"""
        be = BusquedaExponencial()
        for indice, numero in self.indices:
            indice_buscado = be.ejecutar(self.lista_ordenada, numero)
            self.assertEqual(indice, indice_buscado)

    def test_ejecucion_busqueda_fibonacci(self):
        """La ejecución del algoritmo de búsqueda fibonacci debe devolver el índice donde se encuentra el elemento
        buscado en la lista ordenada indice * 4 de tamaño tam"""
        bf = BusquedaFibonacci()
        for indice, numero in self.indices:
            indice_buscado = bf.ejecutar(self.lista_ordenada, numero)
            self.assertEqual(indice, indice_buscado)


class ListaOrdenadaAleatoriaSinRepeticion(unittest.TestCase):
    diccionario = {k: loa_sr[k] for k in range(tam)}

    def test_ejecucion_busqueda_lineal(self):
        """La ejecución del algoritmo de búsqueda lineal debe devolver el índice donde se encuentra el elemento buscado
         en la lista ordenada aleatoria sin repetición"""
        bl = BusquedaLineal()
        for indice, numero in self.diccionario.items():
            indice_buscado = bl.ejecutar(loa_sr, numero)
            self.assertEqual(indice, indice_buscado)

    def test_ejecucion_busqueda_binaria(self):
        """La ejecución del algoritmo de búsqueda binaria debe devolver el índice donde se encuentra el elemento buscado
         en la lista ordenada aleatoria sin repetición"""
        bb = BusquedaBinaria()
        for indice, numero in self.diccionario.items():
            indice_buscado = bb.ejecutar(loa_sr, numero)
            self.assertEqual(indice, indice_buscado)

    def test_ejecucion_busqueda_salto(self):
        """La ejecución del algoritmo de búsqueda salto debe devolver el índice donde se encuentra el elemento buscado
         en la lista ordenada aleatoria sin repetición"""
        bs = BusquedaSalto()
        for indice, numero in self.diccionario.items():
            indice_buscado = bs.ejecutar(loa_sr, numero)
            self.assertEqual(indice, indice_buscado)

    def test_ejecucion_busqueda_interpolacion(self):
        """La ejecución del algoritmo de búsqueda interpolacion debe devolver el índice donde se encuentra el elemento
        buscado en la lista ordenada aleatoria sin repetición"""
        bi = BusquedaInterpolacion()
        for indice, numero in self.diccionario.items():
            indice_buscado = bi.ejecutar(loa_sr, numero)
            self.assertEqual(indice, indice_buscado)

    def test_ejecucion_busqueda_exponencial(self):
        """La ejecución del algoritmo de búsqueda exponencial debe devolver el índice donde se encuentra el elemento
        buscado en la lista ordenada aleatoria sin repetición"""
        be = BusquedaExponencial()
        for indice, numero in self.diccionario.items():
            indice_buscado = be.ejecutar(loa_sr, numero)
            self.assertEqual(indice, indice_buscado)

    def test_ejecucion_busqueda_fibonacci(self):
        """La ejecución del algoritmo de búsqueda fibonacci debe devolver el índice donde se encuentra el elemento
        buscado en la lista ordenada aleatoria sin repetición"""
        bf = BusquedaFibonacci()
        for indice, numero in self.diccionario.items():
            indice_buscado = bf.ejecutar(loa_sr, numero)
            self.assertEqual(indice, indice_buscado)


class ListaOrdenadaAleatoriaConRepeticion(unittest.TestCase):
    diccionario = {k: [v for v in range(tam) if loa_cr[v] == k] for k in set(loa_cr)}

    def test_ejecucion_busqueda_lineal(self):
        """La ejecución del algoritmo de búsqueda lineal debe devolver el índice donde se encuentra el elemento buscado
         en la lista ordenada aleatoria con repetición"""
        bl = BusquedaLineal()
        for numero, indices_posibles in self.diccionario.items():
            indice_buscado = bl.ejecutar(loa_cr, numero)
            self.assertIn(indice_buscado, indices_posibles)

    def test_ejecucion_busqueda_binaria(self):
        """La ejecución del algoritmo de búsqueda binaria debe devolver el índice donde se encuentra el elemento buscado
         en la lista ordenada aleatoria con repetición"""
        bb = BusquedaBinaria()
        for numero, indices_posibles in self.diccionario.items():
            indice_buscado = bb.ejecutar(loa_cr, numero)
            self.assertIn(indice_buscado, indices_posibles)

    def test_ejecucion_busqueda_salto(self):
        """La ejecución del algoritmo de búsqueda salto debe devolver el índice donde se encuentra el elemento buscado
         en la lista ordenada aleatoria con repetición"""
        bs = BusquedaSalto()
        for numero, indices_posibles in self.diccionario.items():
            indice_buscado = bs.ejecutar(loa_cr, numero)
            self.assertIn(indice_buscado, indices_posibles)

    def test_ejecucion_busqueda_interpolacion(self):
        """La ejecución del algoritmo de búsqueda interpolacion debe devolver el índice donde se encuentra el elemento
        buscado en la lista ordenada aleatoria con repetición"""
        bi = BusquedaInterpolacion()
        for numero, indices_posibles in self.diccionario.items():
            indice_buscado = bi.ejecutar(loa_cr, numero)
            self.assertIn(indice_buscado, indices_posibles)

    def test_ejecucion_busqueda_exponencial(self):
        """La ejecución del algoritmo de búsqueda exponencial debe devolver el índice donde se encuentra el elemento
        buscado en la lista ordenada aleatoria con repetición"""
        be = BusquedaExponencial()
        for numero, indices_posibles in self.diccionario.items():
            indice_buscado = be.ejecutar(loa_cr, numero)
            self.assertIn(indice_buscado, indices_posibles)

    def test_ejecucion_busqueda_fibonacci(self):
        """La ejecución del algoritmo de búsqueda fibonacci debe devolver el índice donde se encuentra el elemento
        buscado en la lista ordenada aleatoria con repetición"""
        bf = BusquedaFibonacci()
        for numero, indices_posibles in self.diccionario.items():
            indice_buscado = bf.ejecutar(loa_cr, numero)
            self.assertIn(indice_buscado, indices_posibles)


class ListaAleatoriaSinRepeticion(unittest.TestCase):
    diccionario = {k: la_sr[k] for k in range(tam)}

    def test_ejecucion_busqueda_lineal(self):
        """La ejecución del algoritmo de búsqueda lineal debe devolver el índice donde se encuentra el elemento buscado
         en la lista aleatoria sin repetición de tamaño tam"""
        bl = BusquedaLineal()
        for indice, numero in self.diccionario.items():
            indice_buscado = bl.ejecutar(la_sr, numero)
            self.assertEqual(indice, indice_buscado)


class ListaAleatoriaConRepeticion(unittest.TestCase):
    diccionario = {k: [v for v in range(tam) if la_cr[v] == k] for k in set(la_cr)}

    def test_ejecucion_busqueda_lineal(self):
        """La ejecución del algoritmo de búsqueda lineal debe devolver el índice donde se encuentra el elemento buscado
         en la lista aleatoria con posibles repeticiones de tamaño tam"""
        bl = BusquedaLineal()
        for numero, indices_posibles in self.diccionario.items():
            indice_buscado = bl.ejecutar(la_cr, numero)
            self.assertIn(indice_buscado, indices_posibles)


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
        """La ejecución del algoritmo de búsqueda lineal debe fallar al recibir como entrada un objeto que no sea una
        lista o una secuencia inmutable tuple """
        bl = BusquedaLineal()
        for entrada_erronea in self.no_listas:
            self.assertRaises(ex.EntradaNoLista, bl.ejecutar, entrada_erronea, self.numero)

    def test_busqueda_lineal_variable_busqueda_no_numero(self):
        """La ejecución del algoritmo de búsqueda lineal debe fallar al recibir como entrada una variable de búsqueda
        que no sea un número entero"""
        bl = BusquedaLineal()
        for numero in self.no_enteros:
            self.assertRaises(ex.ValorBusquedaNoNumeroEntero, bl.ejecutar, self.lista, numero)

    def test_busqueda_lineal_variable_busqueda_num_negativo(self):
        """La ejecución del algoritmo de búsqueda lineal debe fallar al recibir como entrada una variable de búsqueda
        que sea un número entero negativo"""
        bl = BusquedaLineal()
        for numero in self.num_negativos:
            self.assertRaises(ex.ValorBusquedaEnteroNegativo, bl.ejecutar, self.lista, numero)

    def test_busqueda_lineal_variable_busqueda_no_encontrada(self):
        """La ejecución del algoritmo de búsqueda lineal debe fallar al no encontrar la variable de búsqueda"""
        bl = BusquedaLineal()
        for numero in self.no_encuentra:
            self.assertRaises(ex.ValorBusquedaNoEncontrado, bl.ejecutar, self.lista, numero)

    def test_busqueda_binaria_entrada_no_lista(self):
        """La ejecución del algoritmo de búsqueda binaria debe fallar al recibir como entrada un objeto que no sea
        una lista o una secuencia inmutable tuple"""
        bb = BusquedaBinaria()
        for entrada_erronea in self.no_listas:
            self.assertRaises(ex.EntradaNoLista, bb.ejecutar, entrada_erronea, self.numero)

    def test_busqueda_binaria_variable_busqueda_no_numero(self):
        """La ejecución del algoritmo de búsqueda binaria debe fallar al recibir como entrada una variable de búsqueda
        que no sea un número entero"""
        bb = BusquedaBinaria()
        for numero in self.no_enteros:
            self.assertRaises(ex.ValorBusquedaNoNumeroEntero, bb.ejecutar, self.lista, numero)

    def test_busqueda_binaria_variable_busqueda_num_negativo(self):
        """La ejecución del algoritmo de búsqueda binaria debe fallar al recibir como entrada una variable de búsqueda
        que sea un número entero negativo"""
        bb = BusquedaBinaria()
        for numero in self.num_negativos:
            self.assertRaises(ex.ValorBusquedaEnteroNegativo, bb.ejecutar, self.lista, numero)

    def test_busqueda_binaria_variable_busqueda_no_encontrada(self):
        """La ejecución del algoritmo de búsqueda binaria debe fallar al no encontrar la variable de búsqueda"""
        bb = BusquedaBinaria()
        for numero in self.no_encuentra:
            self.assertRaises(ex.ValorBusquedaNoEncontrado, bb.ejecutar, self.lista, numero)

    def test_busqueda_binaria_lista_no_ordenada(self):
        """La ejecución del algoritmo de búsqueda binaria debe fallar si recibe una lista no ordenada"""
        bb = BusquedaBinaria()
        self.assertRaises(ex.ListaNoOrdenada, bb.ejecutar, self.lista_no_ordenada, self.numero)

    def test_busqueda_salto_entrada_no_lista(self):
        """La ejecución del algoritmo de búsqueda salto debe fallar al recibir como entrada un objeto que no sea
        una lista o una secuencia inmutable tuple"""
        bs = BusquedaSalto()
        for entrada_erronea in self.no_listas:
            self.assertRaises(ex.EntradaNoLista, bs.ejecutar, entrada_erronea, self.numero)

    def test_busqueda_salto_variable_busqueda_no_numero(self):
        """La ejecución del algoritmo de búsqueda salto debe fallar al recibir como entrada una variable de búsqueda
        que no sea un número entero"""
        bs = BusquedaSalto()
        for numero in self.no_enteros:
            self.assertRaises(ex.ValorBusquedaNoNumeroEntero, bs.ejecutar, self.lista, numero)

    def test_busqueda_salto_variable_busqueda_num_negativo(self):
        """La ejecución del algoritmo de búsqueda salto debe fallar al recibir como entrada una variable de búsqueda
        que sea un número entero negativo"""
        bs = BusquedaSalto()
        for numero in self.num_negativos:
            self.assertRaises(ex.ValorBusquedaEnteroNegativo, bs.ejecutar, self.lista, numero)

    def test_busqueda_salto_variable_busqueda_no_encontrada(self):
        """La ejecución del algoritmo de búsqueda salto debe fallar al no encontrar la variable de búsqueda"""
        bs = BusquedaSalto()
        for numero in self.no_encuentra:
            self.assertRaises(ex.ValorBusquedaNoEncontrado, bs.ejecutar, self.lista, numero)

    def test_busqueda_salto_lista_no_ordenada(self):
        """La ejecución del algoritmo de búsqueda salto debe fallar si recibe una lista no ordenada"""
        bs = BusquedaSalto()
        self.assertRaises(ex.ListaNoOrdenada, bs.ejecutar, self.lista_no_ordenada, self.numero)

    def test_busqueda_interpolacion_entrada_no_lista(self):
        """La ejecución del algoritmo de búsqueda interpolacion debe fallar al recibir como entrada un objeto que no sea
        una lista o una secuencia inmutable tuple"""
        bi = BusquedaInterpolacion()
        for entrada_erronea in self.no_listas:
            self.assertRaises(ex.EntradaNoLista, bi.ejecutar, entrada_erronea, self.numero)

    def test_busqueda_interpolacion_variable_busqueda_no_numero(self):
        """La ejecución del algoritmo de búsqueda interpolacion debe fallar al recibir como entrada una variable de
        búsqueda que no sea un número entero"""
        bi = BusquedaInterpolacion()
        for numero in self.no_enteros:
            self.assertRaises(ex.ValorBusquedaNoNumeroEntero, bi.ejecutar, self.lista, numero)

    def test_busqueda_interpolacion_variable_busqueda_num_negativo(self):
        """La ejecución del algoritmo de búsqueda interpolacion debe fallar al recibir como entrada una variable de
        búsqueda que sea un número entero negativo"""
        bi = BusquedaInterpolacion()
        for numero in self.num_negativos:
            self.assertRaises(ex.ValorBusquedaEnteroNegativo, bi.ejecutar, self.lista, numero)

    def test_busqueda_interpolacion_variable_busqueda_no_encontrada(self):
        """La ejecución del algoritmo de búsqueda interpolacion debe fallar al no encontrar la variable de búsqueda"""
        bi = BusquedaInterpolacion()
        for numero in self.no_encuentra:
            self.assertRaises(ex.ValorBusquedaNoEncontrado, bi.ejecutar, self.lista, numero)

    def test_busqueda_interpolacion_lista_no_ordenada(self):
        """La ejecución del algoritmo de búsqueda interpolacion debe fallar si recibe una lista no ordenada"""
        bi = BusquedaInterpolacion()
        self.assertRaises(ex.ListaNoOrdenada, bi.ejecutar, self.lista_no_ordenada, self.numero)

    def test_busqueda_exponencial_entrada_no_lista(self):
        """La ejecución del algoritmo de búsqueda exponencial debe fallar al recibir como entrada un objeto que no sea
        una lista o una secuencia inmutable tuple"""
        be = BusquedaExponencial()
        for entrada_erronea in self.no_listas:
            self.assertRaises(ex.EntradaNoLista, be.ejecutar, entrada_erronea, self.numero)

    def test_busqueda_exponencial_variable_busqueda_no_numero(self):
        """La ejecución del algoritmo de búsqueda exponencial debe fallar al recibir como entrada una variable de
        búsqueda que no sea un número entero"""
        be = BusquedaExponencial()
        for numero in self.no_enteros:
            self.assertRaises(ex.ValorBusquedaNoNumeroEntero, be.ejecutar, self.lista, numero)

    def test_busqueda_exponencial_variable_busqueda_num_negativo(self):
        """La ejecución del algoritmo de búsqueda exponencial debe fallar al recibir como entrada una variable de
        búsqueda que sea un número entero negativo"""
        be = BusquedaExponencial()
        for numero in self.num_negativos:
            self.assertRaises(ex.ValorBusquedaEnteroNegativo, be.ejecutar, self.lista, numero)

    def test_busqueda_exponencial_variable_busqueda_no_encontrada(self):
        """La ejecución del algoritmo de búsqueda exponencial debe fallar al no encontrar la variable de búsqueda"""
        be = BusquedaExponencial()
        for numero in self.no_encuentra:
            self.assertRaises(ex.ValorBusquedaNoEncontrado, be.ejecutar, self.lista, numero)

    def test_busqueda_exponencial_lista_no_ordenada(self):
        """La ejecución del algoritmo de búsqueda exponencial debe fallar si recibe una lista no ordenada"""
        be = BusquedaExponencial()
        self.assertRaises(ex.ListaNoOrdenada, be.ejecutar, self.lista_no_ordenada, self.numero)

    def test_busqueda_fibonacci_entrada_no_lista(self):
        """La ejecución del algoritmo de búsqueda fibonacci debe fallar al recibir como entrada un objeto que no sea
        una lista o una secuencia inmutable tuple"""
        bf = BusquedaFibonacci()
        for entrada_erronea in self.no_listas:
            self.assertRaises(ex.EntradaNoLista, bf.ejecutar, entrada_erronea, self.numero)

    def test_busqueda_fibonacci_variable_busqueda_no_numero(self):
        """La ejecución del algoritmo de búsqueda fibonacci debe fallar al recibir como entrada una variable de
        búsqueda que no sea un número entero"""
        bf = BusquedaFibonacci()
        for numero in self.no_enteros:
            self.assertRaises(ex.ValorBusquedaNoNumeroEntero, bf.ejecutar, self.lista, numero)

    def test_busqueda_fibonacci_variable_busqueda_num_negativo(self):
        """La ejecución del algoritmo de búsqueda fibonacci debe fallar al recibir como entrada una variable de
        búsqueda que sea un número entero negativo"""
        bf = BusquedaFibonacci()
        for numero in self.num_negativos:
            self.assertRaises(ex.ValorBusquedaEnteroNegativo, bf.ejecutar, self.lista, numero)

    def test_busqueda_fibonacci_variable_busqueda_no_encontrada(self):
        """La ejecución del algoritmo de búsqueda fibonacci debe fallar al no encontrar la variable de búsqueda"""
        bf = BusquedaFibonacci()
        for numero in self.no_encuentra:
            self.assertRaises(ex.ValorBusquedaNoEncontrado, bf.ejecutar, self.lista, numero)

    def test_busqueda_fibonacci_lista_no_ordenada(self):
        """La ejecución del algoritmo de búsqueda fibonacci debe fallar si recibe una lista no ordenada"""
        bf = BusquedaFibonacci()
        self.assertRaises(ex.ListaNoOrdenada, bf.ejecutar, self.lista_no_ordenada, self.numero)


if __name__ == '__main__':
    unittest.main()
