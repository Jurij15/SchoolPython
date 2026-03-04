#Naloga 1
# V kodo spodaj dodaj prikaz teksta (lahko je preprost label ali pa canvas), na katerem se bo prikazovalo število trenutnih klikov.
# Dodaj tudi tipko, ki bo ob kliku povečala število.
# Ko se število poveča, naj se poveča tudi velikost fonta teksta.
# Če je število deljivo z 10, naj se barva besedila spremeni v rdeče, če ne naj je modra


import tkinter as tk

# Definicija globalnih spremenljivk
SIRINA = 400
VISINA = 300

hitrost_x = 4
hitrost_y = 5

# Ustvari okno in platno
okno = tk.Tk()
okno.title("Žogica")

#platno = tk.Canvas()
#platno.pack()

#zogica = platno.create_oval

# Določi animacijo
def animacija():
    global hitrost_x, hitrost_y

    platno.move(zogica, hitrost_x, hitrost_y)
    #polozaj = =?

    if polozaj[3] >= VISINA or polozaj[1] <= 0:
        hitrost_y = -hitrost_y

    if polozaj[2] >= SIRINA or polozaj[0] <= 0:
        hitrost_x = -hitrost_x

    #okno.after(?)

# Zaženi animacijo
animacija()
okno.mainloop()
