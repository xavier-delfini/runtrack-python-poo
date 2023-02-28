class Rectangle:
    def __init__(self,longueur,largeur):
        self.__longueur=longueur
        self.__largeur= largeur
    def getLongueur(self):
        return self.__longueur
    def setLongueur(self,new_long):
        self.__longueur=new_long
    def getLargeur(self):
        return self.__largeur
    def setLargeur(self, new_larg):
        self.__largeur = new_larg

Rect1=Rectangle(10,5)
Rect1.setLongueur(7)
print(Rect1.getLongueur())
Rect1.setLargeur(3)
print(Rect1.getLargeur())