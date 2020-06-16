import pickle
import os

tiposf = os.path.join("data", "tipos.pickle")
busquedaf = os.path.join("data", "busqueda.pickle")
ordenacionf = os.path.join("data", "ordenacion.pickle")


def carga(nombre_fichero):
    with open(nombre_fichero, 'rb') as f:
        return pickle.load(f)


def busqueda():
    return [carga(tiposf)[0], carga(busquedaf)]


def ordenacion():
    return [carga(tiposf)[1], carga(ordenacionf)]


def alg_perm_pd():
    return {
        carga(tiposf)[0]: carga(busquedaf),
        carga(tiposf)[1]: carga(ordenacionf)
    }
