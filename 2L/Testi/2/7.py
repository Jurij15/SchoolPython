def OdmotajPrepleteneCrke(niz):
    velikeCrke = ""
    maleCrke = ""

    for c in niz:
        if c.isupper():
            velikeCrke = velikeCrke + c
        else:
            maleCrke = maleCrke + c

    return  velikeCrke+maleCrke

vnos = input("vnesi besedilo: ")
print(OdmotajPrepleteneCrke(vnos))