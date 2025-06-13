import tkinter as tk
from tkinter import messagebox
from veiculo import Veiculo
from veiculoDAO import VeiculoDAO
from usuario import Usuario
from usuarioDAO import UsuarioDAO
from app import App

from metodos import Voltar
from tkinter import ttk #? PARTE DO SELECT BOX


# class PlanoViagem:
#     def __init__(self, root, id_usuario):
#         self.dao = UsuarioDAO()
#         self.id_usuario = id_usuario
#         self.root = root
#         self.root.title("Atualizar dados")
#         self.root.geometry("1280x720")
#         self.root.configure(bg="lightblue")

#         self.card = tk.Frame(root, bg="white", bd=2, relief="raised", padx=10, pady=10)
#         self.card.pack(padx=20, pady=20, fill="both", expand=True)
        
#         tk.Button(self.card, text="< Voltar", command=self.gerarPlano, bg="#333", fg="White").pack(pady=20, anchor="w")
#         titulo = tk.Label(self.card, text="Planejamento de Viagem", font=("Helvetica", 14, "bold"))
#         titulo.pack(anchor="w")

#         descricao = tk.Label(self.card, text="Informe os dados para fornecermos o plano de viagem ideal para você. \nPara a bateria pode-se informar o valor arredondado para baixo", wraplength=260)
#         descricao.pack(anchor="w", pady=(10, 10))

#         self.label_partida = tk.Label(self.card, text="Qual o local de partida?").pack(anchor="w")
#         self.entry_partida = tk.Entry(self.card, font="Arial: 15").pack(anchor="w")
#         self.label_destino = tk.Label(self.card, text="Qual o destino?").pack(pady=5, anchor="w")
#         self.entry_destino = tk.Entry(self.card, font="Arial: 15").pack(pady=5, anchor="w")
#         self.label_bateria = tk.Label(self.card, text="Qual a porcetagem de bateria?").pack(pady=5, anchor="w")
#         #self.label_partida = tk.Entry(self.card).pack(pady=5) #!FAZER SELECT BOX
#         opcoes = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
#         self.entry_bateria = ttk.Combobox(self.card, values=opcoes , state="readonly")
#         self.entry_bateria.set("Selecione a porcentagem")  # Valor inicial
#         self.entry_bateria.pack(pady=20, anchor="w")

#         tk.Button(self.card, text="Gerar Plano", command=self.gerarPlano, bg="#333", fg="White").pack(pady=20, anchor="w")


#     def gerarPlano(self):
#         img = tk.PhotoImage(file="enersync/imgs/plano.png")  # Caminho da imagem
#         self.img = img
#         label = tk.Label(self.card, image=self.img)
#         label.pack()

class PlanoViagem(Voltar):
    def __init__(self, root, id_usuario):
        self.dao = UsuarioDAO()
        self.id_usuario = id_usuario
        self.root = root
        self.root.title("Atualizar dados")
        self.root.geometry("1280x720")
        self.root.configure(bg="lightblue")
       

        self.card = tk.Frame(root, bg="white", bd=2, relief="raised", padx=10, pady=10)
        self.card.pack(padx=20, pady=20, fill="both", expand=True)

        # Container horizontal: esquerda = formulário | direita = imagem
        self.container = tk.Frame(self.card, bg="white")
        self.container.pack(fill="both", expand=True)

        # Frame para os campos de entrada (lado esquerdo)
        self.form_frame = tk.Frame(self.container, bg="white")
        self.form_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        # Frame para a imagem (lado direito)
        self.img_frame = tk.Frame(self.container, bg="white")
        self.img_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Botão voltar
        tk.Button(self.form_frame, text="< Voltar", command=self.voltar, bg="#333", fg="White").pack(pady=10, anchor="w")

        # Texto e campos
        tk.Label(self.form_frame, text="Planejamento de Viagem", font=("Helvetica", 14, "bold"), bg="white").pack(anchor="w")

        descricao = tk.Label(self.form_frame, text="Informe os dados para fornecermos o plano de viagem ideal para você.\nPara a bateria pode-se informar o valor arredondado para baixo",
                             wraplength=300, bg="white")
        descricao.pack(anchor="w", pady=(10, 10))

        tk.Label(self.form_frame, text="Qual o local de partida?", bg="white").pack(anchor="w")
        self.entry_partida = tk.Entry(self.form_frame, font="Arial: 15")
        self.entry_partida.pack(anchor="w")

        tk.Label(self.form_frame, text="Qual o destino?", bg="white").pack(pady=5, anchor="w")
        self.entry_destino = tk.Entry(self.form_frame, font="Arial: 15")
        self.entry_destino.pack(pady=5, anchor="w")

        tk.Label(self.form_frame, text="Qual a porcentagem de bateria?", bg="white").pack(pady=5, anchor="w")
        opcoes = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
        self.entry_bateria = ttk.Combobox(self.form_frame, values=opcoes, state="readonly")
        self.entry_bateria.set("Selecione a porcentagem")
        self.entry_bateria.pack(pady=20, anchor="w")

        tk.Button(self.form_frame, text="Gerar Plano", command=self.gerarPlano, bg="#333", fg="White").pack(pady=20, anchor="w")

        # Chama o método para carregar a imagem logo na criação (ou pode deixar vazio até clicar no botão)
        

    def gerarPlano(self):
        img = tk.PhotoImage(file="enersync/imgs/plano.png")  # Ou use seu arquivo: /mnt/data/eb5aa8d0-edce-4295-bdc4-75ba63f772dc.png
        self.img = img  # manter referência
        for widget in self.img_frame.winfo_children():
            widget.destroy()  # remove imagens anteriores se já tiver

        label = tk.Label(self.img_frame, image=self.img, bg="white")
        label.pack()



    



    