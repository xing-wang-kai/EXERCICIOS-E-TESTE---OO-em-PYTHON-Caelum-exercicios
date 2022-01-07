import random
"""27.12.2021"""


def function_newgame_hangmangame():
    open_smg = "WELCOME TO HANGMANGAME BY KAI"

    function_open_smg(open_smg)

    secret_word = function_define_secret_word()

    hangman_list = ["_" for item in secret_word]

    print(hangman_list)

    winner = loser = False

    erro = 0

    while not winner and not loser:
        guess = str(input("\nInput your guess letter: ")).upper().strip()[0]

        if guess in secret_word:
            function_complet_hangman_list(guess, secret_word, hangman_list)
        else:
            print(
                f"\nThe guess letter isn't in secret_word, please try again you have \033[1:31m {6 - erro}\033[m chances\n")
            erro += 1

        function_style_hangman_list(hangman_list)

        winner = "_" not in hangman_list
        loser = erro == 7

    if winner:
        function_winner_smg()
    elif loser:
        function_loser_smg(secret_word)


def function_open_smg(smg):
    print("\033[7:34m-=\033[m"*24)
    print(f"\033[7:34m{smg:-^48}\033[m")
    print("\033[7:34m-=\033[m" * 24)


def function_winner_smg():
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


def function_loser_smg(secret_word):
    """
        This function Print the mensagem LOSER
        :param secret_word:  this is the word computer was difined in choice in radom in secret_list
        :return:
        """

    print('\n\033[7:31m             YOU LOSE!!            \033[m')
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


def function_define_secret_word():
    word_dados = open("fruit_list.txt", "w")
    word_dados.write("banana\n")
    word_dados.write("pineapple\n")
    word_dados.write("orange\n")
    word_dados.write("strawberry\n")
    word_dados.write("blueberry\n")
    word_dados.write("cherry\n")
    word_dados.write("grapefruit\n")
    word_dados.write("blackberry\n")
    word_dados.write("coconut\n")
    word_dados.write("kiwifruit\n")
    word_dados.write("watermelon\n")
    word_dados.close()

    word_dados = open("fruit_list.txt", "r")
    secret_list = []
    for words in word_dados:
        secret_list.append(words.strip().upper())

    print(f"{secret_list}")

    secret_word = random.choice(secret_list)
    print(secret_word)
    return secret_word


def function_complet_hangman_list(guess, secret_word, hangman_list, ):
    posiction = 0
    for letter in secret_word:
        if guess == letter:
            hangman_list[posiction] = f"\033[7:31m {letter} \033[m"
        posiction += 1


def function_style_hangman_list(hangman_list):
        for item in hangman_list:
            print(f"|{item}|", end = " ")


function_newgame_hangmangame()
