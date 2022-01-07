"""26.12.2021"""
import random

arquivo = open("fruit_list.txt", "w")
arquivo.write("banana\n")
arquivo.write("pineapple\n")
arquivo.write("orange\n")
arquivo.write("strawberry\n")
arquivo.write("blueberry\n")
arquivo.write("cherry\n")
arquivo.write("grapefruit\n")
arquivo.write("blackberry\n")
arquivo.write("coconut\n")
arquivo.write("kiwifruit\n")
arquivo.write("watermelon\n")
arquivo.close()

arquivo = open("fruit_list.txt", "r")
secret_list = [item.upper().strip() for item in arquivo]

arquivo.close()

secret_word = random.choice(secret_list)
"""hangman_word = ["_" for item in secret_word]"""
hangman_word = []
for item in secret_word:
    hangman_word.append("_")

winner = loser = False

erro =  0

while not winner and not loser:
    guess = str(input("choice you guess letter: ")).upper().strip()[0]
    posicion = 0
    if guess in secret_word:
        for letter in secret_word:
            if guess == letter:
                hangman_word[posicion] = letter
            posicion += 1
    else:
        erro += 1
    print(f"{hangman_word}")
    print(f"{erro}")
    print(posicion)
    winner = "_" not in hangman_word
    loser = erro == 7

if winner:
    print('\033[7:33m    CONGRATULATIONS YOU WIN!!   \033[m')
    print("\033[7:33m            ___________         \033[m")
    print("\033[7:33m           ' ._==_==_=_. '      \033[m")
    print("\033[7:33m       .-\ \:           /-.     \033[m")
    print("\033[7:33m       | (|:.           |) |    \033[m")
    print("\033[7:33m        '-|:.           |-'     \033[m")
    print("\033[7:33m         \ \::.         /       \033[m")
    print("\033[7:33m            '::.    .'          \033[m")
    print("\033[7:33m               )   (            \033[m")
    print("\033[7:33m             _.'   '._          \033[m")
    print("\033[7:33m            ' ------- '         \033[m")
elif loser:
    """"Define a mensagem de perdeu"""
    print('\033[7:31m             YOU LOSE!!            \033[m')
    print(f'\033[7:31m    THE CHOISEN WORD WAS {secret_word}\033[m')
    print("\033[7:31m         _______________           \033[m")
    print("\033[7:31m  /                         \      \033[m")
    print("\033[7:31m /                           \     \033[m")
    print("\033[7:31m//                            \/\  \033[m")
    print("\033[7:31m\|     XXXX            XXXX   | /  \033[m")
    print("\033[7:31m |     XXXX            XXXX   |/   \033[m")
    print("\033[7:31m |      XXX            XXX    |    \033[m")
    print("\033[7:31m |                            |    \033[m")
    print("\033[7:31m  \__           XXX        __/     \033[m")
    print("\033[7:31m    |\          XXX       /|       \033[m")
    print("\033[7:31m    | |                  | |       \033[m")
    print("\033[7:31m    |     I I I I I I I    |       \033[m")
    print("\033[7:31m    |      I I I I I I     |       \033[m")
    print("\033[7:31m     \_                  _/        \033[m")
    print("\033[7:31m       \_              _/          \033[m")
    print("\033[7:31m         \___     ____/            \033[m")


print(secret_list)
print(secret_word)
print(hangman_word)