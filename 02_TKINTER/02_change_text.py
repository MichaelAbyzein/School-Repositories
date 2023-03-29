from tkinter import Tk, Label, Entry, Button, StringVar

def change_text():
	label.configure(text=entry_variable.get())

window = Tk()

label = Label(window, text="Never gonna give you up!")
label.grid()

entry_variable = StringVar()
entry = Entry(window, textvariable=entry_variable)
entry.grid()

button1 = Button(window, text="da!", command=change_text)
button1.grid()

window.mainloop()