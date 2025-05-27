import tkinter as tk
from tkinter import messagebox
import mysql.connector


class Veiculo:
    def __init__(self, id=None, id_usuario="", marca="", modelo="" ):
        self.__id = id
        self.__id_usuario = id_usuario
        self.__marca = marca
        self.__modelo = modelo

    @property
    def id(self):
        return self.__id
    
    @property
    def id_usuario(self):
        return self.__id_usuario
    
    @property
    def marca(self):
        return self.__marca
    
    @property
    def modelo(self):
        return self.__modelo
    

    @id_usuario.setter
    def id_usuario(self, valor):
        self.__id_usuario = valor