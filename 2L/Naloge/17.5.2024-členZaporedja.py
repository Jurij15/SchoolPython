zaporedje = [1,1,1]

koncno = 0

for i in range (1,124):
    zaIzracun = zaporedje[-3:]

    izracun = 0
    for j in zaIzracun:
        izracun += int(j)

    zaporedje.append(izracun)
    #print(izracun)
    koncno = izracun

print(koncno)