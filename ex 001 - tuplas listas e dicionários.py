def base(dados):
    print("=-"*20)
    print(f"{dados:=^40}")
    print("=-"*20)


print("\n \033[1:31m1. Dada a lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52] faça um programa que:\033[m")
lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
print("\n \033[1:34m a) imprima o maior elemento\033[m")
print(f"\n o maior número da lista é {max(lista)}")
print("\n \033[1:34mb) imprima o menor elemento\033[m")
print(f"\n o menor número da lista é {min(lista)}")
print("\n \033[1:34mc) imprima os números pares\033[m")
for par in lista:
    if par % 2 == 0:
        print(f"{par}", end=" ")
print("\n \033[1:34m  d) imprima o número de ocorrências do primeiro elemento da lista \033[m")
print(f"O primeiro número de ocorrencencia da lisa é {lista[0]}")
print("\n \033[1:34m e) imprima a média dos elementos \033[m")
print(f" A média dos elementos da lista é {sum(lista)/len(lista)}")
print("\n \033[1:34mf) imprima a soma dos elementos de valor negativo \033[m")

neg = 0
for c in range(0, len(lista)):
    if lista[c] < 0:
        neg += lista[c]
print(f"O valor somado dos números negátivos da lista é de {neg}")

print("""\n \033[1:31m2. Faça um programa que leia dados do usuário (nome, sobrenome, idade) "
      "adicione em uma lista e imprima seus elementos na tela. \033[m""")

sistema_dados = "\033[1:33mDados pessoais\033[m"
print(base(sistema_dados))

nome = str(input("Qual seu nome? "))
sobrenome = str(input("agora digite seu sobrenome: "))
idade = str(input("agora digite sua idade: "))
dados = []
dados.append(nome)
dados.append(sobrenome)
dados.append(idade)
print(f"os dados informados são {dados}")

sistema_final = "\033[1:31m THE PROGRAM END\033[m"
print(base(sistema_final))

print("\n \033[1:31m 3. Faça um programa que leia 4 notas, mostre as notas e a média na tela.\033[m")
sistema_notas = "\033[1:33mCalcular média do aluno\033[m"

print(base(sistema_notas))

nota1 = float(input("digite a primeira nota do aluno: "))
nota2 = float(input("digite a segunda nota do aluno: "))
nota3 = float(input("digite a terceira nota do aluno: "))
nota4 = float(input("digite a quarta nota do aluno: "))

media = (nota1 + nota2 + nota3 + nota4)/4

print(f"a média do aluno é {media}")
print(base(sistema_final))

print("""\n \033[1:31m4. Faça um programa utilizando um dict que leia dados de entrada do usuário. O usuário deve entrar
com os dados de uma pessoa como nome, idade e cidade onde mora (fique livre para acrescentar
outros). Após isso, você deve imprimir os dados como o exemplo abaixo:
nome: João
idade: 20
cidade: São Paulo \033[m""")

system_dict = "\033[1:33mSOME DICT EXAMPLE:\033[m"

print(base(system_dict))
pessoa = ({})
pessoa["名字"] = str(input("你叫什么名字？: "))
pessoa["大"] = int(input("你多大了？: "))
pessoa["城市"] = str(input("你住哪里？: "))

for keys in pessoa:
    print(f"{keys}: {pessoa[keys]}")

print(base(sistema_final))

print("""\n \033[1:31m5. (Opcional) Utilize o exercício anterior e adicione a pessoa em uma lista. Pergunte ao usuário se ele
deseja adicionar uma nova pessoa. Após adicionar dados de algumas pessoas, você deve imprimir
todos os dados de cada pessoa de forma organizada. \033[m""")

sitem_base = "\033[1:33mAdicionar a base de dados\033[m"
print(base(sitem_base))

data = {}
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
data["nome"] = nome
data["idade"] = idade
data["sexo"] = sexo
data["cidade"] = cidade
for c in range(0, p):
    print(f"dados da {c+1}ª adicionada")
    print("-="*40)
    for k, v in data.items():
        print(f"{k} : {data[k][c]}")
    print("-=" * 40)

print(data)
print(data["nome"][1])
print(len(data.values()))

print(base(sistema_final))

print("\n \033[1:31m \033[m")
print("\n \033[1:34m \033[m")