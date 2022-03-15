from tkinter import *

#akna seaded
aken = Tk()
aken.title("Grand Theft Auto 6")
aken.resizable(0, 0)
aken.configure(background='black')

#tekst
Label(aken, text="Nimi: Roger Niils", font="Tahoma 16 bold italic", foreground="red", background="black", pady=10, padx=30).pack()
Label(aken, text="Rühm: IT21", font="Tahoma 16 bold italic", foreground="red", background="black", pady=10, padx=30).pack()
Label(aken, text="2022", font="Tahoma 16 bold italic", foreground="red", background="black", pady=10, padx=30).pack()
aken.mainloop()