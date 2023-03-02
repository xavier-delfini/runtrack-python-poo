class Rectangle:
    def __init__(self, longeur, largeur):
        self.__longeur = longeur
        self.__largeur = largeur

    def get_longeur(self):
        return self.__longeur

    def set_longeur(self, new_longeur):
        self.__longeur = new_longeur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, new_largeur):
        self.__largeur = new_largeur

    def périmètre(self):
        return (self.__longeur + self.__largeur) * 2

    def surface(self):
        return self.__longeur * self.__largeur


class Parallélépipède(Rectangle):
    def __init__(self, longeur, largeur, volume):
        Rectangle.__init__(self, longeur, largeur)
        self.__volume = volume

    def get_volume(self):
        return self.__volume

    def set_volume(self, new_volume):
        self.__volume = new_volume

    def volume(self):
        return self.get_longeur() * self.get_largeur() * self.get_volume()


print("Rectangle")
rect1 = Rectangle(6, 4)
print(rect1.get_longeur())
print(rect1.get_largeur())
print(rect1.surface())
print(rect1.périmètre())
rect1.set_longeur(5)
rect1.set_largeur(3)
print(rect1.périmètre())

print("Parallélépipède")
Para1 = Parallélépipède(6, 4, 10)
print(Para1.périmètre())
print(Para1.volume())
