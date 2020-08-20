import pickle
import glob
import os
import bin.cargar as cargar

fichero_ajustes = os.path.join("data", "ajustes.pickle")


def ajustes(a):
    serializa(a, fichero_ajustes)


def testdata(td):
    if td.algoritmo.tipo:
        [tipos, nombres] = cargar.ordenacion()
    else:
        [tipos, nombres] = cargar.busqueda()
    tipo = tipos[td.algoritmo.tipo]
    nombre = nombres[td.algoritmo.nombre]
    dir_testdata = os.path.join("data", "testdata", "{0}".format(tipo), "{0}".format(nombre))
    if not os.path.isdir(dir_testdata):
        os.makedirs(dir_testdata)
    fichero_testdata = 'testdata_{0}.pickle'.format(len(glob.glob(os.path.join(dir_testdata, "testdata*"))))
    serializa(td, os.path.join(dir_testdata, fichero_testdata))


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
