# napiši podprogram, ki bo našel najdaljšo besedo v tabeli z uporabo rekurzije

besede = ["pomaranca", "banana", "hruska", "kivi", "breskev"]


def najdaljsa_beseda(t):
    if len(t) == 1:
        return t[0]  # če tabela vsebuje samo eno besedo, vrne prvo
    else:
        # v prvem rekurzivnem koraku preverja prvo besedo v tabeli s preostalim delom table, ki ga obravnavamo rekurzivno
        trenutna_beseda = t[0]
        preostale_besede = najdaljsa_beseda(t[1:])

        # če je trenutna beseda daljša, jo vrne, če ne pa vrne najdaljšo besedo iz preostale table
        if (len(trenutna_beseda) > len(preostale_besede)):
            return trenutna_beseda
        else:
            return preostale_besede


print(najdaljsa_beseda(besede))