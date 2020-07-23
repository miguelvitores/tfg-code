from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.core.window import Window
from bin.cargar import carga_ajustes
from bin.usuarios import Alumno, Profesor
from bin.proyecto import Proyecto
from kivy.config import Config
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.uix.button import Button


Config.set('graphics', 'resizable', 1)
ajustes = carga_ajustes()
proyectos = ajustes['ult_proyectos']


class SpinnerOpciones(SpinnerOption):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0.7725, 0.9882, 0.9412, 1)
        self.color = (0, 0, 0, 1)


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
        self.background_color = (0.4, 0.6078, 0.5647, 1)
        self.color = (1, 1, 1, 1)
        self.font_name = "fonts/FiraSans-Medium"


class DropdownAbrirProyecto(DropDown):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for p in proyectos:
            btn = Button(text=p.nombre, size_hint_y=None, height=50, background_color=(0.4, 0.6078, 0.5647, 1))
            btn.bind(on_release=lambda btn: self.select(btn.text))
            self.add_widget(btn)
        btn = Button(text="Importar Proyecto", size_hint_y=None, height=50, background_color=(0.4, 0.6078, 0.5647, 1))
        btn.bind(on_release=lambda btn: self.select(btn.text))
        self.add_widget(btn)


class DropdownProyectos(DropDown):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for p in proyectos:
            btn = Button(text=p.nombre, size_hint_y=None, height=50, background_color=(0.4, 0.6078, 0.5647, 1))
            btn.bind(on_release=lambda btn: self.select(btn.text))
            self.add_widget(btn)


class PrincipalLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        spinner = self.ids.usuarios_spinner
        usuario = ajustes['ult_usuario']
        spinner.text = usuario.tipo.capitalize()
        if isinstance(usuario, Alumno):
            self.ids.buttons_layout.remove_widget(self.ids.crear_proyecto)
            self.ids.buttons_layout.remove_widget(self.ids.editar_proyecto)
        self.dpdab = DropdownAbrirProyecto()
        self.dpdab.bind(on_select=self.llamada_dpdab)
        self.dpdcp = DropdownProyectos()
        self.dpdcp.bind(on_select=self.llamada_dpdcp)
        self.dpdep = DropdownProyectos()
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
        if usuario is "Profesor":
            ajustes['ult_usuario'] = Profesor()
            self.ids.buttons_layout.add_widget(self.ids.crear_proyecto)
            self.ids.buttons_layout.add_widget(self.ids.editar_proyecto)
        elif usuario is "Alumno":
            ajustes['ult_usuario'] = Alumno()
            self.ids.buttons_layout.remove_widget(self.ids.crear_proyecto)
            self.ids.buttons_layout.remove_widget(self.ids.editar_proyecto)


class PrincipalApp(App):
    def build(self):
        return PrincipalLayout()


if __name__ == '__main__':
    Window.minimum_width = 800
    Window.minimum_height = 600
    Window.fullscreen = 'auto'
    PrincipalApp().run()
