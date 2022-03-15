# Roger Niils
# Harjutus07
# 16.02.22

# ruumala

import math 
      
def kuup(a):
    v = a*a*a
    return v
        
def kera(r):
    v = (4*math.pi*r**3)/3
    return v
        
def koonus(r,h):
    v = (1/3*math.pi*r**2*h,2)
    return v
        
def silinder(r,h):
    v = (math.pi*r**2*h,2)
    return v
           
loop = 1
while loop == 1:
    kujund = int(input("Vali kujund: \n 1 Kuup \n 2 Kera \n 3 Koonus \n 4 Silinder \n 5 Exit \n Valik:"))
    

    if kujund == 1:
        a = int(input("Valisid kuubi. Sisesta kuubi külg: "))
        v = kuup(a)
        print("Vastus: ",v)
    elif kujund == 2:
        r = int(input("Valisid kera. Sisesta kera raadius: "))
        v =kera(r)
        print("Vastus: ",v)
    elif kujund == 3:
        r = int(input("Valisid koonuse. Sisesta koonuse raadius: "))
        h = int(input("Sisesta koonuse kõrgus: "))
        v = koonus(r,h)
        print("Vastus: ",v)
    elif kujund == 4:
        r = int(input("Valisid silindri. Sisesta silindri raadius: "))
        h = int(input("Sisesta silindri kõrgus: "))
        v = silinder(r,h)
        print("Vastus: ",v)
    else:
        print("Exit")
        loop = 0



# tervita

'''
nimi = input("Sisestage nimi: ")
keel = input("Sisestage enda keel et,en,de : ")

def tervita(n,k="de"):
    if k == "en":
        print("Hello", nimi)
    elif k == "et":
        print("Tere", nimi)
    elif k == "de":
        print("Hallo", nimi)  
    
tervita(nimi,keel)
'''