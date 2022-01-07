#este exercicio foi feito para testar os dicionário e tentar puxar valores em tupla para cada key dentro da lista


dados = {}
nome = list()
idade = list()
sexo = list()
cidade = list()

p = 0
while True:
    nome.append(str(input("digite seu nome: ")))
    sexo.append(str(input("sexo F/M? ")))
    idade.append(int(input("qual a idade? ")))
    cidade.append(str(input("vive em qual cidade? ")))
    r = str(input("deseja continuar? [S/N] ")).upper().strip()[0]
    p += 1
    if r not in "Ss":
        break
dados["nome"] = nome
dados["idade"] = idade
dados["sexo"] = sexo
dados["cidade"] = cidade
for c in range(0, p):
    print(f"dados da {c+1}ª adicionada")
    print("-="*40)
    for k, v in dados.items():
        print(f"{k} : {dados[k][c]}")
    print("-=" * 40)

print(dados)
print(dados["nome"][1])
print(len(dados.values()))