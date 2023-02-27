class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherX(self):
        print("x est égal à " + str(self.x))

    def afficherY(self):
        print("y est égal à " + str(self.y))

    def afficherLesPoints(self):
        self.afficherX()
        self.afficherY()

    def changerX(self,newX):
        self.x=newX

    def changerY(self,newY):
        self.y=newY


PT1=Point(14,12)
PT1.afficherX()
PT1.afficherY()

PT1.afficherLesPoints()

PT1.changerX(24)
PT1.afficherX()

PT1.changerY(54)
PT1.afficherY()




