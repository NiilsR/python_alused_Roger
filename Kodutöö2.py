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

arv = int(input("Sisesta täisarv: "))
nisuterad = 1

i = 1
while i <= arv:
    nisuterad *= 2
    i += 1
print(f"Nisuteri on {arv}. ruudu eest: {nisuterad}")
    