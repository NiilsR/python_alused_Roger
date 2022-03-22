# Harjutus06

from tkinter import *

#akna seaded
aken = Tk()
aken.title('Joonistamine')

#lõuendi loomine
louend = Canvas(aken, width=500, height=500)
louend.pack()

#kujundite loomine
louend.create_rectangle(500, 260, 0, 0, fill='#C8102E', outline='#C8102E', width=4)
louend.create_rectangle(200, 0, 220, 260, fill='#FFFFFF', outline='#FFFFFF', width=4)
louend.create_rectangle(0, 100, 500, 120, fill='#FFFFFF', outline='#FFFFFF', width=4)

pilt = PhotoImage(file='denmark.png')
louend.create_image(0, 300, anchor=NW, image=pilt)

#teksti loomine
louend.create_text(350,50, text="Taani", fill="black", font=("Tahoma", 30))
aken.mainloop()

aken.mainloop()