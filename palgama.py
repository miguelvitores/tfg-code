from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, ScreenManagerException
from kivy.config import Config
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.tabbedpanel import TabbedPanelItem
from pygal.view import Box

from bin.serializar import ajustes, eliminar_recursivamente
from bin.usuarios import Alumno, Profesor
from bin.proyecto import Proyecto
from bin.testdata.rango import RangoTam, RangoVal
from bin.testdata.td_tipos import TestDataOrdenacionLOEquidistante, TestDataOrdenacionLOACR, TestDataOrdenacionLOASR, \
    TestDataOrdenacionLAleatoria, TestDataOrdenacionLAleatoriaSR, TestDataBusquedaLOEquidistante, \
    TestDataBusquedaLAleatoria, TestDataBusquedaLOACR, TestDataBusquedaLOASR
from bin.algoritmos.ord.ordenacionseleccion import OrdenacionSeleccion
from bin.algoritmos.ord.ordenacioninsercion import OrdenacionInsercion
from bin.algoritmos.ord.ordenacionburbuja import OrdenacionBurbuja
from bin.algoritmos.ord.ordenacionquicksort import OrdenacionQuicksort
from bin.algoritmos.ord.ordenacionshellsort import OrdenacionShellsort
from bin.algoritmos.ord.ordenacionmergesort import OrdenacionMergesort
from bin.algoritmos.ord.ordenacionradixsort import OrdenacionRadixsort
from bin.algoritmos.busq.busquedalineal import BusquedaLineal
from bin.algoritmos.busq.busquedabinaria import BusquedaBinaria
from bin.algoritmos.busq.busquedasalto import BusquedaSalto
from bin.algoritmos.busq.busquedainterpolacion import BusquedaInterpolacion
from bin.algoritmos.busq.busquedaexponencial import BusquedaExponencial
from bin.algoritmos.busq.busquedafibonacci import BusquedaFibonacci

import bin.cargar as cargar
import bin.testdata.td_tipos as tdt
import os
import pygal

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'resizable', 0)
aj = cargar.carga_ajustes()
proyectos = aj['ult_proyectos']
sm = ScreenManager(transition=FadeTransition())


class SpinnerOpciones(SpinnerOption):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_down = ''
        self.background_color = (0.7725, 0.9882, 0.9412, 1)
        self.text_size = (200, None)
        self.halign = 'center'
        self.bind(on_press=self.presionar_boton, on_release=self.soltar_boton)

    def presionar_boton(self, btn):
        btn.background_color = (0.6157, 0.7882, 0.749, 1)
        btn.color = (1, 1, 1, 1)

    def soltar_boton(self, btn):
        btn.background_color = (0.7725, 0.9882, 0.9412, 1)
        btn.color = (0, 0, 0, 1)


class SpinnerDropdown(DropDown):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_name = "fonts/FiraSans-Medium"


class SpinnerWidget(Spinner):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.option_cls = SpinnerOpciones
        self.dropdown_cls = SpinnerDropdown
        self.background_down = ''
        self.background_normal = ''
        self.bind(on_press=self.presionar_boton, on_release=self.soltar_boton)

    def presionar_boton(self, btn):
        btn.background_color = (1, 1, 1, 1)
        btn.color = (0, 0, 0, 1)

    def soltar_boton(self, btn):
        btn.background_color = (0, 0, 0, 1)
        btn.color = (1, 1, 1, 1)


class DropdownComportamiento(DropDown):
    def presionar_boton(self, btn):
        btn.background_color = (0.2706, 0.4118, 0.3804, 1)
        btn.color = (1, 1, 1, 1)

    def soltar_boton(self, btn):
        btn.background_color = (0.4, 0.6078, 0.5647, 1)
        btn.color = (0, 0, 0, 1)
        self.select(btn.text)


class AbrirPrHijosComportamiento:

    def __init__(self, proyecto: Proyecto):
        self.proyecto = proyecto

    def volver_abrirpr(self, inst):
        Window.maximize()
        sm.switch_to(sm.get_screen("abrirpr_{0}".format(self.proyecto.nombre)))

    def recargar_proyecto(self):
        # Hacemos un refresh de la ventana del proyecto actual
        abrirpr = "abrirpr_{0}".format(self.proyecto.nombre)
        sm.remove_widget(sm.get_screen(name=abrirpr))
        sm.add_widget(AbrirProyectoScreen(self.proyecto, name=abrirpr))
        Window.maximize()
        sm.switch_to(sm.get_screen(abrirpr))

        # Eliminamos todas las pantallas sensibles a cambios del proyecto si existen
        try:
            screen = sm.get_screen("add_espt_{0}".format(self.proyecto.nombre))
            sm.remove_widget(screen)
        except ScreenManagerException:
            pass
        try:
            screen = sm.get_screen("add_paq_{0}".format(self.proyecto.nombre))
            sm.remove_widget(screen)
        except ScreenManagerException:
            pass
        try:
            screen = sm.get_screen("add_exp_{0}".format(self.proyecto.nombre))
            sm.remove_widget(screen)
        except ScreenManagerException:
            pass
        try:
            screen = sm.get_screen("el_espt_{0}".format(self.proyecto.nombre))
            sm.remove_widget(screen)
        except ScreenManagerException:
            pass
        try:
            screen = sm.get_screen("el_paq_{0}".format(self.proyecto.nombre))
            sm.remove_widget(screen)
        except ScreenManagerException:
            pass
        try:
            screen = sm.get_screen("el_exp_{0}".format(self.proyecto.nombre))
            sm.remove_widget(screen)
        except ScreenManagerException:
            pass
        try:
            screen = sm.get_screen("cambiog_{0}".format(self.proyecto.nombre))
            sm.remove_widget(screen)
        except ScreenManagerException:
            pass


class DropdownAbrirProyecto(DropdownComportamiento):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for p in proyectos:
            btn = Button(text=p.nombre, size_hint_y=None, height=50, background_normal='', background_down='',
                         background_color=(0.4, 0.6078, 0.5647, 1))
            btn.bind(on_press=self.presionar_boton, on_release=self.soltar_boton)
            self.add_widget(btn)
        btn = Button(text="Importar Proyecto", size_hint_y=None, height=50, background_normal='', background_down='',
                     background_color=(0.4, 0.6078, 0.5647, 1))
        btn.bind(on_press=self.presionar_boton, on_release=self.soltar_boton)
        self.add_widget(btn)


class DropdownProyectos(DropdownComportamiento):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for p in proyectos:
            btn = Button(text=p.nombre, size_hint_y=None, height=50, background_normal='', background_down='',
                         background_color=(0.4, 0.6078, 0.5647, 1))
            btn.bind(on_press=self.presionar_boton, on_release=self.soltar_boton)
            self.add_widget(btn)


class DropdownExperimentos(DropDown):
    def __init__(self, proyecto, **kwargs):
        super().__init__(**kwargs)
        self.proyecto = proyecto
        btn = Button(text="Añadir", size_hint_y=None, height=50, background_normal='',
                     background_down='', background_color=(0.4, 0.6078, 0.5647, 1))
        btn.bind(on_press=self.presionar_boton, on_release=self.soltar_boton)
        btn.bind(on_release=self.soltar_dpdad)
        self.add_widget(btn)
        btn = Button(text="Eliminar", size_hint_y=None, height=50, background_normal='',
                     background_down='', background_color=(0.4, 0.6078, 0.5647, 1))
        btn.bind(on_press=self.presionar_boton, on_release=self.soltar_boton)
        btn.bind(on_release=self.soltar_dpdel)
        self.add_widget(btn)

        self.dpdad = DropdownExperimentosOpciones(self.proyecto)
        self.dpdel = DropdownExperimentosOpciones(self.proyecto)
        self.dpdad.bind(on_select=self.llamada_dpdad)
        self.dpdel.bind(on_select=self.llamada_dpdel)
        self.dismiss_on_select = False

    @staticmethod
    def presionar_boton(btn):
        btn.background_color = (0.2706, 0.4118, 0.3804, 1)
        btn.color = (1, 1, 1, 1)

    @staticmethod
    def soltar_boton(btn):
        btn.background_color = (0.4, 0.6078, 0.5647, 1)
        btn.color = (0, 0, 0, 1)

    def llamada_dpdad(self, inst, nombre: str):
        self.dismiss()
        if nombre == "Espacio de trabajo":
            self.dpdad.add_espt()
        elif nombre == "Paquete":
            self.dpdad.add_paq()
        elif nombre == "Experimento":
            self.dpdad.add_exp()

    def llamada_dpdel(self, inst, nombre: str):
        self.dismiss()
        if nombre == "Espacio de trabajo":
            self.dpdel.el_espt()
        elif nombre == "Paquete":
            self.dpdel.el_paq()
        elif nombre == "Experimento":
            self.dpdel.el_exp()

    def soltar_dpdad(self, instancia):
        self.dpdad.open(instancia)

    def soltar_dpdel(self, instancia):
        self.dpdel.open(instancia)


class DropdownExperimentosOpciones(DropDown):
    def __init__(self, proyecto, **kwargs):
        super().__init__(**kwargs)
        self.proyecto = proyecto
        self.espt = Button(text="Espacio de trabajo", size_hint_y=None, height=50, background_normal='',
                           background_down='', background_color=(0.7725, 0.9882, 0.9412, 1))
        self.espt.bind(on_press=self.presionar_boton, on_release=self.soltar_espt)
        self.add_widget(self.espt)
        self.paq = Button(text="Paquete", size_hint_y=None, height=50, background_normal='',
                          background_down='',
                          background_color=(0.7725, 0.9882, 0.9412, 1))
        self.paq.bind(on_press=self.presionar_boton, on_release=self.soltar_paq)
        self.add_widget(self.paq)
        self.exp = Button(text="Experimento", size_hint_y=None, height=50, background_normal='',
                          background_down='',
                          background_color=(0.7725, 0.9882, 0.9412, 1))
        self.exp.bind(on_press=self.presionar_boton, on_release=self.soltar_exp)
        self.add_widget(self.exp)

    @staticmethod
    def presionar_boton(btn):
        btn.background_color = (0.6157, 0.7882, 0.749, 1)

    def soltar_espt(self, btn):
        self.espt.background_color = (0.7725, 0.9882, 0.9412, 1)
        self.select(self.espt.text)

    def soltar_paq(self, btn):
        self.paq.background_color = (0.7725, 0.9882, 0.9412, 1)
        self.select(self.paq.text)

    def soltar_exp(self, btn):
        self.exp.background_color = (0.7725, 0.9882, 0.9412, 1)
        self.select(self.exp.text)

    def add_espt(self):
        try:
            screen = sm.get_screen("add_espt_{0}".format(self.proyecto.nombre))
        except ScreenManagerException:
            screen = CrearEspacioTrabajoScreen(self.proyecto, name="add_espt_{0}".format(self.proyecto.nombre))
            sm.add_widget(screen)
        Window.restore()
        sm.switch_to(screen)

    def add_paq(self):
        try:
            screen = sm.get_screen("add_paq_{0}".format(self.proyecto.nombre))
        except ScreenManagerException:
            screen = CrearPaqueteScreen(self.proyecto, name="add_paq_{0}".format(self.proyecto.nombre))
            sm.add_widget(screen)
        Window.restore()
        sm.switch_to(screen)

    def add_exp(self):
        try:
            screen = sm.get_screen("add_exp_{0}".format(self.proyecto.nombre))
        except ScreenManagerException:
            screen = CrearExperimentoScreen(self.proyecto, name="add_exp_{0}".format(self.proyecto.nombre))
            sm.add_widget(screen)
        sm.switch_to(screen)

    def el_espt(self):
        try:
            screen = sm.get_screen("el_espt_{0}".format(self.proyecto.nombre))
        except ScreenManagerException:
            screen = EliminarEspacioTrabajoScreen(self.proyecto, name="el_espt_{0}".format(self.proyecto.nombre))
            sm.add_widget(screen)
        Window.restore()
        sm.switch_to(screen)

    def el_paq(self):
        try:
            screen = sm.get_screen("el_paq_{0}".format(self.proyecto.nombre))
        except ScreenManagerException:
            screen = EliminarPaqueteScreen(self.proyecto, name="el_paq_{0}".format(self.proyecto.nombre))
            sm.add_widget(screen)
        Window.restore()
        sm.switch_to(screen)

    def el_exp(self):
        try:
            screen = sm.get_screen("el_exp_{0}".format(self.proyecto.nombre))
        except ScreenManagerException:
            screen = EliminarExperimentoScreen(self.proyecto, name="el_exp_{0}".format(self.proyecto.nombre))
            sm.add_widget(screen)
        Window.restore()
        sm.switch_to(screen)


class DropdownGraficasAvanzadas(DropdownComportamiento):
    def __init__(self, proyecto, **kwargs):
        super().__init__(**kwargs)
        self.proyecto = proyecto
        btn = Button(text="Cambiar tipo gr\u00e1fica", size_hint_y=None, height=50, background_normal='',
                     background_down='', background_color=(0.4, 0.6078, 0.5647, 1))
        btn.bind(on_press=self.presionar_boton, on_release=self.soltar_boton)
        btn.bind(on_release=self.soltar_cambiog)
        self.add_widget(btn)

    def soltar_cambiog(self, btn):
        try:
            screen = sm.get_screen("cambiog_{0}".format(self.proyecto.nombre))
        except ScreenManagerException:
            screen = CambiarGraficaScreen(self.proyecto, name="cambiog_{0}".format(self.proyecto.nombre))
            sm.add_widget(screen)
        sm.switch_to(screen)


class DropdownTeoriaAlgortimos(DropdownComportamiento):
    def __init__(self, pr: Proyecto, **kwargs):
        super().__init__(**kwargs)
        self.algoritmos = pr.algoritmos_permitidos
        self.auto_width = False
        self.width = 300
        for tipo in self.algoritmos:
            for nombre in self.algoritmos[tipo]:
                btn = Button(text="Teor\u00eda de {0} {1}".format(tipo, nombre), size_hint_y=None, height=50,
                             background_normal='', background_down='', background_color=(0.4, 0.6078, 0.5647, 1))
                btn.bind(on_press=self.presionar_boton, on_release=self.soltar_boton)
                self.add_widget(btn)


# Layouts


class PrincipalLayout(GridLayout):
    botones = ObjectProperty()
    cp = ObjectProperty()
    ep = ObjectProperty()
    elp = ObjectProperty()
    uspinner = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        usuario = aj['ult_usuario']
        if isinstance(usuario, Profesor):
            self.botones.remove_widget(self.cp)
            self.botones.remove_widget(self.ep)
            self.botones.remove_widget(self.elp)
        self.uspinner.text = usuario.tipo.capitalize()
        self.dpdep = DropdownProyectos()
        self.dpdelp = DropdownProyectos()
        self.dpdcp = DropdownProyectos()
        self.dpdab = DropdownAbrirProyecto()
        self.dpdab.bind(on_select=self.llamada_dpdab)
        self.dpdcp.bind(on_select=self.llamada_dpdcp)
        self.dpdep.bind(on_select=self.llamada_dpdep)
        self.dpdelp.bind(on_select=self.llamada_dpdelp)
        self.proyecto_a_eliminar = None

    @staticmethod
    def llamada_dpdab(instancia, nombre):
        pr = [p for p in proyectos if p.nombre is nombre][0]
        try:
            screen = sm.get_screen("abrirpr_{0}".format(nombre))
        except ScreenManagerException:
            screen = AbrirProyectoScreen(pr, name="abrirpr_{0}".format(nombre))
            sm.add_widget(screen)

        proyectos.remove(pr)
        proyectos.insert(0, pr)
        Window.maximize()
        sm.switch_to(screen)

    @staticmethod
    def llamada_dpdcp(instancia, nombre):
        print(instancia, nombre)

    @staticmethod
    def llamada_dpdep(instancia, nombre):
        pr = [p for p in proyectos if p.nombre is nombre][0]
        try:
            screen = sm.get_screen("editarpr_{0}".format(nombre))
        except ScreenManagerException:
            screen = EditarProyectoScreen(pr, name="editarpr_{0}".format(nombre))
            sm.add_widget(screen)

        sm.switch_to(screen)

    def llamada_dpdelp(self, instancia, nombre):
        self.proyecto_a_eliminar = [p for p in proyectos if p.nombre is nombre][0]
        box = BoxLayout(orientation='horizontal', cols=2)
        boton_si = Button(text='Eliminar', font_name="fonts/FiraSans-SemiBold",
                          color=(0, 0, 0, 1), background_color=(0.5451, 0.9529, 0.4235, 1))
        boton_no = Button(text='Cancelar', font_name="fonts/FiraSans-SemiBold",
                          color=(0, 0, 0, 1), background_color=(0.9059, 0.3451, 0.3529, 1))
        box.add_widget(boton_si)
        box.add_widget(boton_no)
        popup = Popup(title='Desea eliminar el proyecto: {}?'.format(nombre), separator_color=(0.4, 0.6078, 0.5647, 1),
                      title_color=(0.4, 0.6078, 0.5647, 1), title_font="fonts/FiraSans-ThinItalic",
                      content=box, size_hint=(None, None), size=(300, 125))
        popup.open()
        boton_si.bind(on_press=self.presionar_eliminar_proyecto)
        boton_no.bind(on_press=self.presionar_cancelar_eliminar_proyecto)
        boton_si.bind(on_release=self.soltar_eliminar_proyecto)
        boton_no.bind(on_release=self.soltar_cancelar_eliminar_proyecto)
        boton_si.bind(on_release=popup.dismiss)
        boton_no.bind(on_release=popup.dismiss)

    @staticmethod
    def presionar_eliminar_proyecto(btn):
        btn.background_color = (0.2667, 0.9059, 0.0745, 1)

    def soltar_eliminar_proyecto(self, btn):
        btn.background_color = (0.5451, 0.9529, 0.4235, 1)
        proyectos.remove(self.proyecto_a_eliminar)
        eliminar_recursivamente(self.proyecto_a_eliminar.ruta)
        sm.switch_to(sm.get_screen("principal_help"))
        sm.remove_widget(sm.get_screen("principal"))
        sm.add_widget(PrincipalScreen(name="principal"))
        sm.switch_to(sm.get_screen("principal"))

    @staticmethod
    def presionar_cancelar_eliminar_proyecto(btn):
        btn.background_color = (0.8824, 0.1451, 0.0784, 1)
        btn.color = (1, 1, 1, 1)

    @staticmethod
    def soltar_cancelar_eliminar_proyecto(btn):
        btn.background_color = (0.949, 0.4667, 0.4196, 1)
        btn.color = (0, 0, 0, 1)

    def soltar_dpdab(self, instancia):
        self.dpdab.open(instancia)

    def soltar_dpdcp(self, instancia):
        self.dpdcp.open(instancia)

    def soltar_dpdep(self, instancia):
        self.dpdep.open(instancia)

    def soltar_dpdelp(self, instancia):
        self.dpdelp.open(instancia)

    def usuario_cambio(self, usuario):
        if usuario == "Profesor":
            aj['ult_usuario'] = Profesor()
            self.botones.add_widget(self.cp)
            self.botones.add_widget(self.ep)
            self.botones.add_widget(self.elp)
        elif usuario == "Alumno":
            aj['ult_usuario'] = Alumno()
            self.botones.remove_widget(self.cp)
            self.botones.remove_widget(self.ep)
            self.botones.remove_widget(self.elp)

    @staticmethod
    def cambiar_a_crear_proyecto(instancia):
        sm.switch_to(sm.get_screen("crearp"))

    @staticmethod
    def salir(instancia):
        Window.close()


class CrearProyectoLayout(GridLayout):
    rows = 2
    cbbb = ObjectProperty()
    cbbe = ObjectProperty()
    cbbf = ObjectProperty()
    cbbi = ObjectProperty()
    cbbl = ObjectProperty()
    cbbs = ObjectProperty()
    cbob = ObjectProperty()
    cboi = ObjectProperty()
    cbom = ObjectProperty()
    cboq = ObjectProperty()
    cbor = ObjectProperty()
    cbos = ObjectProperty()
    cbosh = ObjectProperty()
    nombrepr = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.algs = {'busq': [], 'ord': []}
        self.algs['busq'].append(self.cbbb)
        self.algs['busq'].append(self.cbbe)
        self.algs['busq'].append(self.cbbf)
        self.algs['busq'].append(self.cbbi)
        self.algs['busq'].append(self.cbbl)
        self.algs['busq'].append(self.cbbs)
        self.algs['ord'].append(self.cbob)
        self.algs['ord'].append(self.cboi)
        self.algs['ord'].append(self.cbom)
        self.algs['ord'].append(self.cboq)
        self.algs['ord'].append(self.cbor)
        self.algs['ord'].append(self.cbos)
        self.algs['ord'].append(self.cbosh)

    def seleccionar_todos_ab(self, inst):
        for cb in self.algs['busq']:
            cb.active = inst.active

    def seleccionar_todos_ao(self, inst):
        for cb in self.algs['ord']:
            cb.active = inst.active

    def volver_a_principal(self, inst):
        sm.switch_to(sm.get_screen("principal"))

    def todos_algs_desactivados(self):
        for a in self.algs:
            for cb in self.algs[a]:
                if cb.active is True:
                    return False
        popup = Popup(title='Error creación proyecto', separator_color=(0.9059, 0.3451, 0.3529, 1),
                      title_color=(0.9059, 0.3451, 0.3529, 1), title_font="fonts/FiraSans-ThinItalic",
                      content=Label(text='Selecci\u00f3n de algoritmos no v\u00e1lida',
                                    font_name="fonts/FiraSans-SemiBold",
                                    color=(1, 1, 1, 1)
                                    ), size_hint=(None, None), size=(250, 100))
        popup.open()
        return True

    def get_algs_elegidos(self):
        algs_elegidos = {'b\u00fasqueda': [], 'ordenaci\u00f3n': []}
        if self.cbbb.active:
            algs_elegidos['b\u00fasqueda'].append('binaria')
        if self.cbbe.active:
            algs_elegidos['b\u00fasqueda'].append('exponencial')
        if self.cbbf.active:
            algs_elegidos['b\u00fasqueda'].append('fibonacci')
        if self.cbbi.active:
            algs_elegidos['b\u00fasqueda'].append('interpolación')
        if self.cbbl.active:
            algs_elegidos['b\u00fasqueda'].append('lineal')
        if self.cbbs.active:
            algs_elegidos['b\u00fasqueda'].append('salto')
        if self.cbob.active:
            algs_elegidos['ordenaci\u00f3n'].append('burbuja')
        if self.cboi.active:
            algs_elegidos['ordenaci\u00f3n'].append('inserción')
        if self.cbom.active:
            algs_elegidos['ordenaci\u00f3n'].append('mergesort')
        if self.cboq.active:
            algs_elegidos['ordenaci\u00f3n'].append('3way quicksort')
        if self.cbor.active:
            algs_elegidos['ordenaci\u00f3n'].append('radixsort')
        if self.cbos.active:
            algs_elegidos['ordenaci\u00f3n'].append('selección')
        if self.cbosh.active:
            algs_elegidos['ordenaci\u00f3n'].append('shellsort 3x+1')
        return algs_elegidos

    @staticmethod
    def es_nombrepr_invalido(pr):
        if len(pr) == 0 or pr.isspace():
            popup = Popup(title='Error creación proyecto', separator_color=(0.9059, 0.3451, 0.3529, 1),
                          title_color=(0.9059, 0.3451, 0.3529, 1), title_font="fonts/FiraSans-ThinItalic",
                          content=Label(text='Nombre del proyecto no v\u00e1lido',
                                        font_name="fonts/FiraSans-SemiBold",
                                        color=(1, 1, 1, 1)
                                        ), size_hint=(None, None), size=(250, 100))
            popup.open()
            return True
        return False

    @staticmethod
    def es_nombrepr_repetido(pr):
        if pr.casefold() in [p.nombre.casefold() for p in proyectos]:
            popup = Popup(title='Error creación proyecto', separator_color=(0.9059, 0.3451, 0.3529, 1),
                          title_color=(0.9059, 0.3451, 0.3529, 1), title_font="fonts/FiraSans-ThinItalic",
                          content=Label(text='Nombre de proyecto ya existente',
                                        font_name="fonts/FiraSans-SemiBold",
                                        color=(1, 1, 1, 1)
                                        ), size_hint=(None, None), size=(250, 100))
            popup.open()
            return True
        return False

    def comprobar_form(self, pr):
        if self.es_nombrepr_invalido(pr) or self.es_nombrepr_repetido(pr) or self.todos_algs_desactivados():
            return False
        return True

    def confirmar(self, inst):
        pr = self.nombrepr.text
        if self.comprobar_form(pr):
            algs_seleccionados = self.get_algs_elegidos()
            p = Proyecto(pr, algs_seleccionados)
            os.mkdir(p.ruta)
            proyectos.insert(0, p)
            popup = Popup(title='Proyecto creado', separator_color=(0.5451, 0.9529, 0.4235, 1),
                          title_color=(0.5451, 0.9529, 0.4235, 1), title_font="fonts/FiraSans-ThinItalic",
                          content=Label(text='Proyecto creado correctamente',
                                        font_name="fonts/FiraSans-SemiBold",
                                        color=(1, 1, 1, 1)
                                        ), size_hint=(None, None), size=(250, 100))
            popup.open()

            # Hacemos un refresh de la ventana principal
            sm.remove_widget(sm.get_screen("principal"))
            sm.add_widget(PrincipalScreen(name="principal"))
            sm.switch_to(sm.get_screen("principal"))

            # Hacemos un refresh de la ventana de crear proyectos
            sm.remove_widget(sm.get_screen("crearp"))
            sm.add_widget(CrearProyectoScreen(name="crearp"))


class EditarProyectoLayout(CrearProyectoLayout):
    def __init__(self, proyecto, **kwargs):
        super().__init__(**kwargs)
        self.proyecto = proyecto
        self.nombrepr.text = self.proyecto.nombre
        algs_elegidos = proyecto.algoritmos_permitidos
        if 'binaria' in algs_elegidos['búsqueda']:
            self.cbbb.active = True
        if 'exponencial' in algs_elegidos['búsqueda']:
            self.cbbe.active = True
        if 'fibonacci' in algs_elegidos['búsqueda']:
            self.cbbf.active = True
        if 'interpolación' in algs_elegidos['búsqueda']:
            self.cbbi.active = True
        if 'lineal' in algs_elegidos['búsqueda']:
            self.cbbl.active = True
        if 'salto' in algs_elegidos['búsqueda']:
            self.cbbs.active = True
        if 'burbuja' in algs_elegidos['ordenación']:
            self.cbob.active = True
        if 'inserción' in algs_elegidos['ordenación']:
            self.cboi.active = True
        if 'mergesort' in algs_elegidos['ordenación']:
            self.cbom.active = True
        if '3way quicksort' in algs_elegidos['ordenación']:
            self.cboq.active = True
        if 'radixsort' in algs_elegidos['ordenación']:
            self.cbor.active = True
        if 'selección' in algs_elegidos['ordenación']:
            self.cbos.active = True
        if 'shellsort 3x+1' in algs_elegidos['ordenación']:
            self.cbosh.active = True

    def volver_a_principal(self, inst):
        sm.switch_to(sm.get_screen("principal"))

    def comprobar_form(self, pr):
        if self.es_nombrepr_invalido(pr) or self.todos_algs_desactivados():
            return False
        return True

    def confirmar(self, inst):
        pr = self.nombrepr.text
        if self.comprobar_form(pr):
            nombre_anterior = self.proyecto.nombre
            algs_seleccionados = self.get_algs_elegidos()
            self.proyecto.editar_proyecto(pr, algs_seleccionados)
            proyectos.remove(self.proyecto)
            proyectos.insert(0, self.proyecto)
            popup = Popup(title='Proyecto editado', separator_color=(0.5451, 0.9529, 0.4235, 1),
                          title_color=(0.5451, 0.9529, 0.4235, 1), title_font="fonts/FiraSans-ThinItalic",
                          content=Label(text='Proyecto editado correctamente',
                                        font_name="fonts/FiraSans-SemiBold",
                                        color=(1, 1, 1, 1)
                                        ), size_hint=(None, None), size=(250, 100))
            popup.open()

            # Hacemos un refresh de la ventana principal
            sm.remove_widget(sm.get_screen("principal"))
            sm.add_widget(PrincipalScreen(name="principal"))
            sm.switch_to(sm.get_screen("principal"))

            # Eliminamos la ventana de editar proyectos
            sm.remove_widget(sm.get_screen("editarpr_{0}".format(nombre_anterior)))


class AbrirProyectoLayout(BoxLayout):
    label_nombrepr = ObjectProperty()
    filechooser = ObjectProperty()
    panel_graficas = ObjectProperty()

    def __init__(self, proyecto, **kwargs):
        super().__init__(**kwargs)
        self.proyecto = proyecto
        self.label_nombrepr.text = self.proyecto.nombre
        self.filechooser.rootpath = proyecto.ruta
        self.dpdex = DropdownExperimentos(self.proyecto)
        self.dpdga = DropdownGraficasAvanzadas(self.proyecto)
        self.dpdta = DropdownTeoriaAlgortimos(self.proyecto)
        for graf in self.proyecto.graficas_abiertas:
            self.add_pest(graf)
        if len(self.proyecto.graficas_abiertas) > 0:
            self.panel_graficas.default_tab = self.panel_graficas.tab_list[0]
            self.proyecto.recargar_imagenes = False

    def soltar_dpdex(self, instancia):
        self.dpdex.open(instancia)

    def soltar_dpdga(self, instancia):
        self.dpdga.open(instancia)

    def soltar_dpdta(self, instancia):
        self.dpdta.open(instancia)

    @staticmethod
    def presionar_csv(btn):
        btn.background_color = (0.2706, 0.4118, 0.3804, 1)
        btn.color = (1, 1, 1, 1)

    @staticmethod
    def soltar_csv(btn):
        btn.background_color = (0.4, 0.6078, 0.5647, 1)
        btn.color = (0, 0, 0, 1)
        graf_pickle = "{0}_graf.pickle".format(btn.parent.id)
        graf = cargar.carga(graf_pickle)
        graf.render_in_browser()

    @staticmethod
    def presionar_cerrarp(btn):
        btn.background_color = (0.8824, 0.1451, 0.0784, 1)
        btn.color = (1, 1, 1, 1)

    def soltar_cerrarp(self, btn):
        btn.background_color = (0.949, 0.4667, 0.4196, 1)
        btn.color = (0, 0, 0, 1)
        pest_actual = self.panel_graficas.current_tab
        self.panel_graficas.remove_widget(pest_actual)
        self.panel_graficas.remove_widget(pest_actual.content)
        self.proyecto.graficas_abiertas.remove(btn.parent.id)
        if len(self.panel_graficas.tab_list) > 0:
            self.panel_graficas.switch_to(self.panel_graficas.tab_list[0])

    def add_pest(self, graf):
        graf_png = "{0}.png".format(graf)
        img = Image(source=graf_png, size_hint_y=0.9, allow_stretch=True)
        if self.proyecto.recargar_imagenes:
            img.reload()
        bxlv = BoxLayout(orientation="vertical")
        bxlh = BoxLayout(orientation="horizontal", size_hint_y=0.1)
        btn = Button(text="Abrir csv en navegador", size_hint_x=0.3, background_normal='', background_down='',
                     background_color=(0.4, 0.6078, 0.5647, 1), font_size=18)
        btn_cerrar = Button(text="Cerrar pestaña", size_hint_x=0.3, background_normal='', background_down='',
                            background_color=(0.949, 0.4667, 0.4196, 1), font_size=18)
        bxlh.add_widget(BoxLayout(size_hint_x=0.15))
        bxlh.add_widget(btn)
        bxlh.add_widget(BoxLayout(size_hint_x=0.1))
        bxlh.add_widget(btn_cerrar)
        bxlh.add_widget(BoxLayout(size_hint_x=0.15))
        bxlh.id = graf
        bxlv.add_widget(img)
        bxlv.add_widget(bxlh)
        tbdp = TabbedPanelItem(text=os.path.basename(graf_png))
        btn.bind(on_press=self.presionar_csv)
        btn.bind(on_release=self.soltar_csv)
        btn_cerrar.bind(on_press=self.presionar_cerrarp)
        btn_cerrar.bind(on_release=self.soltar_cerrarp)
        tbdp.add_widget(bxlv)
        self.panel_graficas.add_widget(tbdp)

    def seleccionar_archivo(self, seleccion):
        if len(seleccion) > 0:
            arch = seleccion[0]
            if os.path.isfile(arch):
                graf = arch.split('.')[0]
                if graf in self.proyecto.graficas_abiertas:
                    for pest in self.panel_graficas.tab_list:
                        if pest.text == os.path.basename("{0}.png".format(graf)):
                            self.panel_graficas.switch_to(pest)
                else:
                    self.proyecto.graficas_abiertas.append(graf)
                    self.add_pest(graf)
                    self.panel_graficas.switch_to(self.panel_graficas.tab_list[0])

    @staticmethod
    def volver_a_principal(inst):
        Window.restore()
        # Hacemos un refresh de la ventana principal
        sm.remove_widget(sm.get_screen("principal"))
        sm.add_widget(PrincipalScreen(name="principal"))
        sm.switch_to(sm.get_screen("principal"))

    def get_nombre_proyecto(self):
        return self.proyecto.nombre


class CrearEspacioTrabajoLayout(GridLayout, AbrirPrHijosComportamiento):
    rows = 2
    nombre_et = ObjectProperty()

    def __init__(self, proyecto, **kwargs):
        super().__init__(proyecto=proyecto, **kwargs)
        self.proyecto = proyecto

    def comprobar_form(self, et):
        if self.es_nombre_invalido(et) or self.es_nombre_repetido(et):
            return False
        return True

    def confirmar(self, inst):
        et = self.nombre_et.text
        if self.comprobar_form(et):
            self.proyecto.crear_espacio_trabajo(et)

            popup = Popup(title='Espacio de trabajo creado', separator_color=(0.5451, 0.9529, 0.4235, 1),
                          title_color=(0.5451, 0.9529, 0.4235, 1), title_font="fonts/FiraSans-ThinItalic",
                          content=Label(text='Espacio de trabajo creado correctamente',
                                        font_name="fonts/FiraSans-SemiBold",
                                        color=(1, 1, 1, 1)
                                        ), size_hint=(None, None), size=(350, 100))
            popup.open()

            self.recargar_proyecto()

    @staticmethod
    def es_nombre_invalido(et):
        if len(et) == 0 or et.isspace():
            popup = Popup(title='Error creación espacio de trabajo', separator_color=(0.9059, 0.3451, 0.3529, 1),
                          title_color=(0.9059, 0.3451, 0.3529, 1), title_font="fonts/FiraSans-ThinItalic",
                          content=Label(text='Nombre del espacio de trabajo no v\u00e1lido',
                                        font_name="fonts/FiraSans-SemiBold",
                                        color=(1, 1, 1, 1)
                                        ), size_hint=(None, None), size=(350, 100))
            popup.open()
            return True
        return False

    def es_nombre_repetido(self, et):
        if et.casefold() in [e.casefold() for e in self.proyecto.espacios_trabajo.keys()]:
            popup = Popup(title='Error creación espacio de trabajo', separator_color=(0.9059, 0.3451, 0.3529, 1),
                          title_color=(0.9059, 0.3451, 0.3529, 1), title_font="fonts/FiraSans-ThinItalic",
                          content=Label(text='Nombre de espacio de trabajo ya existente',
                                        font_name="fonts/FiraSans-SemiBold",
                                        color=(1, 1, 1, 1)
                                        ), size_hint=(None, None), size=(350, 100))
            popup.open()
            return True
        return False


class CrearPaqueteLayout(GridLayout, AbrirPrHijosComportamiento):
    rows = 2
    et_spinner = ObjectProperty()
    nombre_paq = ObjectProperty()

    def __init__(self, proyecto, **kwargs):
        super().__init__(proyecto=proyecto, **kwargs)
        self.proyecto = proyecto
        self.et_spinner.values = self.proyecto.espacios_trabajo.keys()
        if len(self.et_spinner.values) == 0:
            self.et_spinner.text = "No hay ningún espacio de trabajo"
        else:
            self.et_spinner.text = self.et_spinner.values[0]

    def comprobar_form(self, et, paq):
        if self.es_nombre_invalido(paq) or self.es_nombre_repetido(et, paq):
            return False
        return True

    def confirmar(self, inst):
        et = self.et_spinner.text
        paq = self.nombre_paq.text
        if self.comprobar_form(et, paq):
            self.proyecto.crear_paquete(et, paq)

            popup = Popup(title='Paquete creado', separator_color=(0.5451, 0.9529, 0.4235, 1),
                          title_color=(0.5451, 0.9529, 0.4235, 1), title_font="fonts/FiraSans-ThinItalic",
                          content=Label(text='Paquete creado correctamente',
                                        font_name="fonts/FiraSans-SemiBold",
                                        color=(1, 1, 1, 1)
                                        ), size_hint=(None, None), size=(350, 100))
            popup.open()

            self.recargar_proyecto()

    @staticmethod
    def es_nombre_invalido(paq):
        if len(paq) == 0 or paq.isspace():
            popup = Popup(title='Error creación paquete', separator_color=(0.9059, 0.3451, 0.3529, 1),
                          title_color=(0.9059, 0.3451, 0.3529, 1), title_font="fonts/FiraSans-ThinItalic",
                          content=Label(text='Nombre del paquete no v\u00e1lido',
                                        font_name="fonts/FiraSans-SemiBold",
                                        color=(1, 1, 1, 1)
                                        ), size_hint=(None, None), size=(350, 100))
            popup.open()
            return True
        return False

    def es_nombre_repetido(self, et, paq):
        if paq.casefold() in [p.casefold() for p in self.proyecto.espacios_trabajo[et].keys()]:
            popup = Popup(title='Error creación paquete', separator_color=(0.9059, 0.3451, 0.3529, 1),
                          title_color=(0.9059, 0.3451, 0.3529, 1), title_font="fonts/FiraSans-ThinItalic",
                          content=Label(text='Nombre de paquete ya existente',
                                        font_name="fonts/FiraSans-SemiBold",
                                        color=(1, 1, 1, 1)
                                        ), size_hint=(None, None), size=(350, 100))
            popup.open()
            return True
        return False


class CrearExperimentoLayout(GridLayout, AbrirPrHijosComportamiento):
    rows = 3
    et_spinner = ObjectProperty()
    paq_spinner = ObjectProperty()
    nombre_exp = ObjectProperty()
    tipoalg_spinner = ObjectProperty()
    nombrealg_spinner = ObjectProperty()
    tipoexp_spinner = ObjectProperty()
    slid_tmax = ObjectProperty()
    slid_tmin = ObjectProperty()
    slid_prec = ObjectProperty()
    slid_vmax = ObjectProperty()
    slid_vmin = ObjectProperty()
    slid_emax = ObjectProperty()
    slid_rep = ObjectProperty()

    def __init__(self, proyecto, **kwargs):
        super().__init__(proyecto=proyecto, **kwargs)
        self.proyecto = proyecto
        self.et_spinner.values = self.proyecto.espacios_trabajo.keys()
        if len(self.et_spinner.values) == 0:
            self.et_spinner.text = "No hay ningún espacio de trabajo"
            self.paq_spinner.text = "No hay ningún paquete"
        else:
            self.et_spinner.text = self.et_spinner.values[0]
            self.actualizar_paqs(self.et_spinner.text)
        self.tipoalg_spinner.values = [t.capitalize() for t in self.proyecto.algoritmos_permitidos.keys()
                                       if len(self.proyecto.algoritmos_permitidos[t]) > 0]
        self.tipoalg_spinner.text = self.tipoalg_spinner.values[0]
        self.tipoexp_spinner.values = ["Lista Ordenada Equidistante", "Lista Ordenada Aleatoria Con Repetición",
                                       "Lista Ordenada Aleatoria Sin Repetición"]
        self.tipoexp_spinner.text = self.tipoexp_spinner.values[0]
        self.actualizar_nombrealgs(self.tipoalg_spinner.text)
        self.rangot_desactivado = True
        self.rangov_desactivado = True

    def actualizar_paqs(self, nombre_et):
        self.paq_spinner.values = self.proyecto.espacios_trabajo[nombre_et]
        if len(self.paq_spinner.values) == 0:
            self.paq_spinner.text = "No hay ningún paquete"
        else:
            self.paq_spinner.text = self.paq_spinner.values[0]

    def actualizar_nombrealgs(self, tipoalg):
        tipo_alg = tipoalg.lower()
        self.nombrealg_spinner.values = [n.capitalize() for n in self.proyecto.algoritmos_permitidos[tipo_alg]]
        self.nombrealg_spinner.text = self.nombrealg_spinner.values[0]
        nombre_alg = self.nombrealg_spinner.text.lower()
        self.actualizar_tipoexps(tipo_alg, nombre_alg)

    def actualizar_tipoexps(self, tipo_alg, nombre_alg):
        if tipo_alg == "búsqueda" and nombre_alg != "lineal":
            try:
                self.tipoexp_spinner.values.remove("Lista Aleatoria")
                self.tipoexp_spinner.values.remove("Lista Aleatoria Sin Repetición")
            except ValueError:
                pass
        elif tipo_alg == "ordenación" or tipo_alg == "búsqueda" and nombre_alg == "lineal":
            if "Lista Aleatoria" not in self.tipoexp_spinner.values:
                self.tipoexp_spinner.values.append("Lista Aleatoria")
            if "Lista Aleatoria Sin Repetición" not in self.tipoexp_spinner.values:
                self.tipoexp_spinner.values.append("Lista Aleatoria Sin Repetición")

    def editar_rangot(self, switch):
        estado = not switch.active
        (self.slid_tmax.disabled, self.slid_tmin.disabled, self.slid_prec.disabled, self.rangot_desactivado) = \
            (estado for a in range(4))
        if estado:
            (self.slid_tmax.value, self.slid_tmin.value, self.slid_prec.value) = (32, 1, 1)

    def editar_rangov(self, switch):
        estado = not switch.active
        (self.slid_vmax.disabled, self.slid_vmin.disabled, self.slid_emax.disabled, self.rangov_desactivado) = \
            (estado for a in range(4))
        if estado:
            (self.slid_vmax.value, self.slid_vmin.value, self.slid_emax.value) = (16, 0, 1)

    def comprobar_form(self, et, paq, exp):
        if self.es_nombre_invalido(exp) or self.es_nombre_repetido(et, paq, exp):
            return False
        return True

    def confirmar(self, inst):
        et = self.et_spinner.text
        paq = self.paq_spinner.text
        exp = self.nombre_exp.text

        if len(self.paq_spinner.values) == 0:
            popup = Popup(title='Error creando experimento', separator_color=(0.9059, 0.3451, 0.3529, 1),
                          title_color=(0.9059, 0.3451, 0.3529, 1), title_font="fonts/FiraSans-ThinItalic",
                          content=Label(text='Ningún paquete v\u00e1lido donde crear un experimento',
                                        font_name="fonts/FiraSans-SemiBold",
                                        color=(1, 1, 1, 1)
                                        ), size_hint=(None, None), size=(350, 100))
            popup.open()
        elif self.comprobar_form(et, paq, exp):

            if self.rangot_desactivado:
                rt = RangoTam(int(self.slid_tmax.value))
            else:
                rt = RangoTam(int(self.slid_tmax.value), int(self.slid_tmin.value), self.slid_prec.value)
            if self.rangov_desactivado:
                rv = RangoVal(int(self.slid_vmax.value))
            else:
                rv = RangoVal(int(self.slid_vmax.value), int(self.slid_vmin.value), self.slid_emax.value)
            rep = int(self.slid_rep.value)
            tipo_alg = self.tipoalg_spinner.text.lower()
            nombre_alg = self.nombrealg_spinner.text.lower()
            tipo_exp = self.tipoexp_spinner.text.lower()

            if tipo_alg == "búsqueda":
                if nombre_alg == "binaria":
                    alg = BusquedaBinaria()
                elif nombre_alg == "exponencial":
                    alg = BusquedaExponencial()
                elif nombre_alg == "fibonacci":
                    alg = BusquedaFibonacci()
                elif nombre_alg == "interpolación":
                    alg = BusquedaInterpolacion()
                elif nombre_alg == "lineal":
                    alg = BusquedaLineal()
                else:
                    alg = BusquedaSalto()
                if tipo_exp == "lista ordenada equidistante":
                    td = TestDataBusquedaLOEquidistante(alg, rt, rv, rep)
                elif tipo_exp == "lista aleatoria":
                    td = TestDataBusquedaLAleatoria(alg, rt, rv, rep)
                elif tipo_exp == "lista ordenada aleatoria con repetición":
                    td = TestDataBusquedaLOACR(alg, rt, rv, rep)
                else:
                    td = TestDataBusquedaLOASR(alg, rt, rv, rep)
            else:
                if nombre_alg == "burbuja":
                    alg = OrdenacionBurbuja()
                elif nombre_alg == "inserción":
                    alg = OrdenacionInsercion()
                elif nombre_alg == "mergesort":
                    alg = OrdenacionMergesort()
                elif nombre_alg == "3way quicksort":
                    alg = OrdenacionQuicksort()
                elif nombre_alg == "radixsort":
                    alg = OrdenacionRadixsort()
                elif nombre_alg == "selección":
                    alg = OrdenacionSeleccion()
                else:
                    alg = OrdenacionShellsort()
                if tipo_exp == "lista ordenada equidistante":
                    td = TestDataOrdenacionLOEquidistante(alg, rt, rv, rep)
                elif tipo_exp == "lista aleatoria":
                    td = TestDataOrdenacionLAleatoria(alg, rt, rv, rep)
                elif tipo_exp == "lista ordenada aleatoria con repetición":
                    td = TestDataOrdenacionLOACR(alg, rt, rv, rep)
                elif tipo_exp == "lista ordenada aleatoria sin repetición":
                    td = TestDataOrdenacionLOASR(alg, rt, rv, rep)
                else:
                    td = TestDataOrdenacionLAleatoriaSR(alg, rt, rv, rep)

            td.analizar()
            self.proyecto.crear_experimento(et, paq, exp, td)

            popup = Popup(title='Experimento creado', separator_color=(0.5451, 0.9529, 0.4235, 1),
                          title_color=(0.5451, 0.9529, 0.4235, 1), title_font="fonts/FiraSans-ThinItalic",
                          content=Label(text='Experimento creado correctamente',
                                        font_name="fonts/FiraSans-SemiBold",
                                        color=(1, 1, 1, 1)
                                        ), size_hint=(None, None), size=(350, 100))
            popup.open()

            self.recargar_proyecto()

    @staticmethod
    def es_nombre_invalido(exp):
        if len(exp) == 0 or exp.isspace():
            popup = Popup(title='Error creación experimento', separator_color=(0.9059, 0.3451, 0.3529, 1),
                          title_color=(0.9059, 0.3451, 0.3529, 1), title_font="fonts/FiraSans-ThinItalic",
                          content=Label(text='Nombre del experimento no v\u00e1lido',
                                        font_name="fonts/FiraSans-SemiBold",
                                        color=(1, 1, 1, 1)
                                        ), size_hint=(None, None), size=(350, 100))
            popup.open()
            return True
        return False

    def es_nombre_repetido(self, et, paq, exp):
        if exp.casefold() in [e.casefold() for e in self.proyecto.espacios_trabajo[et][paq].keys()]:
            popup = Popup(title='Error creación experimento', separator_color=(0.9059, 0.3451, 0.3529, 1),
                          title_color=(0.9059, 0.3451, 0.3529, 1), title_font="fonts/FiraSans-ThinItalic",
                          content=Label(text='Nombre de experimento ya existente',
                                        font_name="fonts/FiraSans-SemiBold",
                                        color=(1, 1, 1, 1)
                                        ), size_hint=(None, None), size=(350, 100))
            popup.open()
            return True
        return False


class EliminarEspacioTrabajoLayout(GridLayout, AbrirPrHijosComportamiento):
    rows = 2
    et_spinner = ObjectProperty()

    def __init__(self, proyecto, **kwargs):
        super().__init__(proyecto=proyecto, **kwargs)
        self.proyecto = proyecto
        self.et_spinner.values = self.proyecto.espacios_trabajo.keys()
        if len(self.et_spinner.values) == 0:
            self.et_spinner.text = "No hay ningún espacio de trabajo"
        else:
            self.et_spinner.text = self.et_spinner.values[0]

    def confirmar(self, inst):
        if len(self.et_spinner.values) == 0:
            popup = Popup(title='Error eliminando espacio de trabajo', separator_color=(0.9059, 0.3451, 0.3529, 1),
                          title_color=(0.9059, 0.3451, 0.3529, 1), title_font="fonts/FiraSans-ThinItalic",
                          content=Label(text='Ningún espacio de trabajo v\u00e1lido',
                                        font_name="fonts/FiraSans-SemiBold",
                                        color=(1, 1, 1, 1)
                                        ), size_hint=(None, None), size=(350, 100))
            popup.open()
        else:
            box = BoxLayout(orientation='horizontal', cols=2)
            boton_si = Button(text='Eliminar', font_name="fonts/FiraSans-SemiBold",
                              color=(0, 0, 0, 1), background_color=(0.5451, 0.9529, 0.4235, 1))
            boton_no = Button(text='Cancelar', font_name="fonts/FiraSans-SemiBold",
                              color=(0, 0, 0, 1), background_color=(0.9059, 0.3451, 0.3529, 1))
            box.add_widget(boton_si)
            box.add_widget(boton_no)
            popup = Popup(title='Desea eliminar el espacio de trabajo: {}?'.format(self.et_spinner.text),
                          separator_color=(0.4, 0.6078, 0.5647, 1), title_color=(0.4, 0.6078, 0.5647, 1),
                          title_font="fonts/FiraSans-ThinItalic", content=box, size_hint=(None, None), size=(350, 125))
            popup.open()
            boton_si.bind(on_press=self.presionar_eliminar_et)
            boton_no.bind(on_press=self.presionar_cancelar_eliminar_et)
            boton_si.bind(on_release=self.soltar_eliminar_et)
            boton_no.bind(on_release=self.soltar_cancelar_eliminar_et)
            boton_si.bind(on_release=popup.dismiss)
            boton_no.bind(on_release=popup.dismiss)

        popup.open()

    @staticmethod
    def presionar_eliminar_et(btn):
        btn.background_color = (0.2667, 0.9059, 0.0745, 1)

    def soltar_eliminar_et(self, btn):
        btn.background_color = (0.5451, 0.9529, 0.4235, 1)
        self.proyecto.eliminar_espacio_trabajo(self.et_spinner.text)
        self.recargar_proyecto()

    @staticmethod
    def presionar_cancelar_eliminar_et(btn):
        btn.background_color = (0.8824, 0.1451, 0.0784, 1)
        btn.color = (1, 1, 1, 1)

    @staticmethod
    def soltar_cancelar_eliminar_et(btn):
        btn.background_color = (0.949, 0.4667, 0.4196, 1)
        btn.color = (0, 0, 0, 1)


class EliminarPaqueteLayout(GridLayout, AbrirPrHijosComportamiento):
    rows = 2
    et_spinner = ObjectProperty()
    paq_spinner = ObjectProperty()

    def __init__(self, proyecto, **kwargs):
        super().__init__(proyecto=proyecto, **kwargs)
        self.proyecto = proyecto
        self.et_spinner.values = self.proyecto.espacios_trabajo.keys()
        if len(self.et_spinner.values) == 0:
            self.et_spinner.text = "No hay ningún espacio de trabajo"
            self.paq_spinner.text = "No hay ningún paquete"
        else:
            self.et_spinner.text = self.et_spinner.values[0]
            self.actualizar_paqs(self.et_spinner.text)

    def actualizar_paqs(self, nombre_et):
        self.paq_spinner.values = self.proyecto.espacios_trabajo[nombre_et]
        if len(self.paq_spinner.values) == 0:
            self.paq_spinner.text = "No hay ningún paquete"
        else:
            self.paq_spinner.text = self.paq_spinner.values[0]

    def confirmar(self, inst):
        if len(self.paq_spinner.values) == 0:
            popup = Popup(title='Error eliminando paquete', separator_color=(0.9059, 0.3451, 0.3529, 1),
                          title_color=(0.9059, 0.3451, 0.3529, 1), title_font="fonts/FiraSans-ThinItalic",
                          content=Label(text='Ningún paquete v\u00e1lido',
                                        font_name="fonts/FiraSans-SemiBold",
                                        color=(1, 1, 1, 1)
                                        ), size_hint=(None, None), size=(350, 100))
            popup.open()
        else:
            box = BoxLayout(orientation='horizontal', cols=2)
            boton_si = Button(text='Eliminar', font_name="fonts/FiraSans-SemiBold",
                              color=(0, 0, 0, 1), background_color=(0.5451, 0.9529, 0.4235, 1))
            boton_no = Button(text='Cancelar', font_name="fonts/FiraSans-SemiBold",
                              color=(0, 0, 0, 1), background_color=(0.9059, 0.3451, 0.3529, 1))
            box.add_widget(boton_si)
            box.add_widget(boton_no)
            popup = Popup(title='Desea eliminar el paquete: {}?'.format(self.paq_spinner.text),
                          separator_color=(0.4, 0.6078, 0.5647, 1), title_color=(0.4, 0.6078, 0.5647, 1),
                          title_font="fonts/FiraSans-ThinItalic", content=box, size_hint=(None, None), size=(350, 125))
            popup.open()
            boton_si.bind(on_press=self.presionar_eliminar_paq)
            boton_no.bind(on_press=self.presionar_cancelar_eliminar_paq)
            boton_si.bind(on_release=self.soltar_eliminar_paq)
            boton_no.bind(on_release=self.soltar_cancelar_eliminar_paq)
            boton_si.bind(on_release=popup.dismiss)
            boton_no.bind(on_release=popup.dismiss)

        popup.open()

    @staticmethod
    def presionar_eliminar_paq(btn):
        btn.background_color = (0.2667, 0.9059, 0.0745, 1)

    def soltar_eliminar_paq(self, btn):
        btn.background_color = (0.5451, 0.9529, 0.4235, 1)
        self.proyecto.eliminar_paquete(self.et_spinner.text, self.paq_spinner.text)
        self.recargar_proyecto()

    @staticmethod
    def presionar_cancelar_eliminar_paq(btn):
        btn.background_color = (0.8824, 0.1451, 0.0784, 1)
        btn.color = (1, 1, 1, 1)

    @staticmethod
    def soltar_cancelar_eliminar_paq(btn):
        btn.background_color = (0.949, 0.4667, 0.4196, 1)
        btn.color = (0, 0, 0, 1)


class EliminarExperimentoLayout(GridLayout, AbrirPrHijosComportamiento):
    rows = 2
    et_spinner = ObjectProperty()
    paq_spinner = ObjectProperty()
    exp_spinner = ObjectProperty()

    def __init__(self, proyecto, **kwargs):
        super().__init__(proyecto=proyecto, **kwargs)
        self.proyecto = proyecto
        self.et_spinner.values = self.proyecto.espacios_trabajo.keys()
        if len(self.et_spinner.values) == 0:
            self.et_spinner.text = "No hay ningún espacio de trabajo"
            self.paq_spinner.text = "No hay ningún paquete"
            self.exp_spinner.text = "No hay ningún experimento"
        else:
            self.et_spinner.text = self.et_spinner.values[0]
            self.actualizar_paqs(self.et_spinner.text)
            self.actualizar_exps(self.et_spinner.text, self.paq_spinner.text)

    def actualizar_paqs(self, nombre_et):
        self.paq_spinner.values = self.proyecto.espacios_trabajo[nombre_et]
        if len(self.paq_spinner.values) == 0:
            self.paq_spinner.text = "No hay ningún paquete"
        else:
            self.paq_spinner.text = self.paq_spinner.values[0]

    def actualizar_exps(self, nombre_et, nombre_paq):
        self.exp_spinner.values = self.proyecto.espacios_trabajo[nombre_et][nombre_paq]
        if len(self.exp_spinner.values) == 0:
            self.exp_spinner.text = "No hay ningún experimento"
        else:
            self.exp_spinner.text = self.exp_spinner.values[0]

    def confirmar(self, inst):
        if len(self.exp_spinner.values) == 0:
            popup = Popup(title='Error eliminando experimento', separator_color=(0.9059, 0.3451, 0.3529, 1),
                          title_color=(0.9059, 0.3451, 0.3529, 1), title_font="fonts/FiraSans-ThinItalic",
                          content=Label(text='Ningún experimento v\u00e1lido',
                                        font_name="fonts/FiraSans-SemiBold",
                                        color=(1, 1, 1, 1)
                                        ), size_hint=(None, None), size=(350, 100))
            popup.open()
        else:
            box = BoxLayout(orientation='horizontal', cols=2)
            boton_si = Button(text='Eliminar', font_name="fonts/FiraSans-SemiBold",
                              color=(0, 0, 0, 1), background_color=(0.5451, 0.9529, 0.4235, 1))
            boton_no = Button(text='Cancelar', font_name="fonts/FiraSans-SemiBold",
                              color=(0, 0, 0, 1), background_color=(0.9059, 0.3451, 0.3529, 1))
            box.add_widget(boton_si)
            box.add_widget(boton_no)
            popup = Popup(title='Desea eliminar el experimento: {}?'.format(self.paq_spinner.text),
                          separator_color=(0.4, 0.6078, 0.5647, 1), title_color=(0.4, 0.6078, 0.5647, 1),
                          title_font="fonts/FiraSans-ThinItalic", content=box, size_hint=(None, None), size=(350, 125))
            popup.open()
            boton_si.bind(on_press=self.presionar_eliminar_exp)
            boton_no.bind(on_press=self.presionar_cancelar_eliminar_exp)
            boton_si.bind(on_release=self.soltar_eliminar_exp)
            boton_no.bind(on_release=self.soltar_cancelar_eliminar_exp)
            boton_si.bind(on_release=popup.dismiss)
            boton_no.bind(on_release=popup.dismiss)

        popup.open()

    @staticmethod
    def presionar_eliminar_exp(btn):
        btn.background_color = (0.2667, 0.9059, 0.0745, 1)

    def soltar_eliminar_exp(self, btn):
        btn.background_color = (0.5451, 0.9529, 0.4235, 1)
        self.proyecto.eliminar_experimento(self.et_spinner.text, self.paq_spinner.text, self.exp_spinner.text)
        self.recargar_proyecto()

    @staticmethod
    def presionar_cancelar_eliminar_exp(btn):
        btn.background_color = (0.8824, 0.1451, 0.0784, 1)
        btn.color = (1, 1, 1, 1)

    @staticmethod
    def soltar_cancelar_eliminar_exp(btn):
        btn.background_color = (0.949, 0.4667, 0.4196, 1)
        btn.color = (0, 0, 0, 1)


class CambiarGraficaLayout(GridLayout, AbrirPrHijosComportamiento):
    rows = 2
    et_spinner = ObjectProperty()
    paq_spinner = ObjectProperty()
    exp_spinner = ObjectProperty()
    tipog_spinner = ObjectProperty()
    estilog_spinner = ObjectProperty()
    interpg_spinner = ObjectProperty()

    def __init__(self, proyecto, **kwargs):
        super().__init__(proyecto=proyecto, **kwargs)
        self.proyecto = proyecto
        self.et_spinner.values = self.proyecto.espacios_trabajo.keys()
        self.tipog_spinner.values = ["Línea básica", "Línea apilada", "Barra apilada", "Barra horizontal",
                                     "Barra básica"]
        self.tipog_spinner.text = self.tipog_spinner.values[0]
        self.estilog_spinner.values = ["Por defecto", "Oscuro", "Neón", "Solarizado oscuro", "Solarizado claro",
                                       "Claro", "Limpio", "Rojo-azul", "Oscuro teñido", "Claro teñído",
                                       "Turquesa", "Verde claro", "Verde oscuro", "Oscuro verde-azul", "Azul"]
        self.estilog_spinner.text = self.estilog_spinner.values[0]
        self.interpg_spinner.values = ["Ninguna", "Cúbica", "Cuadrática", "Lagrange", "Trigonométrica",
                                       "Polinómica de Hermite"]
        self.interpg_spinner.text = self.interpg_spinner.values[0]
        if len(self.et_spinner.values) == 0:
            self.et_spinner.text = "No hay ningún espacio de trabajo"
            self.paq_spinner.text = "No hay ningún paquete"
            self.exp_spinner.text = "No hay ningún experimento"
        else:
            self.et_spinner.text = self.et_spinner.values[0]
            self.actualizar_paqs(self.et_spinner.text)
            self.actualizar_exps(self.et_spinner.text, self.paq_spinner.text)

    def actualizar_paqs(self, nombre_et):
        self.paq_spinner.values = self.proyecto.espacios_trabajo[nombre_et]
        if len(self.paq_spinner.values) == 0:
            self.paq_spinner.text = "No hay ningún paquete"
        else:
            self.paq_spinner.text = self.paq_spinner.values[0]

    def actualizar_exps(self, nombre_et, nombre_paq):
        self.exp_spinner.values = self.proyecto.espacios_trabajo[nombre_et][nombre_paq]
        if len(self.exp_spinner.values) == 0:
            self.exp_spinner.text = "No hay ningún experimento"
        else:
            self.exp_spinner.text = self.exp_spinner.values[0]

    def confirmar(self, inst):
        if len(self.exp_spinner.values) == 0:
            popup = Popup(title='Error cambiando tipo de gr\u00e1fica', separator_color=(0.9059, 0.3451, 0.3529, 1),
                          title_color=(0.9059, 0.3451, 0.3529, 1), title_font="fonts/FiraSans-ThinItalic",
                          content=Label(text='Ningún experimento v\u00e1lido',
                                        font_name="fonts/FiraSans-SemiBold",
                                        color=(1, 1, 1, 1)
                                        ), size_hint=(None, None), size=(350, 100))
            popup.open()
        else:
            self.proyecto.cambiar_tipo_grafica(self.et_spinner.text, self.paq_spinner.text, self.exp_spinner.text,
                                               self.tipog_spinner.text.casefold(), self.estilog_spinner.text.casefold(),
                                               self.interpg_spinner.text.casefold())
            popup = Popup(title='Gr\u00e1fica cambiada', separator_color=(0.5451, 0.9529, 0.4235, 1),
                          title_color=(0.5451, 0.9529, 0.4235, 1), title_font="fonts/FiraSans-ThinItalic",
                          content=Label(text='Tipo de gr\u00e1fica cambiada',
                                        font_name="fonts/FiraSans-SemiBold",
                                        color=(1, 1, 1, 1)
                                        ), size_hint=(None, None), size=(350, 100))
            popup.open()

            self.recargar_proyecto()


# Ventanas


class PrincipalScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(PrincipalLayout())


class CrearProyectoScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(CrearProyectoLayout())


class EditarProyectoScreen(Screen):
    def __init__(self, proyecto: Proyecto, **kw):
        super().__init__(**kw)
        self.add_widget(EditarProyectoLayout(proyecto))


class AbrirProyectoScreen(Screen):
    def __init__(self, proyecto: Proyecto, **kw):
        super().__init__(**kw)
        self.add_widget(AbrirProyectoLayout(proyecto))


class CrearEspacioTrabajoScreen(Screen):
    def __init__(self, proyecto: Proyecto, **kw):
        super().__init__(**kw)
        self.add_widget(CrearEspacioTrabajoLayout(proyecto))


class CrearPaqueteScreen(Screen):
    def __init__(self, proyecto: Proyecto, **kw):
        super().__init__(**kw)
        self.add_widget(CrearPaqueteLayout(proyecto))


class CrearExperimentoScreen(Screen):
    def __init__(self, proyecto: Proyecto, **kw):
        super().__init__(**kw)
        self.add_widget(CrearExperimentoLayout(proyecto))


class EliminarEspacioTrabajoScreen(Screen):
    def __init__(self, proyecto: Proyecto, **kw):
        super().__init__(**kw)
        self.add_widget(EliminarEspacioTrabajoLayout(proyecto))


class EliminarPaqueteScreen(Screen):
    def __init__(self, proyecto: Proyecto, **kw):
        super().__init__(**kw)
        self.add_widget(EliminarPaqueteLayout(proyecto))


class EliminarExperimentoScreen(Screen):
    def __init__(self, proyecto: Proyecto, **kw):
        super().__init__(**kw)
        self.add_widget(EliminarExperimentoLayout(proyecto))


class CambiarGraficaScreen(Screen):
    def __init__(self, proyecto: Proyecto, **kw):
        super().__init__(**kw)
        self.add_widget(CambiarGraficaLayout(proyecto))


# Aplicación


class AAlgApp(App):
    title = "Palgama"

    def build(self):
        sm.add_widget(PrincipalScreen(name="principal"))
        sm.add_widget(CrearProyectoScreen(name="crearp"))
        sm.add_widget(PrincipalScreen(name="principal_help"))
        return sm


def salir_aplicacion(instancia):
    print("Saliendo...")
    aj['ult_proyectos'] = proyectos
    ajustes(aj)
    exit()


if __name__ == '__main__':
    Window.minimum_width = 800
    Window.minimum_height = 600
    Window.bind(on_close=salir_aplicacion)
    # Window.fullscreen = 'auto'
    AAlgApp().run()
