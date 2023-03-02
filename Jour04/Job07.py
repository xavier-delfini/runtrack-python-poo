import random


class __Carte():
    def __init__(self):
        self.__cartes = self.__créer_deck()
        self.list = ["As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Valet", "Reine", "Roi"]
        self.valeur =self.Piocher_carte()
        self.couleur= self.Piocher_couleur()

    def Piocher_couleur(self):
        return random.randint(0, 3)

    def Piocher_carte(self):
        random.choice(self.list)
    def Piocher(self):
        while True:
            for card in self

    # return resultat carte + couleur
    def __créer_deck(self):

        deck = []
        i = 0
        while i < 4:
            deck.append(self.list)
            i += 1
        return deck

# class Jeu:
    init()
    self.deck= self.__créer_deck()