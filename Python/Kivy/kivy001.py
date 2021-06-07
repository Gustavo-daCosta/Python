from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Test(App):
    def build(self):
        box = BoxLayout()
        button = Button(text = 'Botao 1')
        label = Label(text = 'Texto 1')
        box.add_widget(button)
        return box

Test().run()