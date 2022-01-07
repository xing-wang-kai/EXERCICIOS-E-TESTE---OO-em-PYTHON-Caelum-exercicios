import abc


class funcionario(abc.ABC):
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    @abc.abstractmethod
    def get_bonificacao(self):
        return self._salario * 0.10

class gerente(funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd_funcionario):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_funcionario = qtd_funcionario

    def autenticar_senha(self):
        if self._senha == senha:
            print("acesso permitido")
            return True
        else:
            print("acesso negado")
    def get_bonificacao(self):
        return super().get_bonificacao()+1000

class controle_bonificar:
    def __init__(self, total_bonificar=0):
        self._total_bonificar = total_bonificar
    def registrar(self, obj):
        if (hasattr(obj, "get_bonificacao")):
            self._total_bonificar += obj.get_bonificacao()
        else:
            print("o Objeto informado não tem bonificação")
    @property
    def total_bonificacao(self):
        return self._total_bonificar

class cliente:
    def __init__(self, nome, cpf, data_nascimento):
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento



"""import abc

class funcionario(abc.ABC):
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self._cpf = cpf
        self._salario = salario

    @abc.abstractmethod
    def get_bonificar(self):
        return self._salario * 0.15

class gerente(funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd_funcionario):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_funcionario = qtd_funcionario

    def autenticar(self, senha):
        if senha == self._senha:
            print("acesso permitido")
            return True
        else:
            print("acesso Negado")
            return False
    def get_bonificar(self):
        return super().get_bonificar() + 1000

class controle_bonificar:
    def __init__(self, total_bonificar=0):
        self._total_bonificar = total_bonificar
    def registrar(self, obj):
        if (hasattr(obj, "get_bonificar")):
            self._total_bonificar += obj.get_bonificar()
        else:
            print(f"A instancia {self.__class__.__name__} não possui a instancia bonificar")
    @property
    def total_bonificar(self):
        return self._total_bonificar

class cliente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
"""