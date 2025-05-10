import tkinter as tk
from tkinter import messagebox
from usuario import Usuario
from usuarioDAO import UsuarioDAO


class App:
    def __init__(self, root):
        self.dao = UsuarioDAO()
        self.root = root
        self.root.title("CRUD Usuario com MySQL")
        self.root.geometry("400x400")

        #* CAMPOS
        tk.label_nome = tk.Label(root, text="Nome: ")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(root)
        self.entry_nome.pack()
        

        tk.label_email = tk.Label(root, text="Email: ")
        self.label_email.pack()
        self.entry_email = tk.Entry(root)
        self.entry_email.pack()
        
        
        tk.label_id = tk.Label(root, text="ID: (Para atualizar/deletar)")
        self.label_id.pack()
        self.entry_id = tk.Entry(root)
        self.entry_id.pack()

        #?  BOTOES
        tk.Button(root, text="Criar", command=self.criar).pack(pady=5)
        tk.Button(root, text="Listar", command=self.listar).pack(pady=5)
        tk.Button(root, text="Atualizar", command=self.atualizar).pack(pady=5)
        tk.Button(root, text="Deletar", command=self.deletar).pack(pady=5)

        self.text_resultado = tk.Text(root, height=10)
        self.text_resultado.pack()

        def criar():
            nome = self.entry_nome.get()
            email = self.entry_email.get()
            if nome and email:
                usuario = Usuario(nome=nome, email=email)
                self.dao.criar(usuario)
                messagebox.showinfo("SUCESSO", "Usuário criado!")
                self.limpar_campos()
            else:
                messagebox.showwarning("Erro", "Preencha todos os campos!")

