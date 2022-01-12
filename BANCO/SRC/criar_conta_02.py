from class_conta_02 import conta, historico
from time import sleep

conta01 = conta("1234-01", "joão", 3000)
conta02 = conta("1234-02", "maria", 2000)
conta03 = conta("1234-03", "joaquim", 3000)


conta01.sacar(200)
sleep(1)
conta02.depositar(400)
sleep(1)
conta03.transferir(500, conta02)
sleep(1)
conta01.depositar(400)
sleep(1)
conta01.historico.imprimir()
conta02.historico.imprimir()
conta03.historico.imprimir()

