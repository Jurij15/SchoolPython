def navodila():
    print("1 - Vnos")
    print("2 - Brisanje zadnjega imena")
    print("3 - Izpis seznama")
    print("4 - Konec")


seznam = []

while True:
    navodila()
    vnos = int(input("Vnos: "))
    if vnos == 1:
        ime = input("Ime: ")
        seznam.append(ime)
        continue
    elif vnos == 2:
        seznam.pop()
    elif vnos == 3:
        print(seznam)
    elif vnos == 4:
        print("Program zaključen")
        break