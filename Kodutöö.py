'''
def maailm():
    print('Tere, maailm!')

maailm()

def liblikas():
    aasta = 2020
    liblikas = "teelehe-mosaiiklivlikas"
    lause_keskosa = ". aasta liblikas on "
    lause = str(aasta)+lause_keskosa+liblikas
    print(lause)
liblikas()

def pilved(a):
    if a > 6:
        print("Need on ülemised pilved")
    else:
        print("Need ei ole ülemised pilved")
        
a = float(input("Sisestage pilvede aluse kõrgus: "))

pilved(a)
'''
'''
inimesed=int(input("Sisesta inimeste arv: "))
kohad=int(input("Sisesta kohtade arv bussis: "))

if inimesed%kohad==0:
    bussid=inimesed//kohad
    viimases=kohad
else:
    bussid=inimesed//kohad+1

print(f"Busse vaja:{Bussid}\nviimases bussis inimesi")
'''


import random

taringud = int(input("Sisestage täringute arv: "))

for i in range(taringud):
    print(random.randint(1,6))
    
    