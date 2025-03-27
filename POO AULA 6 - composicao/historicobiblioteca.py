import datetime


class HistoricoBiblioteca:
    def __init__(self):
        # self.data_abertura = datetime.datetime.today()
        self.emprestimos = []
        

    def imprime(self):
        
        # print("Data de cadastro do livro: {} \n".format(self.data_abertura))
        print("Emprestimos: ")
        for e in self.emprestimos:
            print("- ", e)

    def registrar_evento(self, evento):
        data = datetime.datetime.today()
        self.emprestimos.append(f"{data} - {evento}")