import datetime

class pessoas:

    ano_atual = datetime.datetime.today().year

    def __init__(self, nome, idade, falando=False, comendo=False):
        self.nome = nome
        self.idade = idade
        self.falando = falando
        self.comendo = comendo


    def falar(self, assunto):
        if self.comendo:
            print(f"O {self.nome} não pode falar comendo")
            return
        elif self.falando:
            print(f"o {self.nome} já está falando")
            return
        elif not self.comendo and not self.falando:
            print(f"o {self.nome} esta falando sobre {assunto}")
            self.falando = True
            return

    def parar_falar(self):
        if not self.falando and not self.comendo:
            print(f"O {self.nome} não está falando")
            return
        elif self.comendo:
            print(f"o {self.nome} não esta falando está comendo")
            return
        elif self.falando:
            print(f" O {self.nome} parou de falar" )
            self.falando = False
            return

    def comecar_comer(self, alimento):
        if self.comendo:
            print(f"O {self.nome} ja está comendo")
            return
        elif self.falando:
            print(f"a {self.nome} está falando não pode comer")
            return
        elif not self.comendo and not self.falando:
            print(f"O {self.nome} está comento {alimento}")
            self.comendo = True
            return

    def parar_comer(self):
        if not self.comendo and not self.falando:
            print(f"o {self.nome} não está comendo e não está falando")
            return
        elif self.falando:
            print(f" o {self.nome} não está comendo, ele está falando")
            return
        elif self.comendo:
            print(f"o {self.nome} parou de comer")
            self.comendo = False

    def status(self):
        print(f"O status falando é : {self.falando} comendo é:  {self.comendo}")

    def get_ano_de_nascimento(self):
        return self.ano_atual - self.idade