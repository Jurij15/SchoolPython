import tkinter as tk
from tkinter import messagebox

def besede():
    niz1=vnos1.get()
    if niz1=="":
        messagebox.showerror("Napaka", "Vnesi oba niza")
    besede = niz1.split(" ")
    rezultat_label.config(text=str(len(besede)))

def velikeCrke():
    niz1=vnos1.get()
    if niz1=="":
        messagebox.showerror("Napaka", "Vnesi oba niza")
    rezultat = (niz1).upper()
    rezultat_label.config(text=rezultat)

def stetje():
    niz1=vnos1.get()
    if niz1=="":
        messagebox.showerror("Napaka", "Vnesi oba niza")
    rezultat = str(len((niz1).replace(" ", "")))
    rezultat_label.config(text=rezultat)

okno=tk.Tk()
okno.title("Delo z nizi")
okno.geometry("600x600")

#vnos 1
tk.Label(okno, text="besedilo").pack()
vnos1=tk.Entry(okno)
vnos1.pack()

#gumb
tk.Button(okno, text="prestej besede", command=besede).pack()
tk.Button(okno, text="Velike crke", command=velikeCrke).pack()
tk.Button(okno, text="prestej crke", command=stetje).pack()

#rezultat
rezultat_label=tk.Label(okno, text="rezultat niz")
rezultat_label.pack()

okno.mainloop()