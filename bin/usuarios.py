import abc
import time


class Usuario(metaclass=abc.ABCMeta):
    def __init__(self):
        self.id = hash(self)
        self.ult_log = time.asctime(time.localtime(time.time()))
        self.ult_modif = -1


class Alumno(Usuario):
    def __init__(self):
        super().__init__()
        self.tipo = "alumno"


class Profesor(Usuario):
    def __init__(self):
        super().__init__()
        self.tipo = "profesor"
