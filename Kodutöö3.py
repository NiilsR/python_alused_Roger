
'''
fail = open("rebased.txt", encoding="UTF-8")
vastuvoetud = []
for rida in fail:
    vastuvoetud.append(int(rida))
    
aasta = input("Palun sisestage, millise aasta andmeid teil vaja on: ")
print(f"{aasta}. aastal oli vastuvõetud {vastuvoetud[int(aasta[3])-1]}")
'''
'''
porgand = 0
ringid = int(input("Sisestage ringide arv: "))
for i in range(1,ringid+1):
    if i%2==0:
        porgand +=i

print(f"Saadavate porgandite kogu arv on {porgand} ")
'''
'''
fail = oepn("konto.txt", encoding="UTF-8")
for rida in fail:
    if int(rida) > 0:
        print(rida,end="")
'''
fail = input("Sisestage failinimi: ")
fail = open(fail, encoding="UFT-8")
for i in fail:
    print(i)




