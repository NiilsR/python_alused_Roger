# Roger Niils
# Harjutus06
# 15.02.22

ere = 0
kes = 0
with open('s6pru_l6ustaraamatus.txt','r') as sobrad:
    for rida in sobrad:
        enimi, pnimi, er, likes = rida.split()
        print (f"{enimi:11}{pnimi:12}{er:7}{likes:5}")
        if er == "RE":
            ere +=1
        elif er == "KE":
            kes +=1
print("Reformikaid:",ere)
print("Kesikuid:",kes)
