# ülikooli vastuvõetud
'''
fail = open("rebased.txt", encoding="UTF-8")
vastuvoetud = []
for rida in fail:
    vastuvoetud.append(int(rida))
    
aasta = input("Palun sisestage, millise aasta andmeid teil vaja on: ")
print(f"{aasta}. aastal oli vastuvõetud {vastuvoetud[int(aasta[3])-1]}")
'''
# Jänesevanemate mure
'''
porgand = 0
ringid = int(input("Sisestage ringide arv: "))
for i in range(1,ringid+1):
    if i%2==0:
        porgand +=i

print(f"Saadavate porgandite kogu arv on {porgand} ")
'''
# Sissetulekud
'''
fail = oepn("konto.txt", encoding="UTF-8")
for rida in fail:
    if int(rida) > 0:
        print(rida,end="")
'''
# Jukebox
'''
lugu = 1
fail1 = input("Sisestage failinimi: ")
fail = open(fail1, encoding="UTF-8")
number = 1
for i in fail:
    print(str(number)+". " +str(i), end="")
    number +=1

fail = open(fail1, encoding="UTF-8")
lugud = int(input("\n Mis lugu tahad? "))
for i in fail:
    if lugu == lugud:
        print(i)
    lugu +=1
'''
#