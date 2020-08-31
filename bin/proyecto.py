import bin.cargar as c
from bin.serializar import eliminar_recursivamente, serializa
import time
import os
import pygal

alg_perm_pd = c.alg_perm_pd()
carpeta_proyectos = os.path.join(os.getcwd(), "data", "proyectos")


class Proyecto:
    def __init__(self, nombre, alg_perm=alg_perm_pd):
        self.nombre = nombre
        self.ruta = os.path.join(os.getcwd(), "data", "proyectos", self.nombre)
        self.algoritmos_permitidos = alg_perm
        self.espacios_trabajo = {}
        self.graficas_abiertas = []
        self.recargar_imagenes = False
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
        self.espacios_trabajo[nombre_et][nombre_p] = {}
        os.mkdir(os.path.join(self.ruta, nombre_et, nombre_p))
        self.ult_modif = time.asctime(time.localtime(time.time()))

    def eliminar_paquete(self, nombre_et, nombre_p):
        self.espacios_trabajo[nombre_et].pop(nombre_p, None)
        eliminar_recursivamente(os.path.join(self.ruta, nombre_et, nombre_p))
        self.ult_modif = time.asctime(time.localtime(time.time()))

    def crear_experimento(self, nombre_et, nombre_p, nombre_exp, testdata):
        ruta_exp = os.path.join(self.ruta, nombre_et, nombre_p, nombre_exp)
        self.espacios_trabajo[nombre_et][nombre_p][nombre_exp] = testdata
        serializa(testdata, "{0}.pickle".format(ruta_exp))
        self.graficas_abiertas.append(ruta_exp)
        graf = pygal.Bar()
        if testdata.algoritmo.tipo == 0:
            tipo_alg = "búsqueda"
        else:
            tipo_alg = "ordenación"
        nombre_alg = alg_perm_pd[tipo_alg][testdata.algoritmo.nombre]
        graf.title = "{0} - {1} {2}".format(nombre_exp, tipo_alg.capitalize(), nombre_alg.capitalize())
        graf.x_labels = testdata.resultados.keys()
        graf.x_title = "Tamaño listas"
        graf.add("tiempo_ejecución", [a.tiempo_ejecucion for a in testdata.resultados.values()])
        graf.add("espacio_utilizado", [a.espacio_utilizado for a in testdata.resultados.values()])
        graf.add("comparaciones", [a.comparaciones for a in testdata.resultados.values()])
        graf.add("intercambios", [a.intercambios for a in testdata.resultados.values()])
        graf.render_to_png("{0}.png".format(ruta_exp))
        serializa(graf, "{0}_graf.pickle".format(ruta_exp))
        self.ult_modif = time.asctime(time.localtime(time.time()))

    def eliminar_experimento(self, nombre_et, nombre_p, nombre_exp):
        ruta_exp = os.path.join(self.ruta, nombre_et, nombre_p, nombre_exp)
        self.espacios_trabajo[nombre_et][nombre_p].pop(nombre_exp, None)
        if os.path.isfile("{0}.pickle".format(ruta_exp)):
            os.remove("{0}.pickle".format(ruta_exp))
        if os.path.isfile("{0}_graf.pickle".format(ruta_exp)):
            os.remove("{0}_graf.pickle".format(ruta_exp))
        if os.path.isfile("{0}.png".format(ruta_exp)):
            os.remove("{0}.png".format(ruta_exp))
        if ruta_exp in self.graficas_abiertas:
            self.graficas_abiertas.remove(ruta_exp)
        self.ult_modif = time.asctime(time.localtime(time.time()))

    def cambiar_tipo_grafica(self, nombre_et, nombre_p, nombre_exp, nombre_tipog, estilog, interpg):
        ruta_exp = os.path.join(self.ruta, nombre_et, nombre_p, nombre_exp)
        graf_anterior = c.carga("{0}_graf.pickle".format(ruta_exp))

        estilo = self.establecer_estilo(estilog)
        if nombre_tipog == "línea básica":
            graf = pygal.Line(fill=False, style=estilo)
        elif nombre_tipog == "línea apilada":
            graf = pygal.StackedLine(fill=True, style=estilo)
        elif nombre_tipog == "barra apilada":
            graf = pygal.StackedBar(fill=False, style=estilo)
        elif nombre_tipog == "barra horizontal":
            graf = pygal.HorizontalBar(fill=False, style=estilo)
        else:
            graf = pygal.Bar(fill=False, style=estilo)

        if nombre_tipog.find("barra") == -1:
            self.establecer_interpolacion(graf, interpg)

        graf.title = graf_anterior.title
        graf.x_labels = graf_anterior.x_labels
        graf.x_title = "Tamaño listas"
        graf.raw_series = graf_anterior.raw_series
        graf.render_to_png("{0}.png".format(ruta_exp))
        serializa(graf, "{0}_graf.pickle".format(ruta_exp))
        if ruta_exp in self.graficas_abiertas:
            self.graficas_abiertas.remove(ruta_exp)
        self.graficas_abiertas.append(ruta_exp)
        self.recargar_imagenes = True
        self.ult_modif = time.asctime(time.localtime(time.time()))

    @staticmethod
    def establecer_interpolacion(graf, interpg):
        if interpg == "ninguna":
            graf.interpolate = None
        elif interpg == "cúbica":
            graf.interpolate = "cubic"
        elif interpg == "cuadrática":
            graf.interpolate = "quadratic"
        elif interpg == "lagrange":
            graf.interpolate = "lagrange"
        elif interpg == "trigonométrica":
            graf.interpolate = "trigonometric"
        elif interpg == "polinómica de hermite":
            graf.interpolate = "hermite"
        else:
            graf.interpolate = None

    @staticmethod
    def establecer_estilo(estilog):
        if estilog == "por defecto":
            return pygal.style.DefaultStyle
        elif estilog == "oscuro":
            return pygal.style.DarkStyle
        elif estilog == "neón":
            return pygal.style.NeonStyle
        elif estilog == "solarizado oscuro":
            return pygal.style.DarkSolarizedStyle
        elif estilog == "solarizado claro":
            return pygal.style.LightSolarizedStyle
        elif estilog == "claro":
            return pygal.style.LightStyle
        elif estilog == "limpio":
            return pygal.style.CleanStyle
        elif estilog == "rojo-azul":
            return pygal.style.RedBlueStyle
        elif estilog == "oscuro teñido":
            return pygal.style.DarkColorizedStyle
        elif estilog == "claro teñido":
            return pygal.style.LightColorizedStyle
        elif estilog == "turquesa":
            return pygal.style.TurquoiseStyle
        elif estilog == "verde claro":
            return pygal.style.LightGreenStyle
        elif estilog == "verde oscuro":
            return pygal.style.DarkGreenStyle
        elif estilog == "oscuro verde-azul":
            return pygal.style.DarkGreenBlueStyle
        elif estilog == "azul":
            return pygal.style.BlueStyle
        else:
            return pygal.style.DefaultStyle
