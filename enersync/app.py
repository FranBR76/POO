
import tkinter as tk
from tkinter import messagebox
from usuario import Usuario
from usuarioDAO import UsuarioDAO

class App:
    def __init__(self, root):
        self.dao = UsuarioDAO()
        self.root = root
        self.root.title("CRUD Usuario com MySQL")
        self.root.geometry("700x600")

        #* CAMPOS
        self.label_nome = tk.Label(root, text="Nome:")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(root)
        self.entry_nome.pack()

        self.label_email = tk.Label(root, text="Email:")
        self.label_email.pack()
        self.entry_email = tk.Entry(root)
        self.entry_email.pack()

        self.label_senha = tk.Label(root, text="Senha:")
        self.label_senha.pack()
        self.entry_senha = tk.Entry(root, show="*")
        self.entry_senha.pack()

        self.label_permissoes = tk.Label(root, text="Permissões:")
        self.label_permissoes.pack()
        self.entry_permissoes = tk.Entry(root)
        self.entry_permissoes.pack()

        self.label_cpf = tk.Label(root, text="CPF:")
        self.label_cpf.pack()
        self.entry_cpf = tk.Entry(root)
        self.entry_cpf.pack()

        self.label_dt_nasc = tk.Label(root, text="Data de Nascimento (YYYY-MM-DD):")
        self.label_dt_nasc.pack()
        self.entry_dt_nasc = tk.Entry(root)
        self.entry_dt_nasc.pack()

        self.label_id = tk.Label(root, text="ID (Para atualizar/deletar):")
        self.label_id.pack()
        self.entry_id = tk.Entry(root)
        self.entry_id.pack()

        #? BOTOES
        tk.Button(root, text="Criar", command=self.criar).pack(pady=5)
        tk.Button(root, text="Listar", command=self.listar).pack(pady=5)
        tk.Button(root, text="Atualizar", command=self.atualizar).pack(pady=5)
        tk.Button(root, text="Deletar", command=self.deletar).pack(pady=5)

        self.text_resultado = tk.Text(root, height=10)
        self.text_resultado.pack()

    def criar(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        senha = self.entry_senha.get()
        permissoes = self.entry_permissoes.get()
        cpf = self.entry_cpf.get()
        dt_nasc = self.entry_dt_nasc.get()

        if nome and email:
            usuario = Usuario(
                nome=nome,
                email=email,
                senha=senha,
                permissoes=permissoes,
                cpf=cpf,
                dt_nasc=dt_nasc
            )
            self.dao.criar(usuario)
            messagebox.showinfo("SUCESSO", "Usuário criado!")
            
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos corretamente!")

    def listar(self):
        usuarios = self.dao.listar()
        self.text_resultado.delete(1.0, tk.END)
        for u in usuarios:
            self.text_resultado.insert(tk.END, str(u) + "\n")

    def atualizar(self):
        try:
            id_usuario = int(self.entry_id.get())
        except ValueError:
            messagebox.showwarning("Erro", "ID inválido.")
            return

        usuario = Usuario(
            id=id_usuario,
            nome=self.entry_nome.get(),
            email=self.entry_email.get(),
            senha=self.entry_senha.get(),
            permissoes=self.entry_permissoes.get(),
            cpf=self.entry_cpf.get(),
            dt_nasc=self.entry_dt_nasc.get()
        )
        self.dao.atualizar(usuario)
        messagebox.showinfo("SUCESSO", "Usuário atualizado!")
      

    def deletar(self):
        try:
            id_usuario = int(self.entry_id.get())
        except ValueError:
            messagebox.showwarning("Erro", "ID inválido.")
            return

        self.dao.deletar(id_usuario)
        messagebox.showinfo("SUCESSO", "Usuário deletado!")
       

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
