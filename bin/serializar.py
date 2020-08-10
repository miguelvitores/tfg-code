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
