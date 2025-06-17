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

        

        tk.Button(root, text="< Voltar", command=self.voltar, font="Arial: 20", bg="#333", fg="White").pack(pady=20,padx="20", anchor="w")

        self.card = tk.Frame(root, bg="#e4e4e4", bd=2, relief="raised", padx=10, pady=10)
        self.card.pack(padx=20, pady=20, fill="both", expand=True)

        # Container horizontal: esquerda = formulário | direita = imagem
        self.container = tk.Frame(self.card, bg="#f2f2f2")
        self.container.pack(fill="both", expand=True)

        # Frame para os campos de entrada (lado esquerdo)
        self.form_frame = tk.Frame(self.container, bg="white")
        self.form_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)


        self.label_nome = tk.Label(self.form_frame, text="Nome:", bg="white",font="Arial: 30")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(self.form_frame, bg="#f2f2f2", font="Arial: 30")
        self.entry_nome.pack()

        self.label_email = tk.Label(self.form_frame, bg="white", text="Email:", font="Arial: 30")
        self.label_email.pack()
        self.entry_email = tk.Entry(self.form_frame, bg="#f2f2f2",  font="Arial: 30")
        self.entry_email.pack()

        self.label_senha = tk.Label(self.form_frame, bg="white", text="Senha:", font="Arial: 30")
        self.label_senha.pack()
        self.entry_senha = tk.Entry(self.form_frame, bg="#f2f2f2",  show="*", font="Arial: 30")
        self.entry_senha.pack()

        # self.label_cpf = tk.Label(self.form_frame, text="CPF:", font="Arial: 30")
        # self.label_cpf.pack()
        # self.entry_cpf = tk.Entry(self.form_frame, bg="#f2f2f2", font="Arial: 30")
        # self.entry_cpf.pack()

        self.label_dt_nasc = tk.Label(self.form_frame, bg="white", text="Data de Nascimento (YYYY-MM-DD):", font="Arial: 30")
        self.label_dt_nasc.pack()
        self.entry_dt_nasc = tk.Entry(self.form_frame, bg="#f2f2f2", font="Arial: 30")
        self.entry_dt_nasc.pack()

        # self.label_id = tk.Label(root, text="ID (Para atualizar/deletar):", font="Arial: 30")
        # self.label_id.pack()
        # self.entry_id = tk.Entry(root, font="Aria bg="#f2f2f2",l: 30")
        # self.entry_id.pack()

        tk.Button(self.form_frame, text="Atualizar", command=self.atualizar, font="Arial: 30", bg="#333", fg="white").pack(side="left", padx=30)


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

   