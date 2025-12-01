stevila = []

izvajanje = True;
while izvajanje:
    vnos = input("Vnesi stevilo ali KONEC: ")
    if(vnos == "KONEC"):
        izvajanje = False
    else:
        stevila.append(int(vnos))

sum = 0
for i in stevila:
    sum += i

print("povprecje "+ sum/len(stevila))