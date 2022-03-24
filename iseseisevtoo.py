# Roger Niils
# 20.03.22
# Iseseisevtoo

# 14.

# Palkade võrdlus - Loo palk.txt fail töötajate nime, soo ja palganumbriga (10 töötajat).
# Koosta programm, mis analüüsib kas firmas toimub diskrimineerimist soo järgi. Selleks võrdle omavahel meeste ja naiste palkade keskmiseid, samuti meeste ja naiste kõige kõrgemat palka. Programm peab tegema otsuse.
# mees=M naine=N

summa = 0
summa2 = 0
kk = 0
kk2 = 0

# Openime faili
with open("palk.txt", "r")as fail:
# Saame siin summa ja keskmise
    for i in fail:
        rida = i.split(" ")
        if rida[2] == "m":
            summa += int(rida[3])
            kk = summa/len(rida[3])
            maks = max(rida[3])
        elif rida[2] == "n":
            summa2 += int(rida[3])
            kk2 = summa2/len(rida[3])
            maks1 = max(rida[3])
            
        
# Keskmine palk       
print ("M keskmine palk on: ",kk,"€.")            
print ("N keskmine palk on: ",kk2,"€.")

# M ja N palga vahe leidmine
vahe=kk-kk2
print("M palk on ",vahe,"€ võrra suurem.")


# Keskmiste palkade võrdlemine
if kk2 < kk:
    print("See on N soo järgi diskrimineerimine.")
    
elif kk < kk2:
    print("See on M soo järgi diskrimineerimine.")
    
else:
    if kk2 == kk:
       print("Firmas ei diskrimineerita.")


#Tekst läheb faili.

with open("palk.txt", "a+") as file_object:
    file_object.seek(0)
    data = file_object.read(100)
    if kk2 < kk:
        file_object.write("\n")
        file_object.write("Firmas on N vastu diskrimineerimine")
    

with open("palk.txt", "a+") as file_object:
    file_object.seek(0)
    data = file_object.read(100)
    if kk < kk2:
        file_object.write("\n")
        file_object.write("Diskrimineerimine on N vastu")
    
with open("palk.txt", "a+") as file_object:
    file_object.seek(0)
    data = file_object.read(100)
    if kk == kk2:
        file_object.write("\n")
        file_object.write("Diskrimineerimine on M vastu")