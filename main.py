#!bin/python3
# coding: utf-8

from tkinter import *
import pygubu.builder

class Main:

    root = None

    def __init__(self):

        self.root = root = Tk()
        self.root.title('Contabil')

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('ui/main.ui')

        #3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('root', root)


