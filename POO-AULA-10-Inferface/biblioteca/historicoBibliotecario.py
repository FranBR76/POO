import datetime


class HistoricoBibliotecario:

    def __init__(self):
        # self.data_abertura = datetime.datetime.today()
        self._cadastros = []
        

    def imprime(self):
        
        # print("Data de cadastro do livro: {} \n".format(self.data_abertura))
        print("Registros: ")
        for e in self._cadastros:
            print("- ", e)

    def registrar_evento(self, evento):
        data = datetime.datetime.today()
        self._cadastros.append(f"{data} - {evento}")


    def get_cadastros(self):
        return self._cadastros
    
    def set_cadastros(self, cadastros):
        self._cadastros = cadastros
        