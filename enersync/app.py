import tkinter as tk
from tkinter import messagebox
from usuario import Usuario
from usuarioDAO import UsuarioDAO
from veiculo_app import VeiculoApp


class App:
    def __init__(self, root, id_usuario):
        self.dao = UsuarioDAO()
        self.id_usuario = id_usuario
        self.root = root
        self.root.title("CRUD Usuario com MySQL")
        self.root.geometry("1280x720")
        self.root.configure(bg="lightblue")

        # self.label_nome = tk.Label(root, text="Nome:", font="Arial: 20")
        # self.label_nome.pack()
        # self.entry_nome = tk.Entry(root, font="Arial: 20")
        # self.entry_nome.pack()

        # self.label_email = tk.Label(root, text="Email:", font="Arial: 20")
        # self.label_email.pack()
        # self.entry_email = tk.Entry(root, font="Arial: 20")
        # self.entry_email.pack()

        # self.label_senha = tk.Label(root, text="Senha:", font="Arial: 20")
        # self.label_senha.pack()
        # self.entry_senha = tk.Entry(root, show="*", font="Arial: 20")
        # self.entry_senha.pack()

        # self.label_cpf = tk.Label(root, text="CPF:", font="Arial: 20")
        # self.label_cpf.pack()
        # self.entry_cpf = tk.Entry(root, font="Arial: 20")
        # self.entry_cpf.pack()

        # self.label_dt_nasc = tk.Label(root, text="Data de Nascimento (YYYY-MM-DD):", font="Arial: 18")
        # self.label_dt_nasc.pack()
        # self.entry_dt_nasc = tk.Entry(root, font="Arial: 20")
        # self.entry_dt_nasc.pack()

        # self.label_id = tk.Label(root, text="ID (Para atualizar/deletar):", font="Arial: 20")
        # self.label_id.pack()
        # self.entry_id = tk.Entry(root, font="Arial: 20")
        # self.entry_id.pack()

        # tk.Button(root, text="Criar", command=self.criar, font="Arial: 20", bg="#333", fg="white").pack(side="left", padx=30)
        # tk.Button(root, text="Listar", command=self.listar, font="Arial: 20", bg="#333", fg="white").pack(side="right", padx=30)
        for col in range(5): 
            root.grid_columnconfigure(col, weight=1)

        tk.Label(root, text="Bem-vindo de volta!", font="Arial: 28", bg="lightblue").grid(row=0, column=2, pady=5, sticky="ew")
        tk.Label(root, text="", font="Arial: 28", bg="lightblue").grid(row=1, column=0, pady=5, sticky="ew")

        #*
        tk.Button(root, text="Atualizar dados", command=self.atualizardado, font="Arial: 20", bg="#333", fg="white").grid(row=2, column=1, pady=5, sticky="ew")
        #!
        tk.Button(root, text="Planejar viagem", command=self.planejar, font="Arial: 20", bg="#333", fg="white").grid(row=2, column=2, sticky="ew", pady=5)
        #!
        tk.Button(root, text="Noticias", command=self.atualizar, font="Arial: 20", bg="#333", fg="white").grid(row=2, column=3, sticky="ew", pady=5)
        #!
        tk.Button(root, text="Comprar peças", command=self.atualizar, font="Arial: 20", bg="#333", fg="white").grid(row=3, column=3, sticky="ew", pady=5)
        #*
        tk.Button(root, text="Cadastro Veiculo", command=self.cadastrar_veiculo, font="Arial: 20", bg="#333", fg="white").grid(row=3, column=1, sticky="ew", pady=5)

        # tk.Button(root, text="Deletar conta", command=self.deletar, font="Arial: 8", bg="#333", fg="white").pack(side="bottom", padx=30)
        # self.text_resultado = tk.Text(root, height=10, font="Arial: 20", bg="#ccc")
        # self.text_resultado.pack(side="bottom", padx=20, pady=20)

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

    def listar(self):
        usuarios = self.dao.listar()
        self.text_resultado.delete(1.0, tk.END)
        for r in usuarios:
            self.text_resultado.insert(tk.END, f"ID: {r[0]} | Nome: {r[1]} | Email: {r[2]}\n\n")
        self.limpar_campos()

    def atualizar(self):
        id = self.entry_id.get()
        nome = self.entry_nome.get()
        email = self.entry_email.get()

        if id and nome and email:
            usuario = Usuario(id=int(id), nome=nome, email=email)
            self.dao.atualizar(usuario)
            messagebox.showinfo("Atualizado", "Usuario atualizado com sucesso")
            self.limpar_campos()
        else:
            messagebox.showwarning("Erro", "Preencha os campos corretamente!")

    def deletar(self):
        id = self.entry_id.get()
        if id:
            self.dao.deletar(int(id))
            messagebox.showinfo("Deletado", "Usuario deletado com sucesso!")
            self.limpar_campos()
        else:
            messagebox.showwarning("Erro", "Informe o ID corretamente")

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_senha.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_dt_nasc.delete(0, tk.END)

    def cadastrar_veiculo(self):
        self.root.destroy()
        root = tk.Tk()
        app = VeiculoApp(root, self.id_usuario)
        root.mainloop()

    def atualizardado(self):
        from atualizar import AtualizarDados
        self.root.destroy()
        root = tk.Tk()
        app = AtualizarDados(root, self.id_usuario)
        root.mainloop()

    def planejar(self):
        from planoViagem import PlanoViagem 
        self.root.destroy()
        root = tk.Tk()
        app = PlanoViagem(root, self.id_usuario)
        root.mainloop()

  