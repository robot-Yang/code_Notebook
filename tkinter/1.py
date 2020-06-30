from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

lbl = Label(window, text="Hello")

lbl.grid(column=0, row=0)

txt = Entry(window,width=10)

txt.grid(column=1, row=0)

txt.focus()

# txt = Entry(window,width=10, state='disabled') # To disable entry widget, you can set the state property to disabled:

def clicked():

    res = "Welcome to " + txt.get()

    lbl.configure(text= res)

btn = Button(window, text="Click Me", command=clicked)

btn.grid(column=2, row=0)

window.mainloop()