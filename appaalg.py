from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from bin.cargar import carga_ajustes
from bin.serializar import ajustes
from bin.usuarios import Alumno, Profesor
from bin.proyecto import Proyecto
from kivy.config import Config
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.lang import Builder


Config.set('graphics', 'resizable', 0)
aj = carga_ajustes()
proyectos = aj['ult_proyectos']


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


class DropdownAbrirProyecto(DropDown):
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

    def presionar_boton(self, btn):
        btn.background_color = (0.2706, 0.4118, 0.3804, 1)
        btn.color = (1, 1, 1, 1)

    def soltar_boton(self, btn):
        btn.background_color = (0.4, 0.6078, 0.5647, 1)
        btn.color = (0, 0, 0, 1)
        self.select(btn.text)


class DropdownProyectos(DropDown):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for p in proyectos:
            btn = Button(text=p.nombre, size_hint_y=None, height=50, background_normal='', background_down='',
                         background_color=(0.4, 0.6078, 0.5647, 1))
            btn.bind(on_press=self.presionar_boton, on_release=self.soltar_boton)
            self.add_widget(btn)

    def presionar_boton(self, btn):
        btn.background_color = (0.2706, 0.4118, 0.3804, 1)
        btn.color = (1, 1, 1, 1)

    def soltar_boton(self, btn):
        btn.background_color = (0.4, 0.6078, 0.5647, 1)
        btn.color = (0, 0, 0, 1)
        self.select(btn.text)


class PrincipalLayout(GridLayout):
    botones = ObjectProperty()
    cp = ObjectProperty()
    ep = ObjectProperty()
    uspinner = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        usuario = aj['ult_usuario']
        if isinstance(usuario, Profesor):
            self.botones.remove_widget(self.cp)
            self.botones.remove_widget(self.ep)
        self.uspinner.text = usuario.tipo.capitalize()
        self.dpdep = DropdownProyectos()
        self.dpdcp = DropdownProyectos()
        self.dpdab = DropdownAbrirProyecto()
        self.dpdab.bind(on_select=self.llamada_dpdab)
        self.dpdcp.bind(on_select=self.llamada_dpdcp)
        self.dpdep.bind(on_select=self.llamada_dpdep)

    def llamada_dpdab(self, instancia, nombre):
        print(instancia, nombre)

    def llamada_dpdcp(self, instancia, nombre):
        print(instancia, nombre)

    def llamada_dpdep(self, instancia, nombre):
        print(instancia, nombre)

    def soltar_dpdab(self, instancia):
        self.dpdab.open(instancia)

    def soltar_dpdcp(self, instancia):
        self.dpdcp.open(instancia)

    def soltar_dpdep(self, instancia):
        self.dpdep.open(instancia)

    def usuario_cambio(self, usuario):
        if usuario == "Profesor":
            aj['ult_usuario'] = Profesor()
            self.botones.add_widget(self.cp)
            self.botones.add_widget(self.ep)
        elif usuario == "Alumno":
            aj['ult_usuario'] = Alumno()
            self.botones.remove_widget(self.cp)
            self.botones.remove_widget(self.ep)

    def cambiar_a_crear_proyecto(self, instancia):
        sm.switch_to(sm.get_screen("crearp"))

    def salir(self, instancia):
        Window.close()


class CrearProyectoLayout(GridLayout):
    pass


class PrincipalScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(PrincipalLayout())


class CrearProyectoScreen(Screen):
    pass


sm = ScreenManager(transition=FadeTransition())


class AAlgApp(App):
    title = "Análisis de Algoritmos"

    def build(self):
        sm.add_widget(PrincipalScreen(name="principal"))
        sm.add_widget(CrearProyectoScreen(name="crearp"))
        return sm


def salir_aplicacion(instancia):
    print("Saliendo...")
    ajustes(aj)
    exit()


if __name__ == '__main__':
    Window.minimum_width = 800
    Window.minimum_height = 600
    Window.bind(on_close=salir_aplicacion)
    # Window.fullscreen = 'auto'
    AAlgApp().run()
