#naloga a)
with open("temperature.txt", "w") as datoteka:
    datoteka.write("15\n")
    datoteka.write("17\n14\n19\n21\n20\n16")

#naloga b)
with open("temperature.txt", "r") as datoteka:
    vrstice= datoteka.readlines() #vrstice = [15,17,14,19,21,20,16] #vsak podatek je STRING (NIZ)

temp = []
for i in vrstice:
    temp.append( int(i.strip())) #lahko se doda tudi .strip(), ni pa nujno

#naloga c)
 n = 0
for i in range(len(temp)):
    n += temp[i]

povprecje = n/len(temp)

#lazji nacin
#povprecje = sum(temp)/len(temp)

#najvecje in najmanjse
najv = temp[0]
najm=temp[0]

for i in temp:
    if i > najv:
        najv = i
    elif i < najm:
        najm = i

#naloga d)
with open("analiza.txt", "w") as datoteka:
    datoteka.write(str(povprecje))
    datoteka.write("\n")
    datoteka.write(str(najv))
    datoteka.write("\n")
    datoteka.write(str(najm))
