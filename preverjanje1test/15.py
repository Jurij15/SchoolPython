class Oseba:
    def __init__(self, ime):
        self.ime = ime

a = Oseba("Ana")
b = a
b.ime ="Ema"
print(a.ime)

"""
a in b nista kopiji - obe spremenljivki se sklicujeta na isti objekt v kopici
podobno kazalcem v c, ampak varno:
    brez deferencijranja NULL
    ni ročnega brisanja
    ni nevarnosti poškodbe pomnilnika
"""