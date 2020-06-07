import bin.excepciones as ex


def comprobar_data_input(data_input):
    if not (isinstance(data_input, tuple) or isinstance(data_input, list)):
        raise ex.EntradaNoLista("La entrada no es ni una lista ni una secuencia inmutable 'tuple'")
    if len(data_input) == 0:
        raise ex.EntradaNoLista("La entrada no puede ser una lista vacía")
    if not isinstance(data_input[0], int):
        raise ex.EntradaNoLista("La entrada no puede ser una lista múltiple (con más de una fila)")


def comprobar_valor_busqueda(valor_busqueda):
    if not isinstance(valor_busqueda, int) or isinstance(valor_busqueda, bool):
        raise ex.ValorBusquedaNoNumeroEntero("La variable de búsqueda solo puede ser un número entero")
    if valor_busqueda < 0:
        raise ex.ValorBusquedaEnteroNegativo("La variable de búsqueda no puede ser un número entero negativo")


def comprobar_ejecucion_busqueda(data_input, valor_busqueda):
    """Realiza las comprobaciones básicas de la ejecución de una búsqueda y, si fallan, lanzan una excepción"""
    comprobar_data_input(data_input)
    comprobar_valor_busqueda(valor_busqueda)


def comprobar_analisis_busqueda(data_input, valor_busqueda, analysis):
    """Realiza las comprobaciones básicas del análisis de una búsqueda y, si fallan, lanzan una excepción"""
    comprobar_ejecucion_busqueda(data_input, valor_busqueda)


def comprobar_analisis_ordenacion(data_input, analysis):
    """Realiza las comprobaciones básicas del análisis de una ordenación y, si fallan, lanzan una excepción"""
    comprobar_ejecucion_ordenacion(data_input)


def comprobar_lista_ordenada_busqueda(data_input):
    """Comprueba que la lista en la que se va a buscar un valor está ordenada y, si no lo está, lanza una excepción"""
    num_anterior = -1
    for numero in data_input:
        if numero < num_anterior:
            raise ex.ListaNoOrdenada("Este algoritmo requiere de una lista previamente ordenada para la búsqueda")
        num_anterior = numero


def comprobar_ejecucion_ordenacion(data_input):
    """Realiza las comprobaciones básicas de la ejecución de una ordenación y, si fallan, lanzan una excepción"""
    comprobar_data_input(data_input)
