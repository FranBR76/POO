# from funcionarioBiblio import Funcionario
from bibliotecario import Bibliotecario
# import cadastroObras
from aluno import Aluno
from obras import Obras
from cadastroObras import *




bibliotecario = Bibliotecario('Cesco', 
                              '123456789',
                              'bibliotecario',
                              4000.00,
                              'senha123')



# def __init__(self, nome, ra, dt_nasc, cpf, email):
a1 = Aluno('Cesco', '123', '18/11/2005', '7878', 'francesco@gmail.com')

# a1.emprestar(Livro_top)
# a1.devolver(Livro_top)
# a1.historico.imprime()




# bibliotecario.autentica('senha123')
# bibliotecario.cadastrar_livro('Livro top', 'Autor top', '2023')
# bibliotecario.cadastrar_livro('Pedro Games', 'Autor toe2ep', '2023')
# bibliotecario.cadastrar_livro('MiniMEUS', 'Autor to2e2p', '2023')

bibliotecario.historico.imprime()