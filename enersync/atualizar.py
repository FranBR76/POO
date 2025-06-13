import tkinter as tk
from tkinter import messagebox
from veiculo import Veiculo
from veiculoDAO import VeiculoDAO
from usuario import Usuario
from usuarioDAO import UsuarioDAO
from app import App

from metodos import Voltar
class AtualizarDados(Voltar):
    def __init__(self, root, id_usuario):
        self.dao = UsuarioDAO()
        self.id_usuario = id_usuario
        self.root = root
        self.root.title("Atualizar dados")
        self.root.geometry("1280x720")
        self.root.configure(bg="lightblue")

        tk.Button(root, text="< Voltar", command=self.voltar, bg="#333", fg="White").pack(pady=20, anchor="w")

        self.label_nome = tk.Label(root, text="Nome:", font="Arial: 15")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(root, font="Arial: 15")
        self.entry_nome.pack()

        self.label_email = tk.Label(root, text="Email:", font="Arial: 15")
        self.label_email.pack()
        self.entry_email = tk.Entry(root, font="Arial: 15")
        self.entry_email.pack()

        self.label_senha = tk.Label(root, text="Senha:", font="Arial: 15")
        self.label_senha.pack()
        self.entry_senha = tk.Entry(root, show="*", font="Arial: 15")
        self.entry_senha.pack()

        # self.label_cpf = tk.Label(root, text="CPF:", font="Arial: 15")
        # self.label_cpf.pack()
        # self.entry_cpf = tk.Entry(root, font="Arial: 15")
        # self.entry_cpf.pack()

        self.label_dt_nasc = tk.Label(root, text="Data de Nascimento (YYYY-MM-DD):", font="Arial: 18")
        self.label_dt_nasc.pack()
        self.entry_dt_nasc = tk.Entry(root, font="Arial: 15")
        self.entry_dt_nasc.pack()

        # self.label_id = tk.Label(root, text="ID (Para atualizar/deletar):", font="Arial: 15")
        # self.label_id.pack()
        # self.entry_id = tk.Entry(root, font="Arial: 15")
        # self.entry_id.pack()

        tk.Button(root, text="Atualizar", command=self.atualizar, font="Arial: 15", bg="#333", fg="white").pack(side="left", padx=30)


    def atualizar(self):
        
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        senha = self.entry_senha.get()
        dt_nasc = self.entry_dt_nasc.get()
        id_usu = self.id_usuario
        if id and nome and email:
            usuario = Usuario(id=id_usu, nome=nome, email=email, senha=senha, dt_nasc=dt_nasc)
            self.dao.atualizar(usuario)
            messagebox.showinfo("Atualizado", "Usuario atualizado com sucesso \n\n Retornando a tela anterior")
            self.root.destroy()
            root = tk.Tk()
            app = App(root, self.id_usuario)
            root.mainloop()
        else:
            messagebox.showwarning("Erro", "Preencha os campos corretamente!")

   