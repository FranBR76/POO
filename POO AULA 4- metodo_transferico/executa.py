from conta import Conta

c1 = Conta('123-4', 'Rodrigo', 120.0, 1000.0)
c2 = Conta('234-5', 'Gilson', 50.0, 1000.0)
# c1 é um atributo de referencia para um objeto para que isso ocorra no python sao acionados de forma transparente os metodos magicos 
# __new__() e __init__() responsaveis por construir e iniciar objetos.
c3 = Conta('123-4', 'Rodrigo', 120.0, 1000.0)


# print(c2.saldo)
# c2.depositar(0.50)
# print(c2.saldo)

# print(c1.saldo)
# c1.depositar(10000.0)
# print(c1.saldo)

if(c1 == c3):
    print("Contas são iguais")
else:
    print("Contas são diferentes")


from pessoa import Pessoa

p1 = Pessoa('Jean Vargas', 45, 1000.0)
p2 = Pessoa('Cesco Matteo', 19, 905.10)
p3 = Pessoa('Mateus Ortileb', 18, 900.0)
p4 = Pessoa('Pedro Dias', 21, 1000.0)

p1.exibeNome()
p1.exibeIdade()
p1.exibeSalario()

p2.exibeNome()
p2.exibeIdade()
p2.exibeSalario()

p3.exibeNome()
p3.exibeIdade()
p3.exibeSalario()   

p4.exibeNome()
p4.exibeIdade()
p4.exibeSalario()