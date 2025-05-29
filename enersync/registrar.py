import tkinter as tk
from tkinter import messagebox
from usuario import Usuario
from usuarioDAO import UsuarioDAO

class Registrar:
    def __init__(self, root):
        self.root = root
        self.root.title("Registrar")
        self.dao = UsuarioDAO()
        self.root.geometry("1280x720")

        self.label_nome = tk.Label(root, text="Nome:", font="Arial: 20")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(root, font="Arial: 20")
        self.entry_nome.pack()

        self.label_email = tk.Label(root, text="Email:", font="Arial: 20")
        self.label_email.pack()
        self.entry_email = tk.Entry(root, font="Arial: 20")
        self.entry_email.pack()

        self.label_senha = tk.Label(root, text="Senha:", font="Arial: 20")
        self.label_senha.pack()
        self.entry_senha = tk.Entry(root, show="*", font="Arial: 20")
        self.entry_senha.pack()

        self.label_cpf = tk.Label(root, text="CPF:", font="Arial: 20")
        self.label_cpf.pack()
        self.entry_cpf = tk.Entry(root, font="Arial: 20")
        self.entry_cpf.pack()

        self.label_dt_nasc = tk.Label(root, text="Data de Nascimento (YYYY-MM-DD):", font="Arial: 18")
        self.label_dt_nasc.pack()
        self.entry_dt_nasc = tk.Entry(root, font="Arial: 20")
        self.entry_dt_nasc.pack()

        tk.Button(root, text="Criar", command=self.criar, font="Arial: 20", bg="#228B22", fg="white").pack(side="left", padx=30)
        tk.Button(root, text="Já tenho conta", command=self.logar , font="Arial: 10", bg="#228B22", fg="white").pack(side="right", pady=10)

    def criar(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        senha = self.entry_senha.get()
        cpf = self.entry_cpf.get()
        dt_nasc = self.entry_dt_nasc.get()

        if nome and email:
            usuario = Usuario(nome=nome, email=email, senha=senha, cpf=cpf, dt_nasc=dt_nasc)
            self.dao.criar(usuario)
            messagebox.showinfo("SUCESSO", "Usuário criado!")
            self.limpar_campos()
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos corretamente!")

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_senha.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_dt_nasc.delete(0, tk.END)

    def logar(self):
        self.root.destroy()
        from login import Login
        root = tk.Tk()
        app = Login(root)
        root.mainloop()
