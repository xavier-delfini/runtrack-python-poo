class Voiture:
    def __init__(self, marque, modèle, année, kilométrage):
        self.__marque = marque
        self.__modèle = modèle
        self.__année = année
        self.__kilométrage = kilométrage
        self.__en_marche = False
        self.__reservoir = 50

    def get_marque(self):
        return self.__marque
    def set_marque(self,new_marque):
        self.__marque= new_marque
    def get_model(self):
        return self.__marque
    def set_model(self,new_model):
        self.__model = new_model
    def get_year(self):
        return self.__année
    def set_year(self,new_year):
        self.__année = new_year
    def get_kilometers(self):
        return self.__kilométrage
    def set_kilometers(self,new_kilometer):
        self.__kilométrage = new_kilometer
    def get_rolling(self):
        return self.__en_marche
    def demmarer(self):
        if not self.get_rolling():
            if self.__verifier_plein() > 5:
                self.__en_marche = True
            else:
                print("La voiture n'a pas assez d'essence pour démmarer")
        else:
            print("La voiture est déjà en marche")
    def arreter(self):
        if self.get_rolling():
            self.__en_marche = False
        else:
            print("La voiture est déjà à l'arret")
    def __verifier_plein(self):
        return self.__reservoir
    def set_reservoir(self,new_reservoir):
        self.__reservoir= new_reservoir
car1=Voiture("Peugeot","205","1995","70000")
car1.demmarer()
car1.arreter()
car1.set_reservoir(5)
car1.demmarer()




