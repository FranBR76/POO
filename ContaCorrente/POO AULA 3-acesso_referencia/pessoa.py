class Pessoa:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def exibeNome(self):
        print("Nome: {}".format(self.nome))

    def exibeIdade(self):
        print("Idade: {}".format(self.idade))

    def exibeSalario(self):
        print("Salario: {}".format(self.salario))
