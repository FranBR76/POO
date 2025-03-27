
# from biblioteca import Biblioteca
# from emprestimo import Emprestimo
# from obras import Obras
# from aluno import Aluno



# a1 = Aluno('Cesco', '123456', '18/11/2006', '12345678910', 'cesquinhogames@email.com')
# a2 = Aluno('Teteu', '222222', '29/06/2006', '88888888888', 'mateuzinho@email.com')

# obra1 = Obras('O Menino Maluquinho', 'Ziraldo', 2015)
# obra2 = Obras('Harry Potter', 'Mateus Ortlieb', 2017)

# a1.emprestimo(obra1)
# a1.devolver(obra1)
# obra1.historicobiblioteca.imprime()


# print('Obra: {} \nEmprestado por: {} \n'.format(obra1.titulo, obra1.aluno.nome))




from obras import Obras
from aluno import Aluno



a1 = Aluno('Cesco', '123456', '18/11/2006', '12345678910', 'cesquinhogames@email.com')
a2 = Aluno('Teteu', '222222', '29/06/2006', '88888888888', 'mateuzinho@email.com')



obra1 = Obras('O Menino Maluquinho', 'Ziraldo', 2015)
obra2 = Obras('Harry Potter', 'J.K. Rowling', 2017)


a1.emprestar(obra1)  
a1.devolver(obra1)   
a2.emprestar(obra2) 
a2.devolver(obra2)   



print(a1.nome)
a1.historico.imprime()
print(a2.nome)
a2.historico.imprime()

a1.emprestar(obra2)
a1.emprestar(obra1)

print(a1.nome)
a1.historico.imprime()