from conta import Conta
# from cliente import Cliente


conta1 = Conta(200.0)
conta2 = Conta(300.0)
conta3 = Conta(-100.00)

print(conta1.get_saldo())
print(conta2.get_saldo())

conta3.set_saldo(conta1.get_saldo() + conta2.get_saldo())
print(conta3.get_saldo())