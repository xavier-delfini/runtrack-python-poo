class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print("Je suis "+self.prenom+" "+self.nom)

Per1 = Personne("Delfini", "Xavier")
Per1.SePresenter()

Per2 = Personne("John", "Doe")
Per2.SePresenter()