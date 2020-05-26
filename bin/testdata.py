

class TestData:
    def __init__(self, algoritmo, data_input, analysis=None, restricciones=None):
        self.algoritmo = algoritmo
        self.analysis = analysis
        self.data_input = data_input
        self.restricciones = restricciones

    def ejecutar(self, valor_busqueda=None):
        """Ejecutaremos dicho algoritmo con las restricciones indicadas"""
        self.algoritmo.ejecutar(self.data_input, valor_busqueda)

    def analizar(self, valor_busqueda=None):
        """Analizaremos dicho algoritmo con las restricciones indicadas"""
        self.algoritmo.analizar(self.data_input, self.analysis, valor_busqueda)
