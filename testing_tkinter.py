from tkinter import *
from tkinter.ttk import *


def clicked():
    res = "welcome to " + txt.get()
    lbl.configure(text=res)

window = Tk()
window.title("This is a test app")
lbl = Label(window, text="hello", font=("Arial Bold", 20))
lbl.grid(column=0, row=0)
btn = Button(window, text="Click Me", bg="blue", command=clicked)
btn.grid(column=0, row=1)
txt = Entry(window, width=10)
txt.focus()
txt.grid(column=2, row=0)
window.geometry('350x200')
window.mainloop()
