
import tkinter as tk
from tkinter import messagebox
from usuario import Usuario
from usuarioDAO import UsuarioDAO

from veiculo import Veiculo
from veiculoDAO import VeiculoDAO

from PIL import Image, ImageTk


class App:
    def __init__(self, root):
        self.dao = UsuarioDAO()
        self.root = root
        self.root.title("CRUD Usuario com MySQL")
        self.root.geometry("1280x720")

        #* CAMPOS
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

        # self.label_permissoes = tk.Label(root, text="Permissões:")
        # self.label_permissoes.pack()
        # self.entry_permissoes = tk.Entry(root)
        # self.entry_permissoes.pack()

        self.label_cpf = tk.Label(root, text="CPF:", font="Arial: 20")
        self.label_cpf.pack()
        self.entry_cpf = tk.Entry(root, font="Arial: 20")
        self.entry_cpf.pack()

        self.label_dt_nasc = tk.Label(root, text="Data de Nascimento (YYYY-MM-DD):", font="Arial: 18")
        self.label_dt_nasc.pack()
        self.entry_dt_nasc = tk.Entry(root, font="Arial: 20")
        self.entry_dt_nasc.pack()

        self.label_id = tk.Label(root, text="ID (Para atualizar/deletar):", font="Arial: 20")
        self.label_id.pack()
        self.entry_id = tk.Entry(root, font="Arial: 20")
        self.entry_id.pack()

        #? BOTOES
        tk.Button(root, text="Criar", command=self.criar, font="Arial: 20", bg="#333", fg="white").pack(side="left", padx=30)
        tk.Button(root, text="Listar", command=self.listar, font="Arial: 20", bg="#333", fg="white").pack(side="right", padx=30)
        tk.Button(root, text="Atualizar", command=self.atualizar, font="Arial: 20", bg="#333", fg="white").pack(side="left", padx=30)
        tk.Button(root, text="Deletar", command=self.deletar, font="Arial: 20", bg="#333", fg="white", ).pack(side="right", padx=30)

        tk.Button(root, text="Cadastro Veiculo", command=self.cadastrar_veiculo, font="Arial: 20", bg="#333", fg="white", ).pack(side="bottom", padx=30)
        self.text_resultado = tk.Text(root, height=10, font="Arial: 20", bg="#ccc")
        self.text_resultado.pack(side="bottom", padx=20, pady=20)

    def criar(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        senha = self.entry_senha.get()
        # permissoes = self.entry_permissoes.get()
        cpf = self.entry_cpf.get()
        dt_nasc = self.entry_dt_nasc.get()

        if nome and email:
            usuario = Usuario(
                nome=nome,
                email=email,
                senha=senha,
                # permissoes=permissoes,
                cpf=cpf,
                dt_nasc=dt_nasc
            )
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
        if __name__ == "__main__":
            self.root.destroy()
            root = tk.Tk()
            app = VeiculoApp(root)
            root.mainloop()


       



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

        tk.Button(root, text="Entrar", command=self.verificar_login , font="Arial: 40", bg="#228B22", fg="white").pack(pady=10)


        tk.Button(root, text="Registrar-se", command=self.criar_conta , font="Arial: 10", bg="#228B22", fg="white").pack(pady=10)

    def verificar_login(self):
        email = self.entry_email.get()
        senha = self.entry_senha.get()

        resultado = self.dao.verificar_usuario(email, senha)

        if resultado:
            messagebox.showinfo("Login", "Login bem-sucedido!")
            self.root.destroy()  # Fecha janela de  login
        # Aqui você pode abrir o menu principal ou outra tela
            
            root = tk.Tk()
            app = App(root)
            root.mainloop()

        # Aqui você pode abrir outra janela ou continuar o programa
        else:
            messagebox.showerror("Erro", "E-mail ou senha incorretos.")

    
    def criar_conta(self):
        self.root.destroy()              
        root = tk.Tk()
        app = Registrar(root)
        root.mainloop()
    
    def limpar_campos(self):
        self.entry_marca.delete(0, tk.END)
        self.entry_modelo.delete(0, tk.END)


class Registrar:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.dao = UsuarioDAO()
        self.root.geometry("720x560")

        #* CAMPOS
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

        
        #? BOTOES
        tk.Button(root, text="Criar", command=self.criar, font="Arial: 20", bg="#228B22", fg="white").pack(side="left", padx=30)
        tk.Button(root, text="Já tenho conta", command=self.logar , font="Arial: 10", bg="#228B22", fg="white").pack(side="right", pady=10)

    def criar(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        senha = self.entry_senha.get()
        # permissoes = self.entry_permissoes.get()
        cpf = self.entry_cpf.get()
        dt_nasc = self.entry_dt_nasc.get()

        if nome and email:
            usuario = Usuario(
                nome=nome,
                email=email,
                senha=senha,
                # permissoes=permissoes,
                cpf=cpf,
                dt_nasc=dt_nasc
            )
            self.dao.criar(usuario)
            messagebox.showinfo("SUCESSO", "Usuário criado!")
            self.limpar_campos()
            
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos corretamente!")
    def limpar_campos(self):
        self.entry_marca.delete(0, tk.END)
        self.entry_modelo.delete(0, tk.END)

    
    def logar(self):
        self.root.destroy()              
        root = tk.Tk()
        app = Login(root)
        root.mainloop()
        

class VeiculoApp:
    def __init__(self, root):
        self.dao = VeiculoDAO()
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
        id_usu = self.usuario.id.get()
        marca = self.entry_marca.get()
        modelo = self.entry_modelo.get()

        if marca and modelo:
            veiculo = Veiculo(id=id_usu, marca=marca, modelo=modelo)
            self.dao.cadastrar(veiculo)
            messagebox.showinfo("SUCESSO", "Veiculo cadastrado")
            self.limpar_campos()
        
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos")
    
    def listarautos(self):
        usuarios = self.dao.listarautos()
        self.text_resultado.delete(1.0, tk.END)
        for r in usuarios:
            self.text_resultado.insert(tk.END, f"ID-Usu: {r[0]} | Marca: {r[1]} | Modelo: {r[2]}\n\n")
            self.limpar_campos()

    def limpar_campos(self):
        self.entry_marca.delete(0, tk.END)
        self.entry_modelo.delete(0, tk.END)



if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()

       
