import tkinter as tk
from tkinter import messagebox
from veiculo import Veiculo
from veiculoDAO import VeiculoDAO
from usuario import Usuario
from usuarioDAO import UsuarioDAO
from app import App


class PlanoViagem:
    def __init__(self, root, id_usuario):
        self.dao = UsuarioDAO()
        self.id_usuario = id_usuario
        self.root = root
        self.root.title("Atualizar dados")
        self.root.geometry("1280x720")
        self.root.configure(bg="lightblue")


        self.label_partida = tk.Label(root, text="Qual o local de partida?").pack()
        self.label_partida = tk.Entry(root, font="Arial: 15").pack()
        self.label_partida = tk.Label(root, text="Qual o destino?").pack()
        self.label_partida = tk.Entry(root, font="Arial: 15").pack()
        self.label_partida = tk.Label(root, text="Qual a porcetagem de bateria?").pack()
        self.label_partida = tk.Entry(root, font="Arial: 15").pack() #!FAZER SELECT BOX
        