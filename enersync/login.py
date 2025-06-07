import tkinter as tk
from tkinter import messagebox
from usuarioDAO import UsuarioDAO
from app import App

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.dao = UsuarioDAO()
        self.root.geometry("1280x720")
        self.root.configure(bg="lightblue")

        tk.Label(root, text="Email:", font="Arial: 40").pack(pady=5)
        self.entry_email = tk.Entry(root, font="Arial: 40")
        self.entry_email.pack(pady=5)

        tk.Label(root, text="Senha:", font="Arial: 40").pack(pady=5)
        self.entry_senha = tk.Entry(root, show="*", font="Arial: 40")
        self.entry_senha.pack(pady=5)

        tk.Button(root, text="Entrar", command=self.verificar_login, font="Arial: 40", bg="#228B22", fg="white").pack(pady=10)
        tk.Button(root, text="Registrar-se", command=self.criar_conta, font="Arial: 10", bg="#228B22", fg="white").pack(pady=10)

    def verificar_login(self):
        email = self.entry_email.get()
        senha = self.entry_senha.get()
        resultado = self.dao.verificar_usuario(email, senha)

        if resultado:
            id_usuario = resultado[0]
            messagebox.showinfo("Login", "Login bem-sucedido!")
            self.root.destroy()
            root = tk.Tk()
            app = App(root, id_usuario)
            root.mainloop()
        else:
            messagebox.showerror("Erro", "E-mail ou senha incorretos.")

    def criar_conta(self):
        self.root.destroy()
        from registrar import Registrar
        root = tk.Tk()
        app = Registrar(root)
        root.mainloop()
