from funcionario import Funcionario
from gerente import Gerente

gerente = Gerente('Rodrigo', 
                  '66756565', 
                  'gerente',
                  20000.00,
                  '1234',
                  5)



# print(gerente.get_bonificacao())
# print(vars(gerente))

# gerente.autentica('1234')

funcionario = Funcionario('Alessandra',
                          '885478745',
                          'Analista',
                          5000.00)

print(funcionario.get_bonificacao())
print(vars(funcionario))