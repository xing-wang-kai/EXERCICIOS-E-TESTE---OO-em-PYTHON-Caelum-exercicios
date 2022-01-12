"""11.01.2022"""
"""repetir em outro dia"""

import datetime

class historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today().year
        self.lista = []

    def imprimir(self):
        print ("*"*20)
        print(f"A sua conta foi aberta em {self.data_abertura}")
        for item in self.lista:
            print (f"--{item}")
        print("*" * 20)

class conta:

    _tot_conta = 0
    def __init__(self, numero, nome, saldo, limite = 5000):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
        self.limite = limite
        self.historico = historico()
        type(self)._tot_conta += 1

    @classmethod
    def get_total_conta(cls):
        return cls._tot_conta


    def sacar(self, valor):
        if valor >= self.saldo:
            print(f"o {valor:2f} é maior que o saldo {self.saldo:.f}")
        else:
            self.saldo -= valor
            self.historico.lista.append(f"{datetime.datetime.today()}")
            self.historico.lista.append(f"-você sacou o valor de R$ {valor:.2f} saldo atual {self.saldo}")

    def depositar(self, valor):
        self.saldo += valor
        self.historico.lista.append(f"{datetime.datetime.today()}")
        self.historico.lista.append(f"-você depositou o valor de R${valor:.2f} saldo atual {self.saldo}")

    def transferir(self, valor, nun_conta):
        self.sacar(valor)
        nun_conta.saldo += valor
        self.historico.lista.append(f"{datetime.datetime.today()}")
        nun_conta.historico.lista.append(f"{datetime.datetime.today()}")
        self.historico.lista.append(f"-você depositou o valor de R${valor:.2f} na conta {nun_conta.numero} em nome de {nun_conta.nome}")
        nun_conta.historico.lista.append(f"-Você recebeu deposito no valor de {valor:.2f} da conta{self.numero} em nome de {self.nome}")
    def estrato(self):
        print(f"o saldo atual é de{self.saldo}")
        self.historico.lista.append(f"{datetime.datetime.today()}")
        self.historico.lista.append(f"o saldo do extrato é de  {self.historico.data_abertura}")





