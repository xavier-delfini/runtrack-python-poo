class Ville:
    def __init__(self, nom, num_habitant):
        self.__nom = nom
        self.__num_habitant = num_habitant

    def get_num_habitant(self):
        return self.__num_habitant

    def set_num_habitant(self, new_number):
        self.__num_habitant = new_number


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.ajouterPopulation()

    def ajouterPopulation(self):
        new_habitants = self.__ville.get_num_habitant() + 1
        self.__ville.set_num_habitant(new_habitants)


Paris = Ville("Paris", 1000000)
print("Population de la vile de Paris: "+str(Paris.get_num_habitant())+" habitants")
Marseille = Ville("Marseille", 861635)
print("Population de la vile de Marseille: "+str(Marseille.get_num_habitant())+" habitants")

Person1 = Personne("John", 45, Paris)
Person2 = Personne("Myrtille", 4, Paris)
Person3 = Personne("Chloé", 18, Marseille)
print("Population de la vile de Paris: "+str(Paris.get_num_habitant())+" habitants")
print("Population de la vile de Marseille: "+str(Marseille.get_num_habitant())+" habitants")
