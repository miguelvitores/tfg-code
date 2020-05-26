import pickle
import os

tiposf = os.path.join("data", "tipos.pickle")
busquedaf = os.path.join("data", "busqueda.pickle")
ordenacionf = os.path.join("data", "ord.pickle")


def carga(nombre_fichero):
    with open(nombre_fichero, 'rb') as f:
        return pickle.load(f)


def busqueda():
    return [carga(tiposf), carga(busquedaf)]


def ordenacion():
    return [carga(tiposf), carga(ordenacionf)]
