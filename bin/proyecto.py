import bin.cargar as c
import time

alg_perm_pd = c.alg_perm_pd()


class Proyecto:
    def __init__(self, nombre, alg_perm=alg_perm_pd):
        self.nombre = nombre
        self.algoritmos_permitidos = alg_perm
        self.ult_modif = time.asctime(time.localtime(time.time()))
