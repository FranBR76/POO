import tkinter as tk
from tkinter import messagebox
from veiculo import Veiculo
from veiculoDAO import VeiculoDAO
from usuario import Usuario
from usuarioDAO import UsuarioDAO
from app import App
from tkinter import ttk #? PARTE DO SELECT BOX


class PlanoViagem:
    def __init__(self, root, id_usuario):
        self.dao = UsuarioDAO()
        self.id_usuario = id_usuario
        self.root = root
        self.root.title("Atualizar dados")
        self.root.geometry("1280x720")
        self.root.configure(bg="lightblue")

        card = tk.Frame(root, bg="white", bd=2, relief="raised", padx=10, pady=10)
        card.pack(padx=20, pady=20, fill="both", expand=True)
        
        titulo = tk.Label(card, text="Planejamento de Viagem", font=("Helvetica", 14, "bold"))
        titulo.pack(anchor="w")

        descricao = tk.Label(card, text="Informe os dados para fornecermos o plano de viagem ideal para você. \nPara a bateria pode-se informar o valor arredondado para baixo", wraplength=260)
        descricao.pack(anchor="w", pady=(10, 10))

        self.label_partida = tk.Label(card, text="Qual o local de partida?").pack(anchor="w")
        self.entry_partida = tk.Entry(card, font="Arial: 15").pack(anchor="w")
        self.label_destino = tk.Label(card, text="Qual o destino?").pack(pady=5, anchor="w")
        self.entry_destino = tk.Entry(card, font="Arial: 15").pack(pady=5, anchor="w")
        self.label_bateria = tk.Label(card, text="Qual a porcetagem de bateria?").pack(pady=5, anchor="w")
        #self.label_partida = tk.Entry(card).pack(pady=5) #!FAZER SELECT BOX
        opcoes = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
        self.entry_bateria = ttk.Combobox(card, values=opcoes , state="readonly")
        self.entry_bateria.set("Selecione a porcentagem")  # Valor inicial
        self.entry_bateria.pack(pady=20, anchor="w")


        # Conteúdo do card

# Criando a Combobox