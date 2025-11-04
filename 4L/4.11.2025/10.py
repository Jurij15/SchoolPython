def izpisi_meni():
    print("1.Dodaj ime v seznam")
    print("2.Izbriši zadnje ime")
    print("3.Prikaži trenutni seznam")
    print("4.Konec")

seznam = []

while True:
    izpisi_meni()
    izbor = int(input())
    if izbor == 1:
        print("Vnesi ime")
        ime = input()
        seznam.append(ime)
    elif izbor == 2:
        print("izbrisano zadnje ime")
        seznam.remove(seznam[len(seznam)-1])
    elif izbor == 3:
        print(seznam)
    elif izbor == 4:
        print("KONEC")
        break
    else:
        print("NAPAČNI IZBOR")