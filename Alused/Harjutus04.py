# Harjutus04
# Roger Niils
# 03.02.22

'''
# ruutude ja kuupide tabel

print("   Arv | Ruut | Kuup")
for d in range(1,11):
    print(f" {d:6}|{d*d:6}|{d*d*d:6}")
'''
'''
# pank

raha = 10000
intress = 0.05
aastad = 5
konto = 0
konto += raha

for i in range(aastad):
    kasum = intress*konto
    print(konto,kasum,konto+kasum)
    konto += kasum
'''
'''
# arvamismäng

import random
kord = 0
loop = 1
suvnr = random.randint(1, 11)
while loop == 1:
    if kord == 2:
        loop = 0
    tasku = int(input("Sisesta arv 1-10 "))
    kord +=1
    if tasku == suvnr:
        print("tubli")
        loop = 0
    else:
        print("ei arvand")
'''
'''
# viisikud

for i in range(1,101):
    if i % 5 == 0:
        print(i)
'''
    
'''
# korrutustabel

number = 5

for i in range(1, 10):
    print(number, 'x', i, '=', number*i)
'''

'''
# paaris ja paaritu

number = input("Sisesta enda number: ",)
if int(number) % 2 == 0:
    print("{0} on paaris".format(number))
else:
    print("{0} on paaritu".format(number))
'''

'''
# loto

import random
suvalinenr = random.randint(10000,99999)
print(f"Siin on sinu suvaline number: {suvalinenr}")
'''

'''
# tärnid

for i in range(1,6):
    for j in range(1,6):
        print('* ', end='')
    print()
print("-----------------------------")
for k in range(0,5):
    for l in range(0, k+1):
        print ('*', end='')
    print()
print("-----------------------------")
for m in range(5,0,-1):
    for n in range(0,m):
        print('*', end='')
    print()
'''

'''
# jalgpall

sugu = input("Sisesta sugu: ")
if sugu == "mees":
    vanus = int(input("Sisesta vannus: "))
    if vanus >=16 and vanus <=18:
        print("Olete sobilik")
'''
'''
# müük
hind = int(input("Toote hind: "))
if hind <= 10:
    hind = hind * 0.9
else:
    hind = hind * 0.8
    
print(f"Toote hind on {hind}€")
'''

'''
# juubel
# kasutaja sisestab oma sünnipäeva ja programm ütleb, kas on juubel või ei.
sunnipaev = input("Sisesta enda sünnipäev: ",)
if int(sunnipaev) % 10 == 0:
    print("On juubel")
else:
    print("Ei ole juubel")
'''

'''
#matemaatika
arv1 = int(input("Sisesta mingi arv: "))
tehe = input("Sisestage mingi tehe (+,-,*,/)")
arv2 = int(input("Sisesta mingi arv: "))
if tehe == "+":
    v = arv1+arv2
elif tehe == "-":
    v = arv1-arv2
elif tehe == "*":
    v = arv1*arv2
else:
    v = arv1/arv2
print(f'{arv1}{tehe}{arv2}={v}')
'''

'''
#Ruudu kontroll == > < >= !=
a = int(input("Sisesta ruudu üks külg: "))
b = int(input("Sisesta ruudu teine külg: "))
if a == b:
    print("Tegemist on ruuduga")
elif:
# kirjutad siia veel midagi
else:
    print("Risttahukas")
'''