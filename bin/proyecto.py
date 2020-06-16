import bin.cargar as c

alg_perm_pd = c.alg_perm_pd()


class Proyecto:
    def __init__(self, nombre, alg_perm: dict):
        self.nombre = nombre
        self.algoritmos_permitidos = alg_perm
        self.ult_modif = -1
