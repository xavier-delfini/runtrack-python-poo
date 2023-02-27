class Personnage:
    def __init__(self):
        self.x = 0
        self.y = 0

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def haut(self):
        self.y -= 1

    def bas(self):
        self.y += 1

    def position(self):
        pos=(self.x, self.y)
        return pos


Per1 = Personnage()
print(Per1.position())
Per1.droite()
print(Per1.position())
Per1.bas()
print(Per1.position())
Per1.gauche()
print(Per1.position())
Per1.haut()
print(Per1.position())

