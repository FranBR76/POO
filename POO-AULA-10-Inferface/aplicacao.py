import tkinter as tk
from tkinter import messagebox
from conta import Conta

class Aplicacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Conta Corrente")

        self.contas = {}

        tk.Label(root, text="Titular:").grid(row=0, column=0)
        self.entry_titular = tk.Entry(root)
        self.entry_titular.grid(row=0, column=1)

        tk.Label(root, text="Numero:").grid(row=1, column=0)
        self.entry_numero = tk.Entry(root)
        self.entry_numero.grid(row=1, column=1)


        tk.Label(root, text="Saldo inicial:").grid(row=2, column=0)
        self.entry_saldo = tk.Entry(root)
        self.entry_saldo.grid(row=2, column=1)

        tk.Button(root, text="Criar Conta", command=self.criar_conta).grid(row=3, column=0, columnspan=2)

        tk.Label(root, text="Numero da Conta para transação:").grid(row=4, column=0)
        self.entry_num_transacao = tk.Entry(root)
        self.entry_num_transacao.grid(row=4, column=1)

        tk.Label(root, text="Valor:").grid(row=5, column=0)
        self.entry_valor = tk.Entry(root)
        self.entry_valor.grid(row=5, column=1)

        tk.Button(root, text="Depositar", command=self.depositar).grid(row=6, column=0)
        tk.Button(root, text="Sacar", command=self.sacar).grid(row=6, column=1)
        tk.Button(root, text="Ver detalhes", command=self.ver_detalhes).grid(row=7, column=0, columnspan=2)

    def criar_conta(self):
        titular = self.entry_titular.get()
        numero = self.entry_numero.get()
        saldo = float(self.entry_saldo.get() or 0)

        if numero in self.contas:
            messagebox.showerror("Erro", "Número da conta já existe")
            return
        
        self.contas[numero] = Conta(titular, numero, saldo)
        messagebox.showinfo("Sucesso", "Conta criada com sucesso")


    def depositar(self):
        numero = self.entry_num_transacao.get()
        valor = float(self.entry_valor.get() or 0)

        if numero in self.contas:
            if self.contas[numero].depositar(valor):
                messagebox.showinfo("Sucesso", f"Deposito de R$ {valor:.2f} realizado!")
            else:
                messagebox.showerror("Erro", "Valor inválido para depósito!")
        
        else:
            messagebox.showerror("Erro", "Conta não encontrada")

    def sacar(self):
        numero = self.entry_num_transacao.get()
        valor = float(self.entry_valor.get() or 0)

        if numero in self.contas:
            if self.contas[numero].sacar(valor):
                messagebox.showinfo("Sucesso", f"Saque de R$ {valor:.2f} realizado!")
            else:
                messagebox.showerror("Erro", "Saldo insuficiente ou valor inválido")
        else:
            messagebox.showerror("Erro", "Conta não encontrada")

    def ver_detalhes(self):
        numero = self.entry_num_transacao.get()
        
        if numero in self.contas:
            detalhes = self.contas[numero].detalhes()
            messagebox.showinfo("Detalhes da Conta", detalhes)
        else:
            messagebox.showerror("Erro", "Conta não encontrada")


# Inicializacao da aplicacao
if __name__ == "__main__":
    root = tk.Tk() 
    app = Aplicacao(root)
    root.mainloop()