import tkinter as tk
from tkinter import messagebox
import mysql.connector 
from veiculo import Veiculo
from usuario import Usuario
from usuarioDAO import UsuarioDAO

class VeiculoDAO:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "startupenersync"
            
        )
        self.cursor = self.conexao.cursor()
        
    def cadastrar(self, veiculo):
        sql = "INSERT INTO veiculo (id_usuario, marca, modelo) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (veiculo.id_usuario, veiculo.marca, veiculo.modelo))
        self.conexao.commit()
    
    def listarautos(self):
        self.cursor.execute("SELECT * FROM veiculo")
        return self.cursor.fetchall()