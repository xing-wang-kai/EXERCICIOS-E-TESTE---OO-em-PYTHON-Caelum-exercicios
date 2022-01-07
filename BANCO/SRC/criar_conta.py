from class_conta import cliente, conta

cliente_01 = cliente("sergio", "antonio", "111.111.111-11")
cliente_02 = cliente("maria", "alessandra", "222.222.222-22")
cliente_03 = cliente("Jose", "riquelme", "333.333.333-33")

conta_01 = conta("1234-001", cliente_01, 3000)
conta_02 = conta("1234-002", cliente_02, 2000)
print(conta._total_conta)
conta_03 = conta("1234-003", cliente_03, 4000)
print(conta._total_conta)

conta.get_total_conta()

conta.conta_01 = "minha conta"

print(conta_01)
"""print(vars(conta_01)) este atributo foi derrubado pelo slot"""
"""for k, intem in vars(conta_01).items():
    print(f"{k} : {intem}")"""
print(conta_01.numero)
print(conta_02.saldo)
print(conta_03._limite)

conta_02.saldo = 3000

print(conta_02.saldo)
conta_01.set_sacar(200)
conta_02.set_depositar(400)
conta_03.set_transferir(300, conta_01)
print("*"*40)
print(conta_01.saldo)
print(conta_02.saldo)
print(conta_03.saldo)
print("*"*40)

conta_01.set_extrato()
conta_02.set_extrato()
conta_03.set_extrato()

conta_01.historico.imprimir()
conta_02.historico.imprimir()
conta_03.historico.imprimir()
print(conta._total_conta)