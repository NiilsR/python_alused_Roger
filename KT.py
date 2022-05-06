# KT
# Roger Niils
# 10.03.22

def kass1(a):

fail = open("felix.txt")
pikkus = 0
sabad = 0
for a in fail:
    a = a.strip()
    nimi, varv, pikkus = a.split(" ")
    
    if varv == varvinimi:
        pikkus += int(pikkus)
        kogus += 1
        
    if sabad == 0:
        sabad = 1
    sabapikkus = pikkus // sabad
    return sabapikkus

kassvarv = input("Sisestage siia kassi värvi mida tahate: ")
if kassid(kassvarv) != 0:
    print("Selle kassi värvi keskmine saba pikkus on {kassid(kassvarv)} cm.")
else:
    print("Sellist kassi värvi ei ole.")