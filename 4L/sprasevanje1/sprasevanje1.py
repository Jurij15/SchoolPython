import tkinter as tk
from tkinter import messagebox

def dolzina():
    niz1=vnos1.get()
    if niz1=="":
        messagebox.showerror("Napaka", "Vnesi oba niza")
    rezultat = str(len((niz1).lower()))
    rezultat_label.config(text=rezultat)

def velikeCrke():
    niz1=vnos1.get()
    if niz1=="":
        messagebox.showerror("Napaka", "Vnesi oba niza")
    rezultat = (str(niz1)).upper()
    rezultat_label.config(text=rezultat)

def steviloSamoglasnikov():
    niz1=vnos1.get()
    if niz1=="":
        messagebox.showerror("Napaka", "Vnesi oba niza")
    rezultat = 0

    samoglasniki = "AEIOUaeiou"

    for i in range(len(niz1)):
        if niz1[i] in samoglasniki:
            rezultat +=1

    rezultat_label.config(text=str(rezultat))

def primerjaj():
    niz1=vnos1.get()
    niz2=vnos2.get()
    if niz1=="":
        messagebox.showerror("Napaka", "Vnesi oba niza")
    rezultat = str(niz1==niz2)
    rezultat_label.config(text=rezultat)

def obrat():
    niz1=vnos1.get()
    if niz1=="":
        messagebox.showerror("Napaka", "Vnesi oba niza")
    rezultat = niz1[::-1]

    rezultat_label.config(text=rezultat)

okno = tk.Tk()
okno.title("Obdelovanje crk")
okno.geometry("600x600")

#vnos 1
tk.Label(okno, text="Prvi niz").pack()
vnos1=tk.Entry(okno)
vnos1.pack()

#vnos 2
tk.Label(okno, text="drugi niz").pack()
vnos2=tk.Entry(okno)
vnos2.pack()

#gumb
tk.Button(okno, text="Dolzina niza", command=dolzina).pack()
tk.Button(okno, text="Velike crke", command=velikeCrke).pack()
tk.Button(okno, text="Stevilo samoglasnikov", command=steviloSamoglasnikov).pack()
tk.Button(okno, text="primerjaj", command=primerjaj).pack()
tk.Button(okno, text="Obrat", command=obrat).pack()

#rezultat
rezultat_label=tk.Label(okno, text="rezultat niz")
rezultat_label.pack()

okno.mainloop()