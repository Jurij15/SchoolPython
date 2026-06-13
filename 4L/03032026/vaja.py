import tkinter as tk
from tkinter import messagebox

def sestej():
    global stevilo1, stevilo2

    if (stevilo1.get() == "") or (stevilo2.get() == ""):
        messagebox.showerror("Napaka","Vnesi podatke!")
        return
    elif (int(stevilo1.get()) == 0) or (int(stevilo2.get())== 0):
        messagebox.showerror("Napaka","Vnesi podatke!")
        return

    sestevek = (int(stevilo1.get())) + (int(stevilo2.get()))

    result.config(text= sestevek)

def odstej():
    global stevilo1, stevilo2

    if (stevilo1.get() == "") or (stevilo2.get() == ""):
        messagebox.showerror("Napaka","Vnesi podatke!")
        return
    elif (int(stevilo1.get()) == 0) or (int(stevilo2.get())== 0):
        messagebox.showerror("Napaka","Vnesi podatke!")
        return

    sestevek = (int(stevilo1.get())) - (int(stevilo2.get()))

    result.config(text= sestevek)

def zmnozi():
    global stevilo1, stevilo2

    if (stevilo1.get() == "") or (stevilo2.get() == ""):
        messagebox.showerror("Napaka","Vnesi podatke!")
        return
    elif (int(stevilo1.get()) == 0) or (int(stevilo2.get())== 0):
        messagebox.showerror("Napaka","Vnesi podatke!")
        return

    sestevek = (int(stevilo1.get())) * (int(stevilo2.get()))

    result.config(text= sestevek)

def deli():
    global stevilo1, stevilo2

    if (stevilo1.get() == "") or (stevilo2.get() == ""):
        messagebox.showerror("Napaka","Vnesi podatke!")
        return
    elif (int(stevilo1.get()) == 0) or (int(stevilo2.get())== 0):
        messagebox.showerror("Napaka","Vnesi podatke!")
        return

    if(stevilo2.get() == "0"):
        return

    sestevek = (int(stevilo1.get())) / (int(stevilo2.get()))

    result.config(text= sestevek)

# Ustvari okno, okvir in platno
okno = tk.Tk()
okno.title("Okno")
okno.geometry("800x240")

stevilo1 = tk.StringVar()
stevilo2 = tk.StringVar()

text1 = tk.Entry(okno, textvariable=stevilo1)
text1.grid(row=0, column=0)
text2 = tk.Entry(okno, textvariable=stevilo2)
text2.grid(row=1, column=0)

result = tk.Label(okno)
result.grid(row=2, column=0)

sbutton = tk.Button(okno, text="Sestej", command = sestej, width=20)
obutton = tk.Button(okno, text="Odstej", command = odstej, width=20)
zbutton = tk.Button(okno, text="Zmnozi", command = zmnozi, width=20)
dbutton = tk.Button(okno, text="Deli", command = deli, width=20)
sbutton.grid(row=3, column=0)
obutton.grid(row=3, column=1)
zbutton.grid(row=3, column=2)
dbutton.grid(row=3, column=3)

# Zaženi dogodkovno zanko
okno.mainloop()