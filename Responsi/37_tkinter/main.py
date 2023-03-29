from tkinter import Tk, Label, Button, Entry, StringVar, Radiobutton, Frame
from tkinter.ttk import Combobox
import os #wait, why is this here?

def trig():
	print(a_var.get())


window = Tk()
window.title("Hey, I'm on TV!")
window.geometry("350x350") # must string (widthxheight)

my_label = Label(window, text="Hey Dad!") # Label(lokasi[window], text=...)
my_label.grid(row=0, column=0, sticky="esnw") #atas kiri [0][1]
#row and column can't skipped... my creativity has been ruined!

label_num = Label(window, text="Your Credit Card PIN")
label_num.grid(row=1, column=0)

label_mood = Label(window, text="Mood")
label_mood.grid(row=2, column=0)

my_frame = Frame(window)
my_frame.grid(row=2, column=1)

a_var = StringVar()
my_entry = Entry(window, textvariable=a_var) # alt name: a text box
my_entry.grid(row=0, column=1)

acombobox = Combobox(window, width=15)
acombobox["values"] = list(range(1000, 10000))
acombobox.current(694)
acombobox.grid(row=1, column=1)

my_button = Button(window, text="Goodbye", command=trig) # how you can't be not knowing about it
my_button.grid(row=2, column=0, columnspan=10)

my_mood = StringVar()
mood_sad = Radiobutton(my_frame, text=":(", variable=my_mood, value="sad")
mood_sad.grid(row=0, column=0, sticky="nesw")

mood_happ = Radiobutton(my_frame, text=":)", variable=my_mood, value="happy")
mood_happ.grid(row=0, column=1, sticky="nesw")
# note to self: sharing is caring... (lol)

window.mainloop()
#This ^ (= run())