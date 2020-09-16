from bin.serializar import eliminar_recursivamente
import pickle
import os
import shutil

tiposf = os.path.join("data", "tipos.pickle")
busquedaf = os.path.join("data", "busqueda.pickle")
ordenacionf = os.path.join("data", "ordenacion.pickle")
ajustesf = os.path.join("data", "ajustes.pickle")
obj_pr = os.path.join("obj_proyecto.pickle")
temp_dir = os.path.join("data", "tmp")
proyectos_dir = os.path.join("data", "proyectos")


def carga(nombre_fichero):
    with open(nombre_fichero, 'rb') as f:
        return pickle.load(f)


def carga_ajustes():
    return carga(ajustesf)


def busqueda():
    return [carga(tiposf)[0], carga(busquedaf)]


def ordenacion():
    return [carga(tiposf)[1], carga(ordenacionf)]


def alg_perm_pd():
    return {
        carga(tiposf)[0]: carga(busquedaf),
        carga(tiposf)[1]: carga(ordenacionf)
    }


def obtener_obj_proyecto(ruta):
    nombrepr = os.path.basename(ruta).split('.')[0]
    shutil.unpack_archive(ruta, os.path.join(temp_dir, nombrepr), 'zip')
    proyecto = carga(os.path.join(temp_dir, nombrepr, obj_pr))
    eliminar_recursivamente(temp_dir)
    return proyecto


def obtener_testdata(proyecto, espacio_trabajo, paquete, experimento):
    fichero = os.path.join(proyectos_dir, proyecto, espacio_trabajo, paquete, "{0}.pickle".format(experimento))
    return carga(fichero)
