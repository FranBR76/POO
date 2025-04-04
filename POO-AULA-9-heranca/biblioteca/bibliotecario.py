from funcionarioBiblio import Funcionario
class Bibliotecario(Funcionario):
    def __init__(self, nome, cpf, cargo, salario, senha):
        super().__init__(nome, cpf, cargo, salario)
        self._senha = senha
        self.autenticado = False

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
            arquivo.write(f"\n{objetoLivro} = Obras('{livro}', '{autor}', {ano}) \n{objetoLivro}.disponivel = True " '\n')
            arquivo.close()
            print(f'Livro - {livro} cadastrado com sucesso!')


        else:
            print('Não foi possível cadastrar o livro! - Usuario não autenticado!')
