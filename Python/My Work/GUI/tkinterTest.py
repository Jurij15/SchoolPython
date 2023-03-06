import tkinter as tk


def testbtn_click():
    print("test btn clicked!")


window = tk.Tk()
window.title("Test Window")
window.geometry("640x480")

label = tk.Label(window, text="Test Label")
label.pack()

button = tk.Button(window, text="Test", command=testbtn_click())
button.pack()

window.mainloop()
