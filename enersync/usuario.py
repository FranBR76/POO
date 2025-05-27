import tkinter as tk
from tkinter import messagebox
import mysql.connector

class Usuario:
    def __init__(self, id=None, nome="", email="", senha="", permissoes="", cpf="", dt_nasc="" ):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__permissoes = permissoes
        self.__cpf = cpf
        self.__dt_nasc = dt_nasc

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome
    @property
    def email(self):
        return self.__email
    @property
    def email(self):
        return self.__email
    @property
    def senha(self):
        return self.__senha
    @property
    def permissoes(self):
        return self.__permissoes
    @property
    def cpf(self):
        return self.__cpf
    @property
    def dt_nasc(self):
        return self.__dt_nasc
