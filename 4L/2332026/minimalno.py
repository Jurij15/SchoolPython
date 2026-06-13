#naredi graficno aplikacijo, ki:
#- ima 2 polji za vnos besedila
#- ima gumb zdruzi
#- izpise zdruzen niz (spajanje obeh nizov)
#- prikaze napako, ce uporabnik pusti prazno polje

import tkinter as tk
from tkinter import messagebox

def zdruzi():
    niz1=vnos1.get()
    niz2=vnos2.get()
    if niz1=="" or niz2=="":
        messagebox.showerror("Napaka", "Vnesi oba niza")
    rezultat = niz1+niz2
    rezultat_label.config(text=rezultat)

def velikeCrke():
    niz1=vnos1.get()
    niz2=vnos2.get()
    if niz1=="" or niz2=="":
        messagebox.showerror("Napaka", "Vnesi oba niza")
    rezultat = (niz1+niz2).upper()
    rezultat_label.config(text=rezultat)

def maleCrke():
    niz1=vnos1.get()
    niz2=vnos2.get()
    if niz1=="" or niz2=="":
        messagebox.showerror("Napaka", "Vnesi oba niza")
    rezultat = (niz1+niz2).lower()
    rezultat_label.config(text=rezultat)

def stetje():
    niz1=vnos1.get()
    niz2=vnos2.get()
    if niz1=="" or niz2=="":
        messagebox.showerror("Napaka", "Vnesi oba niza")
    rezultat = str(len((niz1+niz2).lower()))
    rezultat_label.config(text=rezultat)

okno=tk.Tk()
okno.title("Delo z nizi")
okno.geometry("600x600")

#vnos 1
tk.Label(okno, text="prvi niz").pack()
vnos1=tk.Entry(okno)
vnos1.pack()

#vnos 1
tk.Label(okno, text="drugi niz").pack()
vnos2=tk.Entry(okno)
vnos2.pack()

#gumb
tk.Button(okno, text="Zdruzi", command=zdruzi).pack()
tk.Button(okno, text="Velike crke", command=velikeCrke).pack()
tk.Button(okno, text="Mlae crke", command=maleCrke).pack()
tk.Button(okno, text="stetje crk", command=stetje).pack()

#rezultat
rezultat_label=tk.Label(okno, text="rezultat niz")
rezultat_label.pack()

okno.mainloop()