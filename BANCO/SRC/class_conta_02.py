import datetime
class historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []


    def historico_imprimir(self):
        print("*"*30)
        print(f"A DATA DE ABERTURA:{self.data_abertura}")
        for t in self.transacoes:
            print(f" -- {t}")
        print("*" * 30)



class cliente:
    def __init__(self, nome, sobrenome, CPF):
        self.nome = nome
        self.sobrenome = sobrenome
        self.CPF = CPF


class conta:

    #conta_abertas calcula o número de conta, notar que a variavel não inicia com SELF e sim cm CONTA uma vez que é ela objeto da conta.
    _contas_abertas = 0
    def __init__(self, numero, titular, saldo, limite=5000):
        self.numero = numero
        self.titular = titular
        self._saldo = saldo
        self.limite = limite
        self.historico = historico()
        conta._contas_abertas += 1


    def conta_sacar(self, valor):
        self.valor = valor
        if valor > self._saldo:
            print(f"O saldo é R${self._saldo} o valor a ser sacado é R$ {self.valor}, não é possiel sacar")
        else:
            self._saldo -= valor
            self.historico.transacoes.append(f"SACOU R$ {valor} \n-- SALDO R$ {self._saldo}")


    def conta_depositar(self, valor):
        self.valor = valor
        self._saldo += valor
        self.historico.transacoes.append(f"DEPOSITOU R$ {valor} \n-- SALDO R$ {self._saldo}")


    def conta_transferir_para(self, valor, remetente):
        self.valor = valor
        self.remetente = remetente
        self.conta_sacar(valor)
        remetente.conta_depositar(valor)
        remetente.historico.transacoes.append(f"RECEBEU TRANSFERENCIA DE R$ {valor} \n-- DA CONTA {self.numero} ")
        self.historico.transacoes.append(f"TRANSFERIU R$ {valor} para a conta {remetente.numero}")


    def conta_extrato(self):
        print("*"*30)
        print(f"a CONTA: {self.numero} \no SALDO é R${self.saldo}")
        print("*" * 30)



# usando o código para encapsular a propriedade que está protegida, devido a regra de nogócios não foi protegido sacar depositar e transferir somente demais operações.
    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, saldo):
        if self._saldo < 0:
            print('não é possivel realizar está operação valor negativo')
        else:
            self._saldo = saldo


    """def get_saldo(self):
        return self.saldo
    def set_saldo(self, saldo):
        if saldo < 0:
            print('não é possivel realizar está operação valor negativo')
        else:
            self.saldo = saldo"""
