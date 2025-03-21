
# from biblioteca import Biblioteca
# from emprestimo import Emprestimo
from obras import Obras
from aluno import Aluno



a1 = Aluno('Cesco', '123456', '18/11/2006', '12345678910', 'cesquinhogames@email.com')
a2 = Aluno('Teteu', '222222', '29/06/2006', '88888888888', 'mateuzinho@email.com')

obra1 = Obras('O Menino Maluquinho', 'Ziraldo', 2015, a1)
obra2 = Obras('Harry Potter', 'Mateus Ortlieb', 2017, a2)

a1.emprestimo("O Menino Maluquinho")
a1.devolver("O Menino Maluquinho")
obra1.historicobiblioteca.imprime()

# print('Obra: {} \nEmprestado por: {} \n'.format(obra1.titulo, obra1.aluno.nome))