from class_funcionarios import funcionario, gerente, cliente, controle_bonificar

gerente_01 = gerente("joão", "111.111.111-11", 5000, 1234, 0)
gerente_02 = gerente("maria", "222.222.222-11", 3000, 1234, 0)

print(gerente_01._nome)
print(gerente_01.get_bonificacao())
print(gerente_02.get_bonificacao())

print(vars(gerente_01))
print(vars(gerente_02))

cliente_01 = cliente("maria", "222.222.222-22", "21")

print(vars(cliente_01))

controle = controle_bonificar()
controle.registrar(gerente_01)
controle.registrar(gerente_02)


print(f"o total é {controle.total_bonificacao}")

print(eval("2+5"))