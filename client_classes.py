from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

    def build(self):
        label = Label(text="дурак онлайн")

        return label
