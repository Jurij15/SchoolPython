#simulacija meta kocke
#izpis stevila metov
#rezultati metov v tabeli

import random

def metKocke():
    return random.randint(1,6)

def simulacijaMetaKocke(n):
    metiKocke = []

    for i in range(steviloMetov):
        metiKocke.append(metKocke())

    return metiKocke

steviloMetov = int(input("Vnesi stevilo metov kock: "))

print("Rezultati:")
print(simulacijaMetaKocke(steviloMetov))