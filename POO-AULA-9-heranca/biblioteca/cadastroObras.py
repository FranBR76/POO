from obras import Obras

class ObrasCadastraa(Obras):
    def __init__(self, titulo, autor, ano):
        super().__init__(titulo, autor, ano)
        self.disponivel = True
# 
# 
def Obrass():
    # Criação de objetos da classe Obras
    
    Livro_top = Obras('Livro top', 'Autor top', 2023) 
    Livro_top.disponivel = True 
    PEDRO_GAMES = Obras('PEDRO GAMES', 'Autor toe2ep', 2023) 
    PEDRO_GAMES.disponivel = True 
    MINIMEUS = Obras('MINIMEUS', 'Autor to2e2p', 2023) 
    MINIMEUS.disponivel = True 
