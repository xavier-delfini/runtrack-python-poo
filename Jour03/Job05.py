class Personnage:
    def __init__(self, nom, vie):
        self.__nom = nom
        self.__vie = vie

    def set_vie(self, new_vie):
        self.__vie = new_vie

    def get_vie(self):
        return self.__vie

    def attaquer(self, adversaire):
        adversaire.set_vie(adversaire.get_vie() - 1)


class Jeu:
    def __init__(self):
        self.__niveau = [0, 0]

    def choisirNiveau(self):
        while True:
            difficulté = input("Bienvenue quel niveau de difficulté voulez vous selectionner ?(Facile=F,Normal=N,Difficile=D,Impossible=I):")
            match difficulté:
                case "F":
                    self.__niveau = [15, 5]
                    break
                case "N":
                    self.__niveau = [13, 7]
                    break
                case "D":
                    self.__niveau = [10, 10]
                    break
                case "I":
                    self.__niveau = [5, 15]
                    break

    def lancerJeu(self):
        if self.__niveau == [0,0]:
            self.choisirNiveau()
        Player = Personnage("Player", self.__niveau[0])
        IA = Personnage("Zangief", self.__niveau[1])
        while self.verif_KO(Player, IA) == 0:
            Player.attaquer(IA)
            IA.attaquer(Player)
        if self.verif_KO(Player, IA) == 1:
            print("Victoire de l'ordinateur")
        elif self.verif_KO(Player, IA) == 2:
            print("Victoire du joueur")
    def verif_KO(self, player, IA):
        if player.get_vie() == 0:
            return 1
        elif IA.get_vie() == 0:
            return 2
        else:
            return 0
Game1=Jeu()
Game1.lancerJeu()