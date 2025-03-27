# from historicobiblioteca import HistoricoBiblioteca

# class Aluno:
#     def __init__(self, nome, ra, dt_nasc, cpf, email):
#         self.nome = nome
#         self.ra = ra
#         self.dt_nasc = dt_nasc
#         self.cpf = cpf
#         self.email = email
#         self.historicobiblioteca = HistoricoBiblioteca()
        
    
#     def emprestimo(self, obra):
               
#         print("Emprestimo realizado da obra {} realizada com sucesso!".format(obra))
#         self.historicobiblioteca.emprestimos.append("Obra {} - emprestada por {}".format(obra, self.nome))
#         return True
    
#     def devolver(self, obra):
#         print("Devolução realizada da obra {} realizada com sucesso!".format(obra))
#         self.historicobiblioteca.emprestimos.append("Obra {} - devolvida por {}".format(obra, self.nome))
#         return True


from historicobiblioteca import HistoricoBiblioteca

class Aluno:
    def __init__(self, nome, ra, dt_nasc, cpf, email):
        self.nome = nome
        self.ra = ra
        self.dt_nasc = dt_nasc
        self.cpf = cpf
        self.email = email
        self.historico = HistoricoBiblioteca()
        self.livros_emprestados = []

    def emprestar(self, obra):
        if obra.disponivel:
            obra.disponivel = False 
            self.livros_emprestados.append(obra)
            self.historico.registrar_evento(f"Emprestou a obra '{obra.titulo}'")
            print(f"Emprestimo realizado com sucesso: {obra.titulo}")
        else:
            print(f"Erro: A obra '{obra.titulo}' ja esta emprestada.")

    def devolver(self, obra):
        if obra in self.livros_emprestados:
            obra.disponivel = True  
            self.livros_emprestados.remove(obra)
            self.historico.registrar_evento(f"Devolveu a obra '{obra.titulo}'")
            print(f"Devolucao realizada com sucesso: {obra.titulo}")
        else:
            print(f"Erro: A obra '{obra.titulo}' nao esta registrada como emprestada por {self.nome}.")
