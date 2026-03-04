# napiši program, ki ima pogovorno okno dimenzije 600x300. V pogovornem oknu naj se izpiše besedilo pozdravljen.
# oknu dodaj gumb z napisom "klikni". Ob kliku z miško na ta gumb naj se izpiše tvoje ime.
# Besedilo pozdravljen naj bo zelene barve, po kliku pa rdeče.

import tkinter as tk

gumbBesedilo = "Klikni"
barva = "green"
stevec = 0


def klik():
    global barva
    global gumbBesedilo
    global stevec

    barva = "red"
    stevec += 1
    gumbBesedilo = "Jure Jurij Grom"

    button.config(text=gumbBesedilo)
    label.config(fg=barva, text="Bravo! Stevilo klikov: "+str(stevec))


okno = tk.Tk()
okno.title("vaja")
okno.geometry("600x300")

label = tk.Label(okno, text="Pozdravljen", fg=barva)
label.pack()

button = tk.Button(okno, text=gumbBesedilo, width=25, command=klik)
button.pack()

okno.mainloop()