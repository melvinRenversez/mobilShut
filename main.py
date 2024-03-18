import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

kivy.require('2.0.0')

class GameView(BoxLayout):
    def __init__(self):
        super(GameView, self).__init__()
        self.orientation = 'vertical'  # Définit l'orientation de la disposition en boîte

        # Créez un bouton et ajoutez-le à la disposition en boîte
        self.button = Button(text='Cliquez ici !', size_hint=(None, None))
        self.button.bind(on_press=self.on_button_press)
        self.add_widget(self.button)

    def on_button_press(self, instance):
        print("Le bouton a été cliqué !")

class MelApp(App):
    def build(self):
        return GameView()

melApp = MelApp()
melApp.run()
