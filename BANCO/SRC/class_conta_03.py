"""18.01.2021"""

import datetime

class historico:
    def __init__(self):
        self.dataabertura = datetime.datetime.today().year
        self.extrato = []

    def imprimir(self):
        print(f"a data de ABERTURA É {self.dataabertura}")
        print("-=" * 25)
        for item in self.extrato:
            print(f"---{item}\n")
        print("-=" * 25)


class Conta:

    __slots__ = ["_numero", "_nome", "_saldo", "_limite", "historico"]
    _total_contas = 0
    def __init__(self, _numero, _nome, _saldo, _limite=5000):
        self._numero = _numero
        self._nome = _nome
        self._saldo = _saldo
        self._limite = _limite
        self.historico = historico()
        type(self)._total_contas += 1

    @classmethod
    def get_total_conta(cls):
        return cls._total_contas #this method return the total account number is create using the class, the method using class method for memoraze information;

#THIS IS THE CLASS METHODS FOR GETTER E SETTERS

    def get_numero(self):
        return self._numero

    def set_numero(self, numero):
        self._numero = numero

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, saldo):
        if (saldo > self.limite()):
            print("Não é possivel vincular saldo maior que o limite\n")
        else:
            self._saldo = saldo

    def get_limite(self):
        return self._limite

    def set_limite(self, limite):
        self._limite = limite

    def sacar(self, valor):
        if (valor > self.get_saldo()):
            print("não e possivel sacar")
            return True
        else:
            self._saldo -= valor
            self.historico.extrato.append(f"VALOR SACADO R$ {valor} DA CONTA: {self.get_numero()} EM NOME: {self.get_nome()}")
            self.historico.extrato.append(f"O SALDO ATUAL É R$ {self.get_saldo()}")
            return False

    def depositar(self, valor):
        self._saldo += valor
        self.historico.extrato.append(f"O VALOR DEPOSITADO R$ {valor} NA CONTA: {self.get_numero()} EM NOME: {self.get_nome()}")
        self.historico.extrato.append(f"O SALDO ATUAL É R$ {self.get_saldo()}")

    def transferir(self, valor, remetente):
        self.sacar(valor)
        remetente.depositar(valor)
        self.historico.extrato.append(f"VOCE DEPOSITOU R$ {valor} PARA CONTA: {remetente.get_numero()} EM NOME DE {remetente.get_nome()}")
        self.historico.extrato.append(f"O SALDO ATUAL É R$ {self.get_saldo()}")
        remetente.historico.extrato.append(f"VOCE RECEBEU DEPOSITO DE R$ {valor} da conta {self.get_numero()} no NOME DE: {self.get_nome()}")
        remetente.historico.extrato.append(f"O SALDO ATUAL É R$ {remetente.get_saldo()}")

