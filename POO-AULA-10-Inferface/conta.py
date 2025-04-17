from historico import Historico

import tkinter as tk
from tkinter import messagebox


class Conta:
    def __init__ (self, numero, titular, saldo):
        self._titular = titular
        self._numero = numero
        self._saldo = saldo
        # self._limite = limite
        # self.historico = Historico()
        # O _ antes dos atributos faz com o dev entenda que é pra ser um atributo privado, q n é pra ser mexido, não permitindo o usuario alterar informações sem usar métodos| Serve para encapsular

    #Metodo SET e GET encapsulamento
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if(self._saldo < 0):
            print("Saldo não pode ser negativo!")
        else:
            self._saldo = saldo
        

    def depositar(self, valor):
        if(self.saldo > 0):
            self.saldo += valor
            return True
        return False
        
        # self.historico.transacoes.append("Deposito de {}".format(valor))

    def sacar(self, valor):
        if(self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            # self.historico.transacoes.append("Saque de {}".format(valor))
            return True
        


    def extrato(self):
        print("Numero: {} \nSaldo: {}".format(self.numero, self.saldo))
        self.historico.transacoes.append("Tirou extrato - saldo de {}".format(self.saldo))

    def transferencia(self, destino, valor):
        retirou = self.sacar(valor)
        if(retirou == False):
            return False
        else:
            destino.depositar(valor)
            self.historico.transacoes.append("Transferencia de {} para conta {}".format(valor, destino.numero))
            return True


    def detalhes(self):
        return f"Conta {self._numero} \nTitular: {self._titular}\nSaldo: {self._saldo} "