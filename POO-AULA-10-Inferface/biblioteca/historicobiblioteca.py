import datetime


class HistoricoAluno:
    def __init__(self):
        # self.data_abertura = datetime.datetime.today()
        self._emprestimos = []
        

    def imprime(self):
        
        # print("Data de cadastro do livro: {} \n".format(self.data_abertura))
        print("Registros: ")
        for e in self._emprestimos:
            print("- ", e)

    def registrar_evento(self, evento):
        data = datetime.datetime.today()
        self._emprestimos.append(f"{data} - {evento}")


    def get_emprestimos(self):
        return self._emprestimos
    
    def set_emprestimos(self, emprestimos):
        self._emprestimos = emprestimos
        