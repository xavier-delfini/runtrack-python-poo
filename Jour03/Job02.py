class CompteBancaire:
    def __init__(self,account_number,Fname,Lname,solde):
        self.__account_number=account_number
        self.__Fname=Fname
        self.__Lname=Lname
        self.__solde=solde
        self.__decouvert=self.is_decouvert()
    def get_Full_Name(self):
        return(self.__Fname,self.__Lname)
    def get_solde(self):
        return self.__solde
    def set_solde(self,new_solde):
        self.__solde=new_solde
    def get_account_number(self):
        return self.__account_number
    def is_decouvert(self):
        if self.__solde<0:
            return True
        else:
            return False
    def afficher(self):
        return {
            "Nom": self.get_Full_Name()[0],
            "Prénom": self.get_Full_Name()[1],
            "Numéro de compte": self.get_account_number(),
            "solde": self.get_solde(),
            "A découvert": self.is_decouvert()
        }

    def versement(self, money_to_add):
        self.__solde += money_to_add

    def afficherSolde(self):
        print("Votre solde est de :"+str(self.get_solde()))

    def virement(self,montant,destinataire):
        self.set_solde(self.get_solde() - montant)
        destinataire.versement(montant)

    def retrait(self,montant):
        new_solde=self.get_solde()-montant
        if (new_solde>0):
            self.set_solde(new_solde)
        else:
            print("Vous n'avez pas assez d'argent pour effectué ce retrait")
    def agios(self):
        if self.is_decouvert():
            self.set_solde(self.get_solde()+(self.get_solde()*0.05))

Client1 = CompteBancaire("1", "John", "Smith", -100)
Client2 = CompteBancaire("2", "John", "Dos", 500)

Client1.afficherSolde()
Client1.agios()
Client1.afficherSolde()
Client2.retrait(100)
Client2.afficherSolde()
Client2.virement(400,Client1)
Client2.retrait(100)
Client2.afficherSolde()
Client1.afficherSolde()
print(Client2.afficher())