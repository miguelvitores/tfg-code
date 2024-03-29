import random
import math
import bin.operaciones_basicas as ob


def ordenada(minimo, maximo):
    return [c for c in range(minimo, maximo)]


def ordenada_equidistante(minimo, maximo, num):
    salto = (maximo - minimo) / max(num - 1, 1)
    return [math.floor(c * salto + minimo) for c in range(num)]


def aleatoria(minimo, maximo, n):
    return [random.randint(minimo, maximo) for c in range(n)]


def aleatoria_sin_repeticion(minimo, max_espaciado, n):
    lista = ordenada_aleatoria_sin_repeticion(minimo, max_espaciado, n)
    return ob.mezclar_aleatorio(lista)


def ordenada_aleatoria_sin_repeticion(minimo, max_espaciado, n):
    lista = [minimo]
    for x in range(n - 1):
        lista.append(math.floor(lista[x] + max_espaciado * random.random()) + 1)
    return lista


def ordenada_aleatoria_con_repeticion(minimo, max_espaciado, n):
    lista = [minimo]
    for x in range(n - 1):
        lista.append(math.floor(lista[x] + (max_espaciado + 1) * random.random()))
    return lista
