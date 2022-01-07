# os emails que estão como false não foram enviados, os e-maisl como true sim, preciso criar um programa que separe uma lista de emails não enviados

def extrair_emails(dados_1, dados_2):
    """
    Esta função retorna os dados que estão falso em um e-mail neste caso os e-mails que não receberam os arquivos estão
    como falso e precisamos enviar os arquivos -
    para este programa funcionar o dicionário precisa conter as chaves nome, email e enviado sendo nome o nome do titular
    email o endereço de email do titular e enviado com a informação falso ou true para enviado ou não enviado.
    :param dados_1: lista de dados 1 extraida da JSON
    :param dados_2: lista de dados 2 extraida da JSON
    :return: retorna os e-mails que ainda não foram enviados
    """
    list_1 = list(zip(dados_1["nome"], dados_1["email"], dados_1["enviado"]))
    list_2 = list(zip(dados_2["nome"], dados_2["email"], dados_2["enviado"]))

    dados = list_1 + list_2

    emails = list()
    for item in dados:
        if not item[2]:
            emails.append(item[1])
    return emails


dados_1 = {
    'nome': ['Sonia Weber', 'Daryl Lowe', 'Vernon Carroll', 'Basil Gilliam', 'Mechelle Cobb', 'Edan Booker', 'Igor Wyatt', 'Ethan Franklin', 'Reed Williamson', 'Price Singleton'],
    'email': ['Lorem.ipsum@cursusvestibulumMauris.com', 'auctor@magnis.org', 'at@magnaUttincidunt.org', 'mauris.sagittis@sem.com', 'nec.euismod.in@mattis.co.uk', 'egestas@massaMaurisvestibulum.edu', 'semper.auctor.Mauris@Crasdolordolor.edu', 'risus.Quisque@condimentum.com', 'Donec@nislMaecenasmalesuada.net', 'Aenean.gravida@atrisus.edu'],
    'enviado': [False, False, False, False, False, False, False, True, False, False]
}

dados_2 = {
    'nome': ['Travis Shepherd', 'Hoyt Glass', 'Jennifer Aguirre', 'Cassady Ayers', 'Colin Myers', 'Herrod Curtis', 'Cecilia Park', 'Hop Byrd', 'Beatrice Silva', 'Alden Morales'],
    'email': ['at@sed.org', 'ac.arcu.Nunc@auctor.edu', 'nunc.Quisque.ornare@nibhAliquam.co.uk', 'non.arcu@mauriseu.com', 'fringilla.cursus.purus@erategetipsum.ca', 'Fusce.fermentum@tellus.co.uk', 'dolor.tempus.non@ipsum.net', 'blandit.congue.In@libero.com', 'nec.tempus.mauris@Suspendisse.com', 'felis@urnaconvalliserat.org'],
    'enviado': [False, False, False, True, True, True, False, True, True, False]
}
emails = extrair_emails(dados_1, dados_2)

for item in emails:
    print(f" E-mail: {item:^40} reenviar...")

lista = [1, 4, 3, 6, 3, 2, 6, 7, 4, 5,]

print(sorted(lista))
print(lista)

