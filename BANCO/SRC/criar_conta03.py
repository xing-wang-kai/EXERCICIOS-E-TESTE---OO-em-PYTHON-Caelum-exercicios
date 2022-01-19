from class_conta_03 import Conta


conta01 = Conta("1234-21", "Antonio", 5000)
conta02 = Conta("1234-33", "Maria", 4000)
conta03 = Conta("1234-44", "Joaquim", 3000)
nome_conta = conta01.get_nome()
print(nome_conta)


conta01.sacar(400)
conta02.transferir(800, conta03)
conta03.depositar(200)

conta01.transferir(500, conta03)

print(conta01.historico.imprimir())
print(conta02.historico.imprimir())
print(conta03.historico.imprimir())