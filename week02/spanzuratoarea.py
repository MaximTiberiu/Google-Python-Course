import random
lista_generala = ['repetare', 'streptococ', 'piropopircanita', 'pepene', 'tamaduitoare', 'aeroport',
                  'aeronava', 'mamaliga']


# functie care afiseaza etapele spanzuratorii
def afisare_spanzuratoare(incercari):
    if incercari == 7:
        print(":)")
    elif incercari == 6:
        print('''
        -----
        |   |
        -----
        ''')
    elif incercari == 5:
        print('''
        -----
        |   |
        -----
          |
          |
          |
        ''')
    elif incercari == 4:
        print('''
        -----
        |   |
        -----
        < | >
          |
          |
        ''')
    elif incercari == 3:
        print('''
        -----
        |   |
        -----
        < | >
          |
          |
        <  >
        ''')
    elif incercari == 2:
        print('''
        -----
        |   |
        -----
        < | >
          |
          |
        <   >
        _______
        ''')
    elif incercari == 1:
        print('''
        -----
        |   |
        -----
        < | >
          |
          |
        <   >
        _______
        ^^^^^^^
        ''')
    elif incercari == 0:
        print('''
           -----
           |   |
           -----
           < | >
             |
             |
           <   >
           #######
           ''')


# functie care face initializarile
def init(lista_principala):
    text = []
    for i in range(len(lista_principala)):
        text.append('_')

    prima_litera = lista_principala[0]
    ultima_litera = lista_principala[-1]

    for i in range(len(lista_principala)):
        if prima_litera == lista_principala[i]:
            text[i] = prima_litera
        elif ultima_litera == lista_principala[i]:
            text[i] = ultima_litera

    lista_utilizata = [prima_litera, ultima_litera]
    return text, lista_utilizata


# fucntia care executa jocul
def joc(cuvant):
    lista_principala = list(cuvant)
    text, lista_utilizata = init(lista_principala)
    incercari = 7

    while incercari > 0:
        print("".join(text))
        afisare_spanzuratoare(incercari)

        litera = input("Introduceti litera: ")
        if litera not in lista_utilizata:
            lista_utilizata.append(litera)
        else:
            print("litera deja utilizata!")
            continue

        if litera not in lista_principala:
            incercari -= 1
        else:
            for j in range(1, len(lista_principala) - 1):
                if litera == lista_principala[j] and text[j] == "_":
                    text[j] = litera
                    if '_' not in text:
                        print("Jocul s-a terminat, ai castigat!")
                        return

    print("Ai pierdut! :(")


joc(random.choice(lista_generala))
