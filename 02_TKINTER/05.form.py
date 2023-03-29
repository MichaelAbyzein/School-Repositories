from tkinter import Tk, Label, Entry, Button, StringVar, Frame, Radiobutton
from tkinter.ttk import Combobox
import calendar
from datetime import datetime

window = Tk()
window.title("Form Pendaftaran Siswa")
window.geometry("300x400")

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

title = Label(window, text="Ignatius Global School")
title.grid(row=0, column=0, columnspan=2, sticky="nsew")

name_label = Label(window, text="Name Lengkap")
name_label.grid(row=1, column=0, sticky="w")

name_var = StringVar()
name_entry = Entry(window, textvariable=name_var)
name_entry.grid(row=1, column=1, sticky="nsew")

origin_label = Label(window, text="Sekolah Asal")
origin_label.grid(row=2, column=0, sticky="w")

origin_var = StringVar()
origin_entry = Entry(window, textvariable=origin_var)
origin_entry.grid(row=2, column=1, sticky="nsew")

birthplace_label = Label(window, text="Tempat Lahir")
birthplace_label.grid(row=3, column=0, sticky="w")

birthplace_var = StringVar()
birthplace_entry = Entry = Entry(window, textvariable=birthplace_var)
birthplace_entry.grid(row=3, column=1, sticky="nsew")

birthdate_label = Label(window, text="Tanggal Lahir")
birthdate_label.grid(row=4, column=0, sticky="w")

birthdate_frame = Frame(window)
birthdate_frame.grid(row=4, column=1, sticky="nsew")

day_var = StringVar()
day_combobox = Combobox(birthdate_frame, width=3, textvariable=day_var)
day_combobox["values"] = list(range(1, 32))
day_combobox.current(datetime.now().day-1)
day_combobox.grid(row=0, column=0, sticky="nsew")

month_var = StringVar()
month_combobox = Combobox(birthdate_frame, width=15, textvariable=month_var)
month_combobox["values"] = list(calendar.month_name)[1:13]
month_combobox.current(datetime.now().month-1)
month_combobox.grid(row=0, column=1, sticky="nsew")

year_var = StringVar()
year_combobox = Combobox(birthdate_frame, width=5, textvariable=year_var)
year_combobox["values"] = list(range(1910, 2041))
year_combobox.current(datetime.now().year-1910)
year_combobox.grid(row=0, column=2, sticky="nsew")

jk_label = Label(window, text="Jenis Kelamin")
jk_label.grid(row=5, column=0, sticky="w")

jk_frame = Frame(window)
jk_frame.grid(row=5, column=1, sticky="nsew")

jk_var = StringVar()
jk_var.set("m")

maleRb = Radiobutton(jk_frame, text="Laki-Laki", variable=jk_var, value="m")
maleRb.grid(row=0, column=0, sticky="nsew")

femaleRb = Radiobutton(jk_frame, text="Perempuan", variable=jk_var, value="f")
femaleRb.grid(row=0, column=1, sticky="nsew")

save_btn = Button(window, text="Save Data")
save_btn.grid(row=6, column=0, columnspan=2)

window.mainloop()