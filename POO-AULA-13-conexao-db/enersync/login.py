
import tkinter as tk
from tkinter import messagebox
from usuario import Usuario
from usuarioDAO import UsuarioDAO
from appVeiculo import VeiculoApp
from appVeiculo import VeiculoApp


from app import App

class Login():
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.dao = UsuarioDAO()
        self.root.geometry("720x560")

        tk.Label(root, text="Email:", font="Arial: 40").pack(pady=5)
        self.entry_email = tk.Entry(root, font="Arial: 40")
        self.entry_email.pack(pady=5)

        tk.Label(root, text="Senha:", font="Arial: 40").pack(pady=5)
        self.entry_senha = tk.Entry(root, show="*", font="Arial: 40")
        self.entry_senha.pack(pady=5)

        tk.Button(root, text="Entrar", command=self.verificar_login , font="Arial: 40", bg="#333", fg="white").pack(pady=10)

    def verificar_login(self):
        email = self.entry_email.get()
        senha = self.entry_senha.get()

        resultado = self.dao.verificar_usuario(email, senha)

        if resultado:
            messagebox.showinfo("Login", "Login bem-sucedido!")
            self.root.destroy()  # Fecha janela de login
        # Aqui você pode abrir o menu principal ou outra tela
            
            root = tk.Tk()
            app = App(root)
            root.mainloop()

        # Aqui você pode abrir outra janela ou continuar o programa
        else:
            messagebox.showerror("Erro", "E-mail ou senha incorretos.")

    

       

if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()
