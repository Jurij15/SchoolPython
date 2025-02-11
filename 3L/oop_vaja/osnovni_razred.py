class Papagaj:
    def __init__(self, ime,barva,starost):
        self.ime = ime
        self.barva = barva
        self.starost = starost

    def govori(self, besedilo):
        return self.ime+"pravi: "+besedilo
    def leti(self):
        return self.ime+"veselo leti po prostoru"

papagaj1= Papagaj("Koki", "zelen", 15)

print(papagaj1.govori("kekec"))
print(papagaj1.leti())

ime = input("vnesi ime: ")
barva = input("vnesi ime: ")
starost = int(input("vnesi starost: "))
beseda = input("vnesi besedo: ")
papagaj2 = Papagaj(ime,barva,starost)
print(papagaj2.govori(beseda))
print(papagaj2.leti())