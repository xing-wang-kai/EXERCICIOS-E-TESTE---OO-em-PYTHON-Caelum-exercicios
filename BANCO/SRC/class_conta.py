"""30.12.2021"""

import datetime


class historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today().year
        self.extrato = []

    def imprimir(self):
        print("-="*25)
        print(f"Data de abertura: {self.data_abertura}")
        for t in self.extrato:
            print(f"--> {t}")
        print("-=" * 25)

class cliente:

    __slots__ = ["nome", "sobrenome", "cpf"]


    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class conta:


    __slots__ = ["numero", "titular", "_saldo", "_limite", "historico"]


    _total_conta = 0
    def __init__(self, numero, titular, saldo, limite=5000):
        self.numero = numero
        self.titular = titular
        self._saldo = saldo
        self._limite = limite
        self.historico = historico()
        """conta._total_conta += 1"""
        type(self)._total_conta += 1

    """@staticmethod
    def get_total_contas():
        return conta._total_conta"""
    @classmethod
    def get_total_conta(cls):
        return cls._total_conta

    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, saldo):
        if (self._saldo < 0):
            print("O valor da conta não pode ser negativo")
        else:
            self._saldo = saldo


    def get_saca(self):
        return self._saldo

    def set_sacar(self, valor):
        if self._saldo - valor < 0:
            print(f"não é possivel sacar a conta ficará negativa")
        else:
            self._saldo -= valor
            self.historico.extrato.append(f"Sacou R${valor} saldo R${self._saldo}")


    def set_depositar(self, valor):
        self._saldo += valor
        self.historico.extrato.append(f"Depositou R${valor} saldo R${self._saldo}")


    def set_transferir(self, valor, remetente):
        if self._saldo < 0:
            print(f"transferencia foi negada a conta ficará negativa")
        else:
            self._saldo -= valor
            remetente._saldo += valor
            self.historico.extrato.append(f"Transferiu R${valor} de conta{self.numero} para a conta {remetente.numero} saldo R$ {self._saldo}")
            remetente.historico.extrato.append(f"Recebeu transf R${valor} de conta{self.numero} saldo R$ {remetente._saldo}")

    def set_extrato(self):
        print("-=" * 30)
        print(f"A conta: {self.numero}\nSaldo: {self._saldo}")
        print("-=" * 30)
        self.historico.extrato.append(f"você retirou o extrato {datetime.datetime.today()}")


