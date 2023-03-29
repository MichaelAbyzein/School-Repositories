from tkinter import Tk, Label, Entry, Button

window = Tk()

label = Label(window, text="Never gonna give you up!")
label.grid()

entry = Entry(window)
entry.grid()

button1 = Button(window, text="da!")
button1.grid()

window.mainloop()