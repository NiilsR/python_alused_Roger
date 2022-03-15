'''
aratus = int(input("Mitu korda peaks äratus helisema?: "))

for i in range(aratus):
    print("Tõuse ja sära!")
'''

'''
import random

taringud = int(input("Sisestage täringute arv: "))

for i in range(taringud):
    print(random.randint(1,6))
    
'''
'''
arv = int(input("Sisesta täisarv: "))
nisuterad = 1

i = 1
while i <= arv:
    nisuterad *= 2
    i += 1
print(f"Nisuteri on {arv}. ruudu eest: {nisuterad}")
'''
'''
import random
lumi = 14
vmees = int(input("Mitu tahavad õuna?: "))
for i in range(vmees):
    oun = random.randint(1,2)
    print(oun)
    lumi = lumi -oun
print ('Lumivalgekesele jäi: ',lumi)
'''

