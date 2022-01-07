from class_conta_02 import cliente, conta

cliente_001 = cliente("deusivaldo", "portela", "111.111.111-11")
cliente_002 = cliente("deusnir", "portela", "222.222.222-45")
cliente_003 = cliente("algusto", "fonseca", "333.333.333-45")

conta_001 = conta("1234-001", cliente_001, 4000)
conta_002 = conta("1234-002", cliente_002, 3000)
conta_003 = conta("1234-003", cliente_003, 5000)


conta_001.conta_extrato()
conta_002.conta_extrato()
conta_003.conta_extrato()

print(cliente_001.nome)
print(vars(conta_001))

conta_001.conta_sacar(900)
conta_001.conta_transferir_para(200, conta_003)
conta_001.conta_extrato()
conta_003.conta_extrato()

conta_001.historico.historico_imprimir()
conta_002.historico.historico_imprimir()
conta_003.historico.historico_imprimir()