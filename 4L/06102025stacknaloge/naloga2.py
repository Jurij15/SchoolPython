def preveri_oklepaje(izraz):
    sklad = []
    par = {")":"(", "]":"[" , "}":"{"}

    for znak in izraz:
        if znak in "([{":
            sklad.append(znak)
        elif znak in ")]}":
            if not sklad or sklad[-1] != par[znak]:
                return False
            sklad.pop()
    return len(sklad) == 0

print(preveri_oklepaje("(asdf)"))