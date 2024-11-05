#V datoteki imena.txt so imena, vsako v svoji vrstici
#napisi program, ki prebere vsa imena iz te datoteke
#Imena, ki se zacnejo z crkami A-M, zapisi v datoteko _A_M.txt
#Imena, ki se zacnejo z crkami N-Z, zapisi v datoteko _N_z.txt

am = []
nz = []

with open("imena.txt", "r") as file:
    vrstice = file.readlines()

    for i in vrstice:
        if i[0] < "M":
            am.append(i.strip())
        if i[0] > "M":
            nz.append(i.strip())

print(am)
print(nz)