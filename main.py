import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


kivy.require('2.0.0')

class GameView(BoxLayout):
    def __init__(self):
        super(gameView, self).__init__()
    

class MelApp(App):
    def build(self):
        return GameView()
    

melApp = MelApp()
melApp.run()