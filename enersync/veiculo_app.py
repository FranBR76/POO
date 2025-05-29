import tkinter as tk
from tkinter import messagebox
from veiculo import Veiculo
from veiculoDAO import VeiculoDAO

class VeiculoApp:
    def __init__(self, root, id_usuario):
        self.dao = VeiculoDAO()
        self.id_usuario = id_usuario
        self.root = root
        self.root.title("Cadastrar Veiculo")
        self.root.geometry("1280x720")

        self.label_marca = tk.Label(root, text="Marca", font="Arial: 20")
        self.label_marca.pack()
        self.entry_marca = tk.Entry(root, font="Arial: 20")
        self.entry_marca.pack()

        self.label_modelo = tk.Label(root, text="Modelo", font="Arial: 20")
        self.label_modelo.pack()
        self.entry_modelo = tk.Entry(root, font="Arial: 20")
        self.entry_modelo.pack()

        tk.Button(root, text="Cadastrar", command=self.cadastrar, font="Arial: 20", bg="#333", fg="white").pack(side="left", padx=30)
        tk.Button(root, text="Listar", command=self.listarautos, font="Arial: 20", bg="#333", fg="white").pack(side="left", padx=30)

        self.text_resultado = tk.Text(root, height=10, font="Arial: 20", bg="#ccc")
        self.text_resultado.pack(side="bottom", padx=20, pady=20)

    def cadastrar(self):
        marca = self.entry_marca.get()
        modelo = self.entry_modelo.get()
        id_usu = self.id_usuario
       
        if marca and modelo:
            veiculo = Veiculo(id_usuario=id_usu, marca=marca, modelo=modelo)
            self.dao.cadastrar(veiculo)
            messagebox.showinfo("SUCESSO", "Veiculo cadastrado")
            self.limpar_campos()
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos")

    def listarautos(self):
        usuarios = self.dao.listarautos()
        self.text_resultado.delete(1.0, tk.END)
        for r in usuarios:
            self.text_resultado.insert(tk.END, f"ID-Usu: {r[1]} | Marca: {r[2]} | Modelo: {r[3]}\n\n")
        self.limpar_campos()

    def limpar_campos(self):
        self.entry_marca.delete(0, tk.END)
        self.entry_modelo.delete(0, tk.END)
