from conta import Conta
from cliente import Cliente

c1 = Cliente('Rodrigo', 'Viecheneski', '04547726877')
c2 = Cliente('Pedro', 'Godinho', '77777777777')
m1 = Conta('123-4', c1, 120.0, 1000.0)
m2 = Conta('222-2', c2, 200.00, 1000.00)
# print(m2.titular.nome)
# print(m1.titular.sobrenome)
# print(m2.titular.cpf)

# print(m2.__dict__)  
# print(m2.titular.__dict__)

# from biblioteca import Biblioteca
# from emprestimo import Emprestimo
from obras import Obras
from aluno import Aluno



a1 = Aluno('Cesco', '123456', '18/11/2006', '12345678910', 'cesquinhogames@email.com')
a2 = Aluno('Teteu', '222222', '29/06/2006', '88888888888', 'mateuzinho@email.com')

obra1 = Obras('O Menino Maluquinho', 'Ziraldo', 2015, a1)
obra2 = Obras('Harry Potter', 'Mateus Ortlieb', 2017, a2)

print('Obra: {} \nEmprestado por: {} \n'.format(obra1.titulo, obra1.aluno.nome))





# print(c2.saldo)
# # c1.depositar(100.0)
# print(c1.saldo)
# c2.depositar(300.0)
# print(c2.saldo)
# c2.transferencia(c1,30) #por algum motivo não está funcionando com valores altos
# print(c1.saldo)
# print(c2.saldo)


# print(c2.saldo)
# c2.depositar(0.50)
# print(c2.saldo)

# print(c1.saldo)
# c1.depositar(10000.0)
# print(c1.saldo)

# if(c1 == c3):
#     print("Contas são iguais")
# else:
#     print("Contas são diferentes")


# from pessoa import Pessoa

# p1 = Pessoa('Jean Vargas', 45, 1000.0)
# p2 = Pessoa('Cesco Matteo', 19, 905.10)
# p3 = Pessoa('Mateus Ortileb', 18, 900.0)
# p4 = Pessoa('Pedro Dias', 21, 1000.0)

# p1.exibeNome()
# p1.exibeIdade()
# p1.exibeSalario()

# p2.exibeNome()
# p2.exibeIdade()
# p2.exibeSalario()

# p3.exibeNome()
# p3.exibeIdade()
# p3.exibeSalario()   

# p4.exibeNome()
# p4.exibeIdade()
# p4.exibeSalario()