from funcionarioBiblio import Funcionario
from historicoBibliotecario import HistoricoBibliotecario



import tkinter as tk
from tkinter import messagebox


class Bibliotecario(Funcionario):
    def __init__(self, nome, cpf, cargo, salario, senha):
        super().__init__(nome, cpf, cargo, salario)
        self._senha = senha
        self.autenticado = False
        self.historico = HistoricoBibliotecario()
        self._livros_cadastrados = []

    def autentica(self, senha):
        if self._senha == senha:
            print("Acesso permitido")
            self.autenticado = True
            return True
        else:
            print("Acesso negado")
            self.autenticado = False
            return False
    
    def cadastrar_livro(self, livro, autor, ano):
        # livro = Obras(titulo, autor, ano)
        if self.autenticado == True:
            objetoLivro = livro.replace(' ', '_')
            arquivo = open('C:/xampp/htdocs/py/POO/POO-AULA-9-heranca/biblioteca/cadastroObras.py', 'a')
            arquivo.write(f"\n{objetoLivro} = Obras('{livro}', '{autor}', '{ano}') \n{objetoLivro}.disponivel = True  "  '\n')
            arquivo.close()

            self._livros_cadastrados.append(livro)
            self.historico.registrar_evento(f"Livro '{livro}' cadastrado com sucesso!")

            print(f'Livro - {livro} cadastrado com sucesso!')



        else:
            print('Nao foi possivel cadastrar o livro! - Usuario nao autenticado!')
