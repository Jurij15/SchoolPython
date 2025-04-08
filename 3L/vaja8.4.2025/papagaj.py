import random

class Papagaj:
    def __init__(self, ime, barva, starost):
        self.ime = ime
        self.barva = barva
        self.starost = starost

    def govori(self, besedilo):
        print(self.ime , " pravi :", besedilo)
    def leti(self):
        print(self.ime , " veselo leti po prostoru")

class GovoreciPapagaj(Papagaj):
    def __init__(self, ime, barva, starost, besede):
        super().__init__(ime, barva, starost)
        self.besede = besede

    def dodaj_besedo(self, nova_beseda):
        self.besede.append(nova_beseda)

    def nakljucna_beseda(self):
        if len(self.besede) == 0:
            print(self.ime ," ne zna nobene besede!")
        else:
            #beseda = self.besede[random.randint(0,len(self.besede)-1)]
            beseda = random.choice(self.besede)
            print(self.ime, " pravi: ", beseda)

#ustvarjanje papagaja iz osnovnega razreda
papagaj1 = Papagaj("Koki", "moder", 2)
papagaj1.govori("Pozdravljen")
papagaj1.leti()

#ustvarjanje govorečega papagaja
papagaj2 = GovoreciPapagaj("Charlie", "zelen", 5, ["Živjo", "Kako si?", "Dober Dan!"])
papagaj2.nakljucna_beseda()
papagaj2.dodaj_besedo("Rad imam sonce")
papagaj2.nakljucna_beseda()