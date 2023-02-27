import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def circonference(self):
        print("La circonference de ce cercle est de "+str(2*math.pi*self.rayon))

    def changerRayon(self, new_rayon):
        self.rayon = new_rayon

    def aire(self):
        print("L'aire de ce cercle est de "+str(math.pi*(self.rayon*self.rayon)))

    def diametre(self):
        print("Le diametre de ce cercle est de "+str(self.rayon*2))

    def afficherInfos(self):
        print("Voici les différences infos a propos de ce cercle")
        self.circonference()
        self.aire()
        self.diametre()


Cercle1=Cercle(4)
Cercle1.circonference()
Cercle1.aire()
Cercle1.diametre()

Cercle1.changerRayon(15)
Cercle1.afficherInfos()


Cercle2=Cercle(7)
Cercle2.circonference()
Cercle2.aire()
Cercle2.diametre()
Cercle2.afficherInfos()
