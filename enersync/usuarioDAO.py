import tkinter as tk
from tkinter import messagebox
import mysql.connector 
from usuario import Usuario

class UsuarioDAO:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "startupenersync"
            
        )
        self.cursor = self.conexao.cursor()
        
    
    def criar(self, usuario):
        sql = "INSERT INTO usuario (nome, email) VALUES (%s, %s)"
        self.cursor.execute(sql, (usuario.nome, usuario.email))
        self.conexao.commit()
        self.conexao.close()

    def listar(self):
        self.cursor.execute("SELECT * FROM usuario")
        return self.cursor.fetchall()
        
    
    def atualizar(self, usuario):
        sql = "UPDATE usuario SET nome = %s, email = %s WHERE id = %s"
        self.cursor.execute(sql, (usuario.nome, usuario.email, usuario.id))
        self.conexao.commit()
        self.conexao.close()

    def deletar(self, id):
        sql = "DELETE FROM usuario WHERE id = %s"
        self.cursor.execute(sql, (id,))
        self.conexao.commit()
        self.conexao.close()
        