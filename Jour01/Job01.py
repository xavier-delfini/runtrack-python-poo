class Operation:

    def __init__(self):
        self.nombre1=1
        self.nombre2=2
    def show_number(self):
        print("Le nombre1 est "+str(self.nombre1))
        print("Le nombre2 est "+str(self.nombre2))
    def addition(self):
        resultat=self.nombre1+self.nombre2
        print("nombre1 ajouté à nombre2 font "+str(resultat))


if __name__ == "__main__":#Empèche l'execution de ce code si ce fichier est importer
    print(Operation)