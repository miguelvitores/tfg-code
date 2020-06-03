
class Analysis:
    def __init__(self):
        self.tiempo_ejecucion = 0
        self.espacio_utilizado = 0
        self.comparaciones = 0
        self.intercambios = 0

    def sum_te(self, cant: int):
        self.tiempo_ejecucion += cant

    def sum_eu(self, cant: int):
        self.espacio_utilizado += cant

    def sum_co(self, cant: int):
        self.comparaciones += cant
        self.tiempo_ejecucion += cant

    def sum_in(self, cant: int):
        self.intercambios += cant
        self.tiempo_ejecucion += cant

    def sum_declaracion(self, cant: int):
        self.espacio_utilizado += cant
        self.tiempo_ejecucion += cant

    def sum_intercambio_misma_lista(self, cant: int):
        self.tiempo_ejecucion += 2 * cant
        self.sum_in(cant)

    def inicializado(self):
        return not (self.tiempo_ejecucion or self.espacio_utilizado or self.comparaciones or self.intercambios)

    def inicializado_sin_intercambios(self):
        return self.tiempo_ejecucion > 0 and self.espacio_utilizado > 0 and self.comparaciones > 0 \
               and self.intercambios == 0

    def inicializado_sin_comparaciones(self):
        return self.tiempo_ejecucion > 0 and self.espacio_utilizado > 0 and self.comparaciones == 0 \
               and self.intercambios > 0
