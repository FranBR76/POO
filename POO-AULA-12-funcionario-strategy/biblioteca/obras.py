from historicobiblioteca import HistoricoAluno

class Obras:
    def __init__(self, titulo, autor, ano):
        self._titulo = titulo
        self._autor = autor
        self._ano = ano
        # self.aluno = aluno
        self.historicobiblioteca = HistoricoAluno()
        self._disponivel = True
    
    def get_titulo(self):
        return self._titulo
    
    def set_titulo(self, titulo):
        self._titulo = titulo
    
    def get_autor(self):
        return self._autor
    
    def set_autor(self, autor):
        self._autor = autor
    
    def get_ano(self):
        return self._ano
    
    def set_ano(self, ano):
        self._ano = ano

    def get_disponivel(self):
        return self._disponivel
    
    def set_disponivel(self, disponivel):
        self._disponivel = disponivel