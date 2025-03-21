from historicobiblioteca import HistoricoBiblioteca

class Aluno:
    def __init__(self, nome, ra, dt_nasc, cpf, email):
        self.nome = nome
        self.ra = ra
        self.dt_nasc = dt_nasc
        self.cpf = cpf
        self.email = email
        self.historicobiblioteca = HistoricoBiblioteca()
        
    
    def emprestimo(self, obra):
               
        print("Emprestimo realizado da obra {} realizada com sucesso!".format(obra))
        self.historicobiblioteca.emprestimos.append("Obra {} - emprestada por {}".format(obra, self.nome))
        return True
    
    def devolver(self, obra):
        print("Devolução realizada da obra {} realizada com sucesso!".format(obra))
        self.historicobiblioteca.emprestimos.append("Obra {} - devolvida por {}".format(obra, self.nome))
        return True
    