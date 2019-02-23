#!bin/python3
# coding: utf-8
__author__ = {
    "nome": "Guilherme Isaías Silva",
    'email': "guilherme19971936@gmail.com"
}

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class InicioApp(App):
    def build(self):
        return RootWidget()