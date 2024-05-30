from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
import sys
sys.path.append("src")
sys.path.append(".")

from Controller import Control
from Model.Juego_principal import TableroBatallaNaval

class alerta_jugador1(Popup):
    def __init__(self, **kwargs):
        super(alerta_jugador1, self).__init__(**kwargs)
        self.title = 'Alerta'
        self.size_hint = (None, None)
        self.size = (300, 200)
        
        contenido_caja = BoxLayout(orientation='vertical')
        
        mensaje_alerta = Label(text='El jugador 1 ha ganado')
        contenido_caja.add_widget(mensaje_alerta)
        self.content = contenido_caja
class alerta_jugador2(Popup):
    def __init__(self, **kwargs):
        super(alerta_jugador2, self).__init__(**kwargs)
        self.title = 'Alerta'
        self.size_hint = (None, None)
        self.size = (300, 200)
        
        contenido_caja = BoxLayout(orientation='vertical')
        
        mensaje_alerta = Label(text='El jugador 2 ha ganado')
        contenido_caja.add_widget(mensaje_alerta)
        self.content = contenido_caja
class MyPopup_impacto(Popup):
    def __init__(self, **kwargs):
        super(MyPopup_impacto, self).__init__(**kwargs)
        self.title = 'Alerta'
        self.size_hint = (None, None)
        self.size = (300, 200)
        
        content_layout = BoxLayout(orientation='vertical')
        
        mensaje_barco_destruido = Label(text='Barco destruido')
        content_layout.add_widget(mensaje_barco_destruido)
        self.content = content_layout         

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        
        # Initialize the game boards for both players
        self.Tablero_Jugador1 = TableroBatallaNaval(10, 10)
        self.Tablero_Jugador1.colocar_naves()
        self.Tablero_Jugador2 = TableroBatallaNaval(10, 10)
        self.Tablero_Jugador2.colocar_naves()


        ContenedorA= BoxLayout(orientation= "vertical")
        # Create labels to display whose turn it is
        self.Jugador_En_Turno = Label(text="El turno de disparar es para el Jugador 1", font_size="30sp", size_hint_y=0.2)
        ContenedorA.add_widget(self.Jugador_En_Turno)

        Contenedor1 = BoxLayout(orientation='vertical')

        #Crear botones del mapa del Jugador 1
        for numero_fila in range(10):
            fila = BoxLayout(orientation="horizontal")
            for numero_columna in range(10):
                casilla = Button(text='O', font_size=20,
                                 disabled=False
                                 )
                casilla.fila = numero_fila
                casilla.columna = numero_columna
                casilla.bind(on_press=self.Disparo_Jugador1)
                if self.Tablero_Jugador2.buscar_barco():
                    casilla.bind(on_press=self.show_popup)
                fila.add_widget(casilla)
            Contenedor1.add_widget(fila)

        ContenedorA.add_widget(Contenedor1)
        self.add_widget(ContenedorA)
    def show_popup2(self):
        popup = MyPopup_impacto()
        popup.open()
    
    def Disparo_Jugador1(self, instance):
        
        result = self.Tablero_Jugador2.disparar(instance.fila, instance.columna, self.Tablero_Jugador2.tablero)

        
        if result == 'X':
            instance.text = 'X'
            instance.background_color= (255, 0, 0, 1)
            instance.disabled= True
        elif result == 'N':
            instance.text = ' '
            instance.background_color=(0, 255, 255, 0.5) 
            instance.disabled= True

        # Check for sunk ships
        barco_hundido = self.Tablero_Jugador2.barco_hundido()
        if barco_hundido :
            self.show_popup2()

        self.manager.current = 'CambioDePantalla'
    def show_popup(self, instance):
        popup = alerta_jugador1()
        popup.open() 


class CambioDePantalla(Screen):
    def __init__(self, Tablero_Jugador1, **kwargs):
        super(CambioDePantalla, self).__init__(**kwargs)
        self.Tablero_Jugador1 = Tablero_Jugador1

        ContenedorB= BoxLayout(orientation="vertical")
       
        self.Jugador_En_Turno = Label(text="El turno de disparar es para el Jugador 2", font_size="30sp", size_hint_y=0.2)
        ContenedorB.add_widget(self.Jugador_En_Turno)

        Contenedor2 = BoxLayout(orientation='vertical')

        #Crear botones del mapa del Jugador 2
        for numero_fila in range(10):
            fila = BoxLayout(orientation="horizontal")
            for numero_columna in range(10):
                casilla = Button(text='O', font_size=20, 
                                 disabled=False
                                 )
                casilla.fila = numero_fila
                casilla.columna = numero_columna
                casilla.bind(on_press=self.Disparo_Jugador2)
                if self.Tablero_Jugador1.buscar_barco():
                    casilla.bind(on_press=self.show_popup)
                fila.add_widget(casilla)
            Contenedor2.add_widget(fila)

        ContenedorB.add_widget(Contenedor2)
        self.add_widget(ContenedorB)
    def show_popup2(self):
        popup = MyPopup_impacto()
        popup.open()

    def Disparo_Jugador2(self, instance):

        result = self.Tablero_Jugador1.disparar(instance.fila, instance.columna, self.Tablero_Jugador1.tablero)

 
        if result == 'X':
            instance.text = 'X'
            instance.background_color= (255, 0, 0, 1)
            instance.disabled= True
        elif result == 'N':
            instance.text = ' '
            instance.background_color=(0, 255, 255, 0.5) 
            instance.disabled= True
        barco_hundido =self.Tablero_Jugador1.barco_hundido()
        if barco_hundido:
            self.show_popup2()

        self.manager.current = 'Turno_Jugador1'
  
    def show_popup(self, instance):
        popup = alerta_jugador2()
        popup.open()

class BattleshipApp(App):
    def build(self):
        sm = ScreenManager()

        # Create instances of screens
        Pantalla1 = GameScreen(name='Turno_Jugador1')
        Pantalla2 = CambioDePantalla(name='CambioDePantalla', Tablero_Jugador1=Pantalla1.Tablero_Jugador1)

        sm.add_widget(Pantalla1)
        sm.add_widget(Pantalla2)

        return sm

if __name__ == '__main__':
    BattleshipApp().run()

