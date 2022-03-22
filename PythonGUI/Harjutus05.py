from tkinter import *

def arvutamine():
    protsent=int(var.get())
    kokku=int(sisestus.get())
    kokku2 = kokku/100*protsent
    kokku3 = kokku2 + kokku
    print(kokku2)
    print(kokku3)
    valjund.config(text=kokku2)
    valjund1.config(text=kokku3)
    
    
aken = Tk()
aken.title('Käibemaksukalkulaator')
aken.geometry("350x200")

silt = Label(aken, text="Hind käibemaksuta:")
silt.grid(row=0,column=0)


sisestus = Entry(aken)
sisestus.grid(row=0,column=1)


nupp1 = Button(aken, text="Arvuta", width=10, command=arvutamine)
nupp1.grid(row=3, column=1)

def naita_valikut():
    print(var.get())

var = IntVar()
valikukast = Radiobutton(aken,text="9%", variable=var, value=9, command=naita_valikut)
valikukast.grid(row=1,column=1)
valikukast = Radiobutton(aken,text="20%", variable=var, value=20, command=naita_valikut)
valikukast.grid(row=2,column=1)

jah = Label(aken, text="---------------------------------------------")
jah.grid(row=4,columnspan=3)
valjund = Label(aken, text="")
valjund.grid(row=5,column=1)
valjund1 = Label(aken, text="")
valjund1.grid(row=6,column=1)
valjund2 = Label(aken, text="Siia tuleb käibemaks: ")
valjund2.grid(row=5,column=0)
valjund3 = Label(aken, text="Hind käibemaksuga: ")
valjund3.grid(row=6,column=0)





aken.mainloop()