from tkinter import Tk, Label, Entry, Button, StringVar


window = Tk()
window.title("WOW, The Title Work")
window.geometry("500x500")

title = Label(window, text="Login")
title.grid(row=0, column=0, columnspan=2)

sub_title = Label(window, text="Masuk ke Aplikasi")
sub_title.grid(row=1, column=0, columnspan=2)

username_label = Label(window, text="Username:")
username_label.grid(row=3, column=0)

username_entry = Entry(window)
username_entry.grid(row=3, column=1)

password_label = Label(window, text="Password:")
password_label.grid(row=5, column=0)

password_entry = Entry(window)
password_entry.grid(row=5, column=1)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

window.mainloop()