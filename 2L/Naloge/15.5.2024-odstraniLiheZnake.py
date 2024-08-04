def odstraniLihZnake(niz):
    res = ""
    for i in range(0, len(niz)):
        if i % 2 == 0:
            res += niz[i]

    return res

print(odstraniLihZnake(input("vnesi string ")))