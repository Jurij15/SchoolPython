#najdaljsa beseda v datoteki

with open("besede.txt", "w") as file:
    file.write("jabolko\n")
    file.write("pomaranca\n")

with open("besede.txt", "r") as file:
    besede = []
    for line in file:
        besede.append(line)
        
naj=besede[0]

for beseda in besede:
    if len(beseda)>len(naj):
        naj = beseda
        
dolzina = len(naj)
with open("analiza.txt", "w"):
    file.write(naj,dolzina)