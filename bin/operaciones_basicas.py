import random
from bin.analysis import Analysis


def mezclar_aleatorio(lista):
    lista = list(lista)
    tam = len(lista)
    for i in range(tam):
        b = random.randint(i, tam - 1)
        intercambiar(lista, i, b)
    return lista


def mezclar_aleatorio_analisis(lista, an: Analysis):
    lista = list(lista)

    an.sum_declaracion(1)
    tam = len(lista)

    an.sum_declaracion(1)
    for i in range(tam):
        an.sum_co(1)

        an.sum_te(1)
        b = random.randint(i, tam - 1)

        an.sum_intercambio_misma_lista(1)
        intercambiar(lista, i, b)
        an.sum_te(1)
    an.sum_co(1)

    return lista


def intercambiar(lista, a, b):
    tmp = lista[a]
    lista[a] = lista[b]
    lista[b] = tmp
