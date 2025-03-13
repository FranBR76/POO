from conta import Conta     #instanciar classe conta 

conta = Conta('123-4', 'Rodrigo', 120.0, 1000.0) 
type(conta)


# conta.extrato()

# print(conta.titular)

# conta.depositar(200.0)
# conta.extrato()

# conta.sacar(50.0)
# conta.extrato()

# consegui = conta.sacar(222.0)
# if(consegui):
#     print("Consegui sacar")
#     print("Restam ainda: {}".format(conta.saldo))
# else:
#     print("Saldo insuficiente!")



from emprestimo import Emprestimo

livro = Emprestimo('123456', 'O menino maluquinho', 'Ziraldo', 'Disponivel', 'Senac Livros', 'Nenhum', '15/03/2025', '06/03/2025')

print(livro.status)

