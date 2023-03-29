from tkinter import Tk, Frame

window = Tk()
window.title("A Lot Of Column")
window.geometry("300x400")

frame0 = Frame(window, bg="yellow")
frame0.grid(row=0, column=0, columnspan=2, sticky="nsew")

frame1 = Frame(window, bg="black")
frame1.grid(row=1, column=0, sticky="nsew")

frame2 = Frame(window, bg="red")
frame2.grid(row=2, column=0, rowspan=4, sticky="nsew")

frame3 = Frame(window, bg="lime")
frame3.grid(row=1, column=1, rowspan=6, sticky="nsew")

window.grid_rowconfigure(0, weight=2)
window.grid_rowconfigure(1, weight=2)
window.grid_rowconfigure(2, weight=5)

window.grid_columnconfigure(0, weight=2)
window.grid_columnconfigure(1, weight=1)

window.mainloop()