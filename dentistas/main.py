#!bin/python3
# coding: utf-8

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class DentistasLayout(FloatLayout):
    pass

class DentistasApp(App):

    def build(self):
        return DentistasLayout()