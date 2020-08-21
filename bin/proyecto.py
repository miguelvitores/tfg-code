import bin.cargar as c
from bin.serializar import eliminar_recursivamente
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

    def editar_proyecto(self, nombre, alg_perm):
        self._editar_nombre(nombre)
        self._editar_alg_perm(alg_perm)
        self.ult_modif = time.asctime(time.localtime(time.time()))

    def _editar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        ruta_anterior = self.ruta
        self.ruta = os.path.join(carpeta_proyectos, self.nombre)
        os.rename(ruta_anterior, self.ruta)

    def _editar_alg_perm(self, alg_perm):
        self.algoritmos_permitidos = alg_perm

    def crear_espacio_trabajo(self, nombre):
        self.espacios_trabajo[nombre] = {}
        os.mkdir(os.path.join(self.ruta, nombre))
        self.ult_modif = time.asctime(time.localtime(time.time()))

    def eliminar_espacio_trabajo(self, nombre):
        self.espacios_trabajo.pop(nombre, None)
        eliminar_recursivamente(os.path.join(self.ruta, nombre))
        self.ult_modif = time.asctime(time.localtime(time.time()))

    def crear_paquete(self, nombre_et, nombre_p):
        self.espacios_trabajo[nombre_et][nombre_p] = []
        os.mkdir(os.path.join(self.ruta, nombre_et, nombre_p))
        self.ult_modif = time.asctime(time.localtime(time.time()))

    def eliminar_paquete(self, nombre_et, nombre_p):
        self.espacios_trabajo[nombre_et].pop(nombre_p, None)
        eliminar_recursivamente(os.path.join(self.ruta, nombre_et, nombre_p))
        self.ult_modif = time.asctime(time.localtime(time.time()))

    def crear_experimento(self, nombre_et, nombre_p, nombre_exp):
        pass

    def eliminar_experimento(self, nombre_et, nombre_p, nombre_exp):
        self.espacios_trabajo[nombre_et][nombre_p].pop(nombre_exp, None)
        os.remove(os.path.join(self.ruta, nombre_et, nombre_p, nombre_exp))
        self.ult_modif = time.asctime(time.localtime(time.time()))
