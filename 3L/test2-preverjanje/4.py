class Dijak:
    def __init__(self, ime, starost):
        self.__ime = ime
        self.__starost = starost

    def get_ime(self):
        return self.__ime
    def get_starost(self):
        return self.__starost

    def set_ime(self, ime):
        self.__ime = ime
    def set_starost(self, starost):
        self.__starost = starost

    def predstavi_se(self):
        print("Sem ", self.__ime, " in imam ", self.__starost, " let")

dijak1 = Dijak("Ana", 22)
dijak1.predstavi_se()
dijak1.set_ime("Tina")
dijak1.predstavi_se()
dijak1.set_starost(23)
dijak1.predstavi_se()