import random

class Papagaj:
    def __init__(self, ime,barva,starost):
        self.ime = ime
        self.barva = barva
        self.starost = starost

    def govori(self, besedilo):
        return self.ime+"pravi: "+besedilo
    def leti(self):
        return self.ime+"veselo leti po prostoru"

class GovoreciPapagaj(Papagaj):
    def __init__(self, ime,barva,starost, besede):
        super().__init__(ime,barva, starost)
        self.besede = besede

    def dodaj_besedo(self, nova_beseda):
        self.besede.append(nova_beseda)

    def nakljucna_beseda(self):
        return self.besede[random.randint(0,len(self.besede)-1)]



