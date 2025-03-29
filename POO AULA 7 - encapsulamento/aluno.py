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
        self._nome = nome
        self._ra = ra
        self._dt_nasc = dt_nasc
        self._cpf = cpf
        self._email = email
        self.historico = HistoricoBiblioteca()
        self._livros_emprestados = []


    # SET e GET
    def get_email(self):
        return self._email
    def set_email(self, email):
        self._email = email

    def get_nome(self):
        return self._nome
    def set_nome(self, nome):
        self._nome = nome

    
    def get_ra(self):
        return self._ra
    
    def set_ra(self, ra):
        self._ra = ra
    
    def get_dt_nasc(self):
        return self._dt_nasc
    
    def set_dt_nasc(self, dt_nasc):
        self._dt_nasc = dt_nasc
   
    def get_cpf(self):
        return self._cpf
    
    def set_cpf(self, cpf):
        self._cpf = cpf
    
    def get_livros_emprestados(self):
        return self._livros_emprestados
    
    def set_livros_emprestados(self, livros_emprestados):
        self._livros_emprestados = livros_emprestados




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
