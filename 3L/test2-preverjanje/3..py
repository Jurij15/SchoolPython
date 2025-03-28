class Vozilo:
    def __init__(self, hitrost):
        self.hitrost = hitrost

class Avto(Vozilo):
    def __init__(self, hitrost, stevilo_vrat):
        super().__init__(hitrost)
        self.stevilo_vrat = stevilo_vrat

    def premik(self):
        print("Avto se premika s hitrostjo ",self.hitrost, " km/h")

class Kolo(Vozilo):
    def __init__(self, hitrost, tip):
        super().__init__(hitrost)
        self.tip = tip

    def premik(self):
        print("Koloo tipa ", self.tip, " se premika s hitrostjo ", self.hitrost, " km/h")

class Tovornjak(Vozilo):
    def __init__(self, hitrost, nosilnost):
        super().__init__(hitrost)
        self.nosilnost = nosilnost

    def premik(self):
        print("Tovornjak se premika s hitrostjo ", self.hitrost, " in lahko nosi ", self.nosilnost, " ton.")

avto1 = Avto(120, 4)
kolo1 = Kolo(25, "Gorsko")
tovornjak1 = Tovornjak(90, 10)

avto1.premik()
kolo1.premik()
tovornjak1.premik()