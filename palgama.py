from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, ScreenManagerException
from bin.serializar import ajustes
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


class DropdownExperimentos(DropdownComportamiento):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        btn = Button(text="Crear espacio de trabajo", size_hint_y=None, height=50, background_normal='',
                     background_down='', background_color=(0.4, 0.6078, 0.5647, 1))
        btn.bind(on_press=self.presionar_boton, on_release=self.soltar_boton)
        self.add_widget(btn)
        btn = Button(text="Crear paquete", size_hint_y=None, height=50, background_normal='',
                     background_down='',
                     background_color=(0.4, 0.6078, 0.5647, 1))
        btn.bind(on_press=self.presionar_boton, on_release=self.soltar_boton)
        self.add_widget(btn)
        btn = Button(text="Crear experimento", size_hint_y=None, height=50, background_normal='',
                     background_down='',
                     background_color=(0.4, 0.6078, 0.5647, 1))
        btn.bind(on_press=self.presionar_boton, on_release=self.soltar_boton)
        self.add_widget(btn)


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

    def llamada_dpdab(self, instancia, nombre):
        pr = [p for p in proyectos if p.nombre is nombre][0]
        try:
            screen = sm.get_screen("abrirp_{0}".format(nombre))
        except ScreenManagerException:
            screen = AbrirProyectoScreen(pr, name="abrirp_{0}".format(nombre))
            sm.add_widget(screen)

        Window.maximize()
        sm.switch_to(screen)

    def llamada_dpdcp(self, instancia, nombre):
        print(instancia, nombre)

    def llamada_dpdep(self, instancia, nombre):
        pr = [p for p in proyectos if p.nombre is nombre][0]
        try:
            screen = sm.get_screen("editarp_{0}".format(nombre))
        except ScreenManagerException:
            screen = EditarProyectoScreen(pr, name="editarp_{0}".format(nombre))
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

    def presionar_eliminar_proyecto(self, btn):
        btn.background_color = (0.2667, 0.9059, 0.0745, 1)

    def soltar_eliminar_proyecto(self, btn):
        btn.background_color = (0.5451, 0.9529, 0.4235, 1)
        proyectos.remove(self.proyecto_a_eliminar)
        self.eliminar_recursivamente(self.proyecto_a_eliminar.ruta)
        sm.switch_to(sm.get_screen("principal_help"))
        sm.remove_widget(sm.get_screen("principal"))
        sm.add_widget(PrincipalScreen(name="principal"))
        sm.switch_to(sm.get_screen("principal"))

    def eliminar_recursivamente(self, ruta):
        for f in os.walk(ruta, topdown=False):
            for d in f[1]:
                os.rmdir(os.path.join(f[0], d))
            for file in f[2]:
                os.remove(os.path.join(f[0], file))
        os.rmdir(ruta)

    def presionar_cancelar_eliminar_proyecto(self, btn):
        btn.background_color = (0.8824, 0.1451, 0.0784, 1)
        btn.color = (1, 1, 1, 1)

    def soltar_cancelar_eliminar_proyecto(self, btn):
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

    def cambiar_a_crear_proyecto(self, instancia):
        sm.switch_to(sm.get_screen("crearp"))

    def salir(self, instancia):
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

    def es_nombrepr_invalido(self, pr):
        if len(pr) == 0 or pr.isspace():
            print("Nombre no valido")
            popup = Popup(title='Error creación proyecto', separator_color=(0.9059, 0.3451, 0.3529, 1),
                          title_color=(0.9059, 0.3451, 0.3529, 1), title_font="fonts/FiraSans-ThinItalic",
                          content=Label(text='Nombre del proyecto no v\u00e1lido',
                                        font_name="fonts/FiraSans-SemiBold",
                                        color=(1, 1, 1, 1)
                                        ), size_hint=(None, None), size=(250, 100))
            popup.open()
            return True
        return False

    def es_nombrepr_repetido(self, pr):
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
            algs_seleccionados = self.get_algs_elegidos()
            p = Proyecto(pr, algs_seleccionados)
            proyectos.remove(self.proyecto)
            os.rename(self.proyecto.ruta, p.ruta)
            proyectos.insert(0, p)
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
            sm.remove_widget(sm.get_screen("editarp"))


class AbrirProyectoLayout(BoxLayout):
    label_nombrepr = ObjectProperty()
    filechooser = ObjectProperty()

    def __init__(self, proyecto, **kwargs):
        super().__init__(**kwargs)
        self.proyecto = proyecto
        self.label_nombrepr.text = self.proyecto.nombre
        self.filechooser.rootpath = os.getcwd()
        self.dpdex = DropdownExperimentos()
        self.dpdgi = DropdownGraficasInteractivas()
        self.dpdta = DropdownTeoriaAlgortimos(self.proyecto)

    def soltar_dpdex(self, instancia):
        self.dpdex.open(instancia)

    def soltar_dpdgi(self, instancia):
        self.dpdgi.open(instancia)

    def soltar_dpdta(self, instancia):
        self.dpdta.open(instancia)

    def volver_a_principal(self, inst):
        Window.restore()
        sm.switch_to(sm.get_screen("principal"))

    def get_nombre_proyecto(self):
        return self.proyecto.nombre


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
    def __init__(self, proyecto, **kw):
        super().__init__(**kw)
        self.add_widget(EditarProyectoLayout(proyecto))


class AbrirProyectoScreen(Screen):
    def __init__(self, proyecto, **kw):
        super().__init__(**kw)
        self.add_widget(AbrirProyectoLayout(proyecto))


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
