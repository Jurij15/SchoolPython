class Papagaj:
    def __init__(self, ime,barva,starost):
        self.ime = ime
        self.barva = barva
        self.starost = starost
        self.__hrana = 5

    def nahrani(self, kolicina):
        self.__hrana += 1
    def prikazi_hrano(self):
        return self.__hrana