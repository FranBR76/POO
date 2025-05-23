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
        sql = "INSERT INTO usuario (nome, email, senha, cpf, dt_nasc) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (usuario.nome, usuario.email, usuario.senha, usuario.cpf, usuario.dt_nasc))
        self.conexao.commit()
       

    def listar(self):
        self.cursor.execute("SELECT * FROM usuario")
        return self.cursor.fetchall()
        
    
    def atualizar(self, usuario):
        sql = "UPDATE usuario SET nome = %s, email = %s WHERE id = %s"
        self.cursor.execute(sql, (usuario.nome, usuario.email, usuario.id))
        self.conexao.commit()
       

    def deletar(self, id):
        sql = "DELETE FROM usuario WHERE id = %s"
        self.cursor.execute(sql, (id,))
        self.conexao.commit()
       
    
    def verificar_usuario(self, email, senha):
        try:
            sql = "SELECT * FROM usuario WHERE email = %s AND senha = %s"
            self.cursor.execute(sql, (email, senha))
            resultado = self.cursor.fetchone()
            return resultado  # retorna None se não encontrou
        except mysql.connector.Error as erro:
            print("Erro ao consultar usuário:", erro)
            return None