class Produit:
    def __init__(self,nom,prixHT):
        self.nom=nom
        self.prixHT=prixHT
        self.TVA=1.20

    def calc_price_with_TVA(self):
        return self.prixHT*self.TVA

    def change_name(self, new_name):
        self.nom = new_name

    def change_price(self,new_price):
        self.prixHT = new_price

    def show_name(self):
        return self.nom

    def show_price(self):
        return self.prixHT

    def show_current_TVA(self):
        return self.TVA

    def afficher(self):
        infos={
            "Nom produit": self.show_name(),
            "Prix Hors Taxes": self.show_price(),
            "Prix Avec Taxes": self.calc_price_with_TVA(),
            "TVA Actuelle": self.show_current_TVA()
        }
        return infos

    
Prod1=Produit("VTT",500)
print(Prod1.afficher())
Prod1.change_name("Vélo Tout Terrains")
print(Prod1.show_name())
Prod1.change_price(450)
print(Prod1.afficher())

