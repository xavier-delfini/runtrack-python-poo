class Operation:

    def __init__(self):
        self.nombre1 = 1
        self.nombre2 = 2

    def __str__(self):
        return f"Le nombre1 est {self.nombre1}\nLe nombre2 est {self.nombre2}"
    def addition(self):
        resultat=self.nombre1+self.nombre2
        print("nombre1 ajouté à nombre2 font "+str(resultat))

if __name__ == "__main__":#Empèche l'execution de ce code si ce fichier est importer
    Op1 = Operation
    print(Op1())