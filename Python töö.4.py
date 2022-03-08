# Bänner
'''
kuva = int(input("Mitu korda soovid kuvada: "))
def banner(t,k):
    for i in range(k):
        print(t.upper())

banner("Osta ja Sa ei kahetse!",kuva)
'''
# Õunamahla tegemine
'''
def mahlapakkide_arv(kogus):
    mahlapakkidearv = round(kogus*0.4/3,0)
    return mahlapakkidearv
kg = int(input("Sisesta õunade kogus: "))
print(int(mahlapakkide_arv(kg)))
'''

# Peo eelarve
'''
def eelarve(a):
    summa = a*10+55
    return summa
kutsutud =int(input("Mitu inimest on kutsutud? "))
tuleb =int(input("Mitu inimest tuleb kohale? "))
print("Maksimaalne eelarve: ", eelarve(kutsutud), "€")
print("Maksimaalne eelarve: ", eelarve(tuleb), "€")
'''

# Tervitused mõtisklustega
'''
kulalised = int(input("Mitu külalist tuleb?"))
def tervitus(a):
    for i in range(a):
        print('Võõrustaja: "Tere!"')
        print(f"Täna no {i+1} kord tervitada, mõtiskleb võõrustaja")
        print('Külaline: "Tere, suur tänu kutse eest!"')
        
tervitus(kulalised)
'''
