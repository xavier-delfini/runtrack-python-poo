class Personne:
    def __init__(self):
        self.age = 14

    def afficherAge(self):
        return self.age

    def bonjour(self):
        print("Hello")

    def modifierAge(self, new_age):
        if isinstance(new_age, int):
            self.age = new_age
        else:
            print("Veuillez entrer un nombre entier")


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print("J'ai " + str(self.age) + " ans")


class Professeur(Personne):
    def __init__(self, matiere):
        Personne.__init__(self)
        self.__matiereEnseignée = matiere

    def enseigner(self):
        print("Le cours va commencer")

Person1 = Personne()
Student1 = Eleve()

Student1.bonjour()
Student1.allerEnCours()

Prof1=Professeur("Français")
Prof1.modifierAge(40)
Prof1.bonjour()
Prof1.enseigner()

