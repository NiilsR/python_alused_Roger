#Roger Niils
#Harjutus05
#10.02.22



'''
# tärnid

import random
arvud = []
for i in range(6):
    arvud.append(random.randint(1,20))
for n in range(len(arvud)):
    print("*"*arvud[n])
'''
'''
# vanused

import random
vanused = []
for i in range(5):
    vanused.append(random.randint(1,99))
print("Inimeste vanused:",vanused)
print("Kõige vanem inimene:",max(vanused))
print("Kõige noorem inimene:",min(vanused))
print("Kõik vanused kokku:",sum(vanused))
print("Inimeste kesmine vanus:",sum(vanused)/len(vanused))
'''
'''
# duplikaadid

nimed = ["Juhan","Kati","Mario","Mario","Mati","Mati"]
nimed = list(set(nimed))
for n in range(len(nimed)):
    print(n+1,nimed[n])
'''
'''
# õpilased

nimi = ["mati", "kalle", "pille", "peeter", "juhan"]
for n in range(len(nimi)):
    print(n+1,nimi[n])
nr = int(input("Vali number:"))
del nimi[nr-1]
print("------------------")
lisa = input("Sisesta uus nimi:")
nimi.insert(nr-1, lisa)
print("------------------")
for n in range(len(nimi)):
    print(n+1,nimi[n])
'''
'''
# nimed lisame loendisse

nimed = []
for i in range(5):
    nimi = input("Sisesage nimi: ")
    nimed.append(nimi)
nimed.sort()
for i in range (len(nimed)):
    print(nimed[i])
'''