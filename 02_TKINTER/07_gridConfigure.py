from tkinter import Tk, Frame

window = Tk()
window.title("Belajar GridConfigure")
window.geometry("400x300")

frame4 = Frame(window, bg="green")
frame4.grid(row=0, column=1, sticky="nsew")

frame0 = Frame(window, bg="purple")
frame0.grid(row=0, column=0, sticky="nsew")

frame1 = Frame(window, bg="blue")
frame1.grid(row=1, column=0, columnspan= 2, sticky="nsew")

frame2 = Frame(window, bg="red")
frame2.grid(row=2, column=0, columnspan=2, sticky="nsew")

frame3 = Frame(window, bg="yellow")
frame3.grid(row=3, column=0, columnspan=2, sticky="nsew")

window.grid_rowconfigure(0, weight=6)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

window.mainloop()