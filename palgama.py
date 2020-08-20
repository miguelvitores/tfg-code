from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, ScreenManagerException
from bin.serializar import ajustes, eliminar_recursivamente
from bin.usuarios import Alumno, Profesor
from bin.proyecto import Proyecto
from kivy.config import Config
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.lang import Builder

import bin.cargar as cargar
import os

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
        Window.restore()
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


class DropdownGraficasInteractivas(DropdownComportamiento):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        btn = Button(text="Work in progress!", size_hint_y=None, height=50, background_normal='',
                     background_down='', background_color=(0.4, 0.6078, 0.5647, 1))
        btn.bind(on_press=self.presionar_boton, on_release=self.soltar_boton)
        self.add_widget(btn)


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
        self.dpdgi = DropdownGraficasInteractivas()
        self.dpdta = DropdownTeoriaAlgortimos(self.proyecto)

    def soltar_dpdex(self, instancia):
        self.dpdex.open(instancia)

    def soltar_dpdgi(self, instancia):
        self.dpdgi.open(instancia)

    def soltar_dpdta(self, instancia):
        self.dpdta.open(instancia)

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
        if self.es_nombrepr_invalido(et) or self.es_nombrepr_repetido(et):
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

            # Eliminamos la ventana de crear espacios de trabajo
            sm.remove_widget(sm.get_screen("add_espt_{0}".format(self.proyecto.nombre)))

    @staticmethod
    def es_nombrepr_invalido(et):
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

    def es_nombrepr_repetido(self, et):
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

    def __init__(self, proyecto, **kwargs):
        super().__init__(proyecto=proyecto, **kwargs)
        self.proyecto = proyecto


class CrearExperimentoLayout(GridLayout, AbrirPrHijosComportamiento):
    rows = 2

    def __init__(self, proyecto, **kwargs):
        super().__init__(proyecto=proyecto, **kwargs)
        self.proyecto = proyecto


class EliminarEspacioTrabajoLayout(GridLayout, AbrirPrHijosComportamiento):
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
        # Eliminamos la ventana de crear espacios de trabajo
        sm.remove_widget(sm.get_screen("el_espt_{0}".format(self.proyecto.nombre)))

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

    def __init__(self, proyecto, **kwargs):
        super().__init__(proyecto=proyecto, **kwargs)
        self.proyecto = proyecto


class EliminarExperimentoLayout(GridLayout, AbrirPrHijosComportamiento):
    rows = 2

    def __init__(self, proyecto, **kwargs):
        super().__init__(proyecto=proyecto, **kwargs)
        self.proyecto = proyecto


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
