
from tkinter import *

#akna seaded
aken = Tk()
aken.title('Kalkulaator')
aken.option_add('*font', ('tahoma', 12))
aken.geometry("200x200")
lab = Label(aken, text="Siia kunagi vastus!")
lab.grid(row=0,columnspan=5)
#nupud
nupp1 = Button(aken, text="8",width=4, padx=2)
nupp1.grid(row=1, column=1, padx=2)
nupp2 = Button(aken, text="7",width=4 ,padx=2)
nupp2.grid(row=1, column=0, padx=2)
nupp3 = Button(aken, text="4",width=4 ,padx=2)
nupp3.grid(row=2, column=0, padx=2)
nupp3 = Button(aken, text="1",width=4 ,padx=2)
nupp3.grid(row=3, column=0, padx=2)
nupp3 = Button(aken, text="0",width=4 ,padx=2)
nupp3.grid(row=4, column=0, padx=2)
nupp1 = Button(aken, text="5",width=4 ,padx=2)
nupp1.grid(row=2, column=1, padx=2)
nupp1 = Button(aken, text="2",width=4 ,padx=2)
nupp1.grid(row=3, column=1, padx=2)
nupp1 = Button(aken, text=",",width=4 ,padx=2)
nupp1.grid(row=4, column=1, padx=2)
nupp1 = Button(aken, text="9",width=4 ,padx=2)
nupp1.grid(row=1, column=2, padx=2)
nupp1 = Button(aken, text="6",width=4 ,padx=2)
nupp1.grid(row=2, column=2, padx=2)
nupp1 = Button(aken, text="3",width=4 ,padx=2)
nupp1.grid(row=3, column=2, padx=2)
nupp1 = Button(aken, text="=",width=4 ,padx=2)
nupp1.grid(row=4, column=2, padx=2)
nupp1 = Button(aken, text="/",width=4 ,padx=2)
nupp1.grid(row=1, column=3, padx=2)
nupp1 = Button(aken, text="*",width=4 ,padx=2)
nupp1.grid(row=2, column=3, padx=2)
nupp1 = Button(aken, text="-",width=4 ,padx=2)
nupp1.grid(row=3, column=3, padx=2)
nupp1 = Button(aken, text="+",width=4 ,padx=2)
nupp1.grid(row=4, column=3, padx=2)








aken.mainloop()