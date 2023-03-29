from tkinter import Tk, Label, Button, Entry, StringVar

window = Tk()
window.title("Using Lambda")
window.geometry("300x400")

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

window.grid_rowconfigure(0, weight=3)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)

title = Label(window, text="This title will be change!")
title.grid(row=0, column=0, columnspan=2, sticky="nsew") #nsew = north south east west

label_entry = Label(window, text="input here")
label_entry.grid(row=1, column=0, sticky="w")

entry_var = StringVar()
entry = Entry(window, textvariable=entry_var)
entry.grid(row=1, column=1, sticky="nsew")

#fg = foreground
#command = arg untuk binding dengan function (def/lambda)

button = Button(window, text="change", font=("Comic Sans MS", 14), fg="pink",command=lambda : title.configure(text=entry_var.get()))
button.grid(row=2, column=0, columnspan=2, sticky="nsew")

window.mainloop()