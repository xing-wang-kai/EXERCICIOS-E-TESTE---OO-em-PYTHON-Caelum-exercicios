#exercicio para registrar dados de pessoas em um dicionário.

dados = dict()
nome = list()
idade = list()
sexo = list()
cidade = list()
p = 0
while True:
    print("\033[1:37m-=\033[m"*30)
    nome.append(str(input(f"digite o \033[7:33m nome \033[m da {p+1}ª pessoa: ...")))
    idade.append(int(input(f"digite a \033[7:33m idade \033[m da {p+1}ª pessoa: ...")))
    sexo.append(str(input(f"digite o \033[7:33m sexo \033[m da {p+1}ª pessoa: \033[1:31m [M/F] \033[m ...")).upper().strip()[0])
    cidade.append(str(input(f"digite a \033[7:33m cidade \033[m que mora a {p+1}ª pessoa: ...")))
    print("\033[1:37m-=\033[m" * 30)
    continuar = str(input("deseja adicionar mais uma pessoa? \033[1:31m [S/N] \033[m ...")).upper().strip()[0]
    p += 1
    while continuar not in "SsNn":
        continuar = str(input("Insira o valor \033[1:31m[S]\033[m para sim e \033[1:31m[N]\033[m para não: ")).upper().strip()[0]
    if continuar in "Nn":
        break

dados['nome'] = nome
dados["idade"] = idade
dados["sexo"] = sexo
dados["cidade"] = cidade

arquivo_dados = open("arquivo_dados.txt", "w")
for c in range(0, p):
    arquivo_dados.write("-=" * 16)
    arquivo_dados.write("\n")
    print("\033[1:37m-=\033[m" * 20)
    for k, v in dados.items():
        print(f"{k:<10}: {dados[k][c]:>20}")
        arquivo_dados.write(f"{k:<10}: {dados[k][c]:>20}\n")
    print("\033[1:37m-=\033[m" * 20)
    arquivo_dados.write("-=" * 16)
    arquivo_dados.write("\n")
arquivo_dados.close()
