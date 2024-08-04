def najmanjsi(nizi = []):
    index = 0
    for i in  nizi:
        if len(i) < index:
            index = nizi.index(i)

    return  index

def najdaljsiTrijeNizi(nizi = []):
    najdaljsi  = []
    for i in nizi:
        if len(najdaljsi) != 3:
            najdaljsi.append(i)
            continue
        else:
            del najdaljsi[najmanjsi(najdaljsi)]
        for j in najdaljsi:
            if i > j or len(najdaljsi) != 3:
                najdaljsi.append(i)
                break

    return  najdaljsi

besede = []

counter = 1
while(counter < 20):
    besede.append(input("Vnesi besedo "+str(counter) + ": "))

print(najdaljsiTrijeNizi(besede))
