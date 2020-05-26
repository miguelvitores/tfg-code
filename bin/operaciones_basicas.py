import random


def mezclar_aleatorio(lista):
    lista = list(lista)
    tam = len(lista)
    for i in range(tam):
        b = random.randint(i, tam - 1)
        intercambiar(lista, i, b)
    return lista


def intercambiar(lista, a, b):
    tmp = lista[a]
    lista[a] = lista[b]
    lista[b] = tmp
