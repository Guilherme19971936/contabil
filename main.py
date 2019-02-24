#!bin/python3
# coding: utf-8

from tkinter import *
from pygubu.builder import *
from pygubu import TkApplication

class Main(TkApplication):

    root = None

    def __init__(self):
        super(Main, self).__init__()

        self.root = Tk()


    def _create_ui(self):

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        self.builder.add_from_file('ui/main.ui')

        #4: Create the widget using a master as parent
        self.mainwindow = builder.get_object('root', self.root)

        # 3: Associe o menu principal ao frame principal
        self.mainmenu = builder.get_object('menu', self.root)
        self.set_menu(self.mainmenu)

        builder.connect_callbacks(self)

    def tela_dentistas():
        messagebox.showinfo('Fornecedores', 'Você clicou sobre o item <consultar>.')