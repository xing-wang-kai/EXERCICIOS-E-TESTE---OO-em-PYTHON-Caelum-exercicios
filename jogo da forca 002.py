"""21.01.2022"""

import random


def function_jogar():


    print("*" * 50)
    print("*" *10 + "WELCOME TO HANGMANGAME" + "*" * 10)
    print("*" * 50)

    secretWord = function_secret_word()

    print(secretWord)

    hangman_secret_word = ["|_|" for item in secretWord]
    print(hangman_secret_word)

    winner = looser = False
    error = 0
    rights = 0

    while not winner and not looser:
        r = input(str("Input any character from A at Z for secret word: []: ")).upper().strip()[0]
        if r in secretWord:
            x = 0
            for item in secretWord:
                if item == r:
                    hangman_secret_word[x] = r
                    rights += 1
                x += 1
        else:
            error += 1
        print(hangman_secret_word)
        print(f"you aready error = {error}, have rights {rights}")

        winner = "|_|" not in hangman_secret_word
        looser = error == 7
    if winner:
        function_winner()
    else:
        function_looser(secretWord)




def function_secret_word():
    arquivo = open("newWordList.txt", "w");

    wordlist02 = "banana\n pineapple\n orange\n strawberry\n blueberry\n cherry\n grapefruit\n blackberry\n coconut\n kiwifruit\n watermelon\n".upper().split()

    for item in wordlist02:
        arquivo.write(item + "\n")
    arquivo.close()

    arquivo = open("newWordList.txt", "r")

    secret_list = [item.upper().strip() for item in arquivo]

    secretWord = random.choice(secret_list)

    arquivo.close()

    return secretWord

def function_winner():

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

def function_looser(secret_word):

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




function_jogar()




