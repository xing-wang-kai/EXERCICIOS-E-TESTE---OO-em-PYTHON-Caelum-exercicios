"""29.12.2021"""

def extrair_dados(dados_1, dados_2):

    lista_01 = list(zip(dados_1["nome"], dados_1["email"], dados_1["enviado"]))
    lista_02 = list(zip(dados_2["nome"], dados_2["email"], dados_2["enviado"]))

    total_dados = lista_01 + lista_02
    emails = []
    for item in total_dados:
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
emails = extrair_dados(dados_1, dados_2)
print(emails)
print(len(emails))

for item in emails:
    print(f"E-MAIL: \033[1:32m{item:<50}\033[m STATUS: enviado...")