class Zaposleni:
    def __init__(self, ime, priimek, placa):
        self.ime = ime
        self.priimek = priimek
        self.placa = placa

    def predstavi_se(self):
        print(self.ime, " ",self.priimek, " ",self.placa)

class Tehnik(Zaposleni):
    def __init__(self, ime, priimek, placa, specializacija):
        super().__init__(ime, priimek, placa)
        self.specializacija=specializacija

    def predstavi_se(self):
        super().predstavi_se()
        print("Specializiran sem za ",self.specializacija)

    def bonus(self):
        print("Imam bonus: ", self.placa*0.10)

zaposleni1 = Zaposleni("Janez", "Novak", 1500)
tehnik1 = Tehnik("Bojan", "Kovač", 2500, "računalniški inženiring")

zaposleni1.predstavi_se()
tehnik1.predstavi_se()
tehnik1.bonus()
