# KT
# Roger Niils
# 10.03.22

hall = 0
kirju = 0
valge = 0
punane = 0
must = 0
keskminep = []

# Küsin mis värvi kassi tahad
input("Millist kassi värvi sa tahad? ")

with open('felix.txt') as kass:
    for rida in kass:
        nimi, varv, pikkus = rida.split()
        if varv == "hall":
            hall +=1
        if varv == "kirju":
            kirju +=1
        if varv == "valge":
            valge +=1
        if varv == "punane":
            punane +=1
        if varv == "must":
            must +=1


print("Siin on selle kassi keskmine saba pikkus :",)