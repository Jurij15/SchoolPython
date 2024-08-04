# funkcije
def sestevanje(a, b, ):
    print(a + b)


def odstevanje(a, b, ):
    print(a - b)


def mnozenje(a, b, ):
    print(a * b)


def deljenje(a, b, ):
    if a == 0 or b == 0:
        print("Napaka: deljenje z 0 ni mogoče")
    print(a / b)


def deljenjezostankom(a, b, ):
    if a == 0 or b == 0:
        print("Napaka: deljenje z 0 ni mogoče")
    print(a % b)


def deljenjescelimdelom(a, b, ):
    if a == 0 or b == 0:
        print("Napaka: deljenje z 0 ni mogoče")
    print(a // b)


def kvadrat(a, b, ):
    print(a ** b)


def meni():
    print("\n")
    print("Meni kalkulatorja")
    print("Izberi računsko operacijo")
    print("Vnesi + za seštevanje")
    print("Vnesi - za odštevanje")
    print("Vnesi * za množenje")
    print("Vnesi / za deljenje")
    print("Vnesi % za deljenje z ostankom")
    print("Vnesi // za deljenje s celim delom")
    print("Vnesi ** za kvadrat")

while True:
    meni()

    opcija = input("\n")
    funkcija = exit

    if opcija == "+":
        funkcija = sestevanje
    elif opcija == "-":
        funkcija = odstevanje
    elif opcija == "*":
        funkcija = mnozenje
    elif opcija == "/":
        funkcija = deljenje
    elif opcija == "%":
        funkcija = deljenjezostankom
    elif opcija == "//":
        funkcija = deljenjescelimdelom
    elif opcija == "**":
        funkcija = kvadrat
    elif opcija == "k":
        funkcija = exit(0)
    else:
        print("nepodprta operacija!")
        continue

    A = int(input("vnesi a:"))
    B = int(input("vnesi b:"))

    funkcija(A,B)

