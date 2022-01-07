import random


def function_playgame():


    open_msg = "WELCOME TO HANGMAN GAME"
    print(msg_open(open_msg))

    secret_list = function_open_file()

    secret_word = random.choice(secret_list)
    hangman_list = ["_" for item in secret_word]

    winner = loser = False
    erro = 0

    while not winner and not loser:
        guess = str(input("\ninput you guess letter here: ")).upper().strip()
        posicao = 0
        if guess in secret_word:
            for letter in secret_word:
                if guess == letter:
                    hangman_list[posicao] = letter
                posicao += 1
            for item in hangman_list:
                print(f"|{item}|", end =" ")
        else:
            erro += 1
            print(f"the guess {guess} not in secret word, please try again, you have { 7 - erro} chances ")
        winner = "_" not in hangman_list
        loser = erro == 7
    if winner:
        function_winner_msg()
    elif loser:
        function_loser_msg(secret_word)

def function_winner_msg():

    """
    this function print winner mensage
    :return:
    """

    print('\n\033[7:33m    CONGRATULATIONS YOU WIN!!   \033[m')
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

def function_loser_msg(secret_word):

    """
    This function Print the mensagem LOSER
    :param secret_word:  this is the word computer was difined in choice in radom in secret_list
    :return: 
    """

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


def function_open_file():

    """
    This function write the words in one file.txt for choice in secret_word for the hangman game
    :return:
    """
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

    return secret_list

def msg_open(msg):
    """
    Esta função mostra a mensagem de boas vinda ao Game
    :param msg:  A mensagem é personalisada definida em MSG
    :return:
    """
    print("\033[7:33m-=\033[m" * 50)
    print(f"\033[7:33m{msg:=^100}\033[m")
    print("\033[7:33m-=\033[m" * 50)


print(function_playgame())
