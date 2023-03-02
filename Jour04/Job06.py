class Véhicule:
    def __init__(self, marque, modele, année, prix):
        self.marque = marque
        self.modele = modele
        self.année = année
        self.prix = prix

    def informationsVehicule(self):
        print("Marque: " + self.marque)
        print("Modèle: " + self.modele)
        print("Année de fabrication: " + str(self.année))
        print("Prix: " + str(self.prix))
    def demarrer(self):
        print("Attention je roule")

class Voiture(Véhicule):
    def __init__(self, marque, modele, année, prix):
        Véhicule.__init__(self, marque, modele, année, prix)
        self.portes = 4

    def informationsVehicule(self):
        Véhicule.informationsVehicule(self)
        print("Nombre de portes: " + str(self.portes))
    def demarrer(self):
        print("La Voiture démarre attention !")

Car1 = Voiture("Tesla", "Modèle S", "2020", 30000)
Car1.informationsVehicule()
Car1.demarrer()


class Moto(Véhicule):
    def __init__(self, marque, modele, année, prix):
        Véhicule.__init__(self, marque, modele, année, prix)
        self.roues = 2
    def informationsVehicule(self):
        Véhicule.informationsVehicule(self)
        print("Nombre de roues: " + str(self.roues))
    def demarrer(self):
        print("La moto demmare attention !")
Moto1=Moto("Yamaha","1200 Vmax",1987,4500)
Moto1.informationsVehicule()
Moto1.demarrer()