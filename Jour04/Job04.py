class Forme:
    def aire(self):
        return 0
class Rectangle(Forme):
    def __init__(self,longeur,largeur):
        self.longeur=longeur
        self.largeur=largeur
    def aire(self):
        return self.longeur*self.largeur
if __name__ == "__main__":
    Rect1=Rectangle(7,4)
    print(Rect1.aire())