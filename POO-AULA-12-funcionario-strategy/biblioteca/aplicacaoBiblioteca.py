import tkinter as tk
from tkinter import messagebox
from bibliotecario import Bibliotecario

class Aplicacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Bibliotecario")

        # self.bibliotecarios = {}

        tk.Label(root, text="Nome:").grid(row=0, column=0)
        self.entry_nome = tk.Entry(root)
        self.entry_nome.grid(row=0, column=1)

        
        tk.Label(root, text="CPF:").grid(row=1, column=0)
        self.entry_cpf = tk.Entry(root)
        self.entry_cpf.grid(row=1, column=1)

        
        tk.Label(root, text="Cargo:").grid(row=2, column=0)
        self.entry_cargo = tk.Entry(root)
        self.entry_cargo.grid(row=2, column=1)

        
        tk.Label(root, text="Salario").grid(row=3, column=0)
        self.entry_salario = tk.Entry(root)
        self.entry_salario.grid(row=3, column=1)

        
        tk.Label(root, text="Senha").grid(row=4, column=0)
        self.entry_senha = tk.Entry(root)
        self.entry_senha.grid(row=4, column=1)

        tk.Button(root, text="Cadastrar Bibliotecario", command=self.cadastrar_bibliotecario).grid(row=5, column=0, columnspan=2)