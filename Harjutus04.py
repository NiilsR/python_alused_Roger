# Harjutus04
# Roger Niils
#03.02.22

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
print("{arv1}{tehe}{arv2}={v}")
    


#Ruudu kontroll == > < >= !=
a = int(input("Sisesta ruudu üks külg: "))
b = int(input("Sisesta ruudu teine külg: "))
if a == b:
    print("Tegemist on ruuduga")
#elif:
# kirjutad siia veel midagi
else:
    print("Risttahukas")