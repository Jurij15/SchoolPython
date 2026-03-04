#Naloga 2
# V kodo dodaj kroglico,
# V kdoo dodaj animacijo, da se kroglica odbija od konca do konca ekrana


import tkinter as tk

# Definicija globalnih spremenljivk
SIRINA = 400
VISINA = 300

hitrost_x = 4
hitrost_y = 5

# Ustvari okno in platno
okno = tk.Tk()
okno.title("Žogica")

platno = tk.Canvas(okno, width=SIRINA, height=VISINA, bg="black")
platno.pack()

#zogica = platno.create_oval

# Določi animacijo
#def animacija():

# Zaženi animacijo
animacija()
okno.mainloop()
