with open('stevila.txt', 'r') as file:  # odpiranje datoteke za branje
    stevila = file.readlines()  # preberemo vsako vrstico in jo shranimo v tabelo

sodaStevila = []  # inicializacija tabele sodaStevila
lihaStevila = []  # inicializacija tabele lihaStevila

for i in stevila:  # sprehod cez vsa stevila
    i = i.strip()  # odstrani presledke in znake za novo vrstico

    if i.isdigit():  # preveri, ali je prebrani znak stevilo
        if int(i) % 2 == 0:  # preveri, ali je stevilo sodo in ga zapise v dolocen seznam
            sodaStevila.append(i)
        else:
            lihaStevila.append(i)

with open('soda.txt', 'w') as file:  # zapisemo vsa soda stevila v datoteko
    for i in sodaStevila:
        file.write(i + "\n")

with open('liha.txt', 'w') as file:  # zapisemo vsa liha stevila v datoteko
    for i in lihaStevila:
        file.write(i + "\n")