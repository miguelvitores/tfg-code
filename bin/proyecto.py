import bin.cargar as c
import time
import os

alg_perm_pd = c.alg_perm_pd()
carpeta_proyectos = os.path.join(os.getcwd(), "data", "proyectos")


class Proyecto:
    def __init__(self, nombre, alg_perm=alg_perm_pd):
        self.nombre = nombre
        self.ruta = os.path.join(os.getcwd(), "data", "proyectos", self.nombre)
        self.algoritmos_permitidos = alg_perm
        self.espacios_trabajo = {}
        self.ult_modif = time.asctime(time.localtime(time.time()))

    def add_espacio_trabajo(self, nombre_et):
        self.espacios_trabajo[nombre_et] = {}

    def eliminar_espacio_trabajo(self, nombre_et):
        self.espacios_trabajo.pop(nombre_et, None)

    def editar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        self.ruta = os.path.join(carpeta_proyectos, self.nombre)
        self.ult_modif = time.asctime(time.localtime(time.time()))

    def editar_alg_perm(self, alg_perm):
        self.algoritmos_permitidos = alg_perm
        self.ult_modif = time.asctime(time.localtime(time.time()))
