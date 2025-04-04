from obras import Obras
from aluno import Aluno



a1 = Aluno('Cesco', '123456', '18/11/2006', '12345678910', 'cesquinhogames@email.com')
a2 = Aluno('Teteu', '222222', '29/06/2006', '88888888888', 'mateuzinho@email.com')



obra1 = Obras('O Menino Maluquinho', 'Ziraldo', 2015)
obra2 = Obras('Harry Potter', 'J.K. Rowling', 2017)


print(a1.get_email())

a1.set_email('TESTE@EMAIL.COM')
print(a1.get_email())


a1.set_nome('Francesco')
a1.set_cpf('13013013020')
print(a1.get_nome())
print(a1.get_cpf())
print(a1.get_email())