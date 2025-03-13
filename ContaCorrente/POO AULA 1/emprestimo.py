class Emprestimo:
    def __init__ (self, isbn, titulo, autor, status, editora, UsuarioAtual, dataEntrega, dataEmprestimo):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.status = status
        self.editora = editora
        self.UsuarioAtual = UsuarioAtual
        self.dataEntrega = dataEntrega
        self.dataEmprestimo = dataEmprestimo

    
    def emprestar(self, UsuarioAtual):
        if(self.status == 'Emprestado'):
            print('Livro "{}" ja esta emprestado para: {}\nData de entrega: {}\n Data do emprestimo: {}'.format(self.titulo, self.UsuarioAtual, self.dataEntrega, self.dataEmprestimo))
        else:
            self.status = 'Emprestado'
            self.UsuarioAtual = UsuarioAtual
            print('Livro "{}" emprestado para: {}'.format(self.titulo, self.UsuarioAtual))

    def devolver(self):
        if(self.status == 'Disponivel'):
            print('Livro "{}" não foi emprestado'.format(self.titulo))
        else:
            self.status = 'Disponivel'
            self.UsuarioAtual = "Ninguem"
            print('Livro "{}" devolvido'.format(self.titulo))


    def status(self):
        print("Status: {} \nUsuario Atual: {}\nISBN: {}\nTitulo: {}".format(self.status, self.UsuarioAtual, self.isbn, self.titulo))

