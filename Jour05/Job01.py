class Factorielle:
    def __init__(self, nb_entier):
        self.i = nb_entier
        self.nombre_total = 1

    def factorisation(self):
        if self.i != 0:
            self.nombre_total *= self.i
            self.i -= 1
            self.factorisation()
        else:
            print(self.nombre_total)
            return 5


nb_entier = input("Veuillez entrer un nombre entier")
Num1 = Factorielle(int(nb_entier))
Num1.factorisation()
