import pickle
import glob
import os
import shutil

fichero_ajustes = os.path.join("data", "ajustes.pickle")
carpeta_pr = os.path.join("data", "proyectos")
carpeta_pr_comp = os.path.join("data", "pr_comp")
obj_pr = os.path.join("obj_proyecto.pickle")


def ajustes(a):
    serializa(a, fichero_ajustes)


def serializa(objeto, nombre_fichero):
    with open(nombre_fichero, 'wb') as f:
        pickle.dump(objeto, f)


def eliminar_recursivamente(ruta):
    for f in os.walk(ruta, topdown=False):
        for d in f[1]:
            os.rmdir(os.path.join(f[0], d))
        for file in f[2]:
            os.remove(os.path.join(f[0], file))
    os.rmdir(ruta)


def comprimir_proyecto(proyecto):
    ruta = proyecto.ruta
    serializa(proyecto, os.path.join(ruta, obj_pr))
    shutil.make_archive(os.path.join(carpeta_pr_comp, proyecto.nombre), 'zip', ruta)
    os.remove(os.path.join(ruta, obj_pr))


def descomprimir_proyecto(pr, ruta_desc):
    shutil.unpack_archive(ruta_desc, pr.ruta, 'zip')
    os.remove(os.path.join(carpeta_pr, pr.nombre, obj_pr))
