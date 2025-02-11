class Papagaj():
    def __init__(self, ime):
        self.ime = ime

    def govori(self):
        return "Čiv Čav"


class Ara():
    def __init__(self, ime):
        self.ime = ime

    def govori(self):
        return "Ara pravi: Pozdrav"


class Kakadu():
    def __init__(self, ime):
        self.ime = ime

    def govori(self):
        return "Kakadu pravi: Hej, prijatelj!"

def oglasi_se(papiga):
    return papiga.govori()