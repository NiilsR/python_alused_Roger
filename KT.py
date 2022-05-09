# KT
# Roger Niils
# 27.04.22

def kassid(a):
    
    fail = open("felix.txt")
    pikkusk = 0
    sabad = 0
    kogus = 0
    for b in fail:
        
        b = b.strip()
        nimi, varv, pikkus = b.split(" ")
        
        if varv == a:
            pikkusk += int(pikkus)
            kogus += 1
    sabad = pikkusk // kogus
    return sabad
        

kassvarv = input("Sisestage siia kassi värvi mida tahate: ")
if kassid(kassvarv) != 0:
    print(f"Selle kassi värvi keskmine saba pikkus on {kassid(kassvarv)} cm.")
else:
    print("Sellist kassi värvi ei ole.")
