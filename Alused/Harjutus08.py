# Roger Niils
# Harjutus08
#28.02.22

class Auto:
    
    #atribuudid
    automark = 0
    aasta = 0
    mudel = 0
    hind = 0
    maksimumkiirus = 0
    
    def lisaautomark(self,x):
        self.automark = x
        
    def lisaaasta(self,x):
        self.aasta = x
        
    def lisamudel(self,x):
        self.mudel = x
        
    def lisahind(self,x):
        self.hind = x
        
    def maksimumkiirus(self,x):
        self.maksimumkiirus = x
        
    def kuva(self):
        print(f"{self.automark} {self.mudel} {self.hind} {self.aasta} {self.maksimumkiirus}")


uusObjekt = Auto()
uusObjekt.lisaautomark("Ford")
uusObjekt.lisamudel("Focus RS")
uusObjekt.lisahind(34999)
uusObjekt.lisaaasta(2016)
uusObjekt.maksimumkiirus("265kmh")
uusObjekt.kuva()