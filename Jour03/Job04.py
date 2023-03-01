class Joueur:
    def __init__(self,nom,numéro,position):
        self.__nom=nom
        self.__numero=numéro
        self.__position=position
        self.__numb_but=0
        self.__pass_de=0
        self.__cart_jaune=0
        self.__cart_rouge=0
    def marquerUnBut(self):
        self.__numb_but+=1
    def effectuerUnePasseDecisive(self):
        self.__pass_de+=1
    def recevoirUnCartonJaune(self):
        self.__cart_jaune+=1
    def recevoirUnCartonRouge(self):
        self.__cart_rouge+=1
    def afficherStatistiques(self):
        return{
            "Nom":self.__nom,
            "Numéro":self.__numero,
            "Position":self.__position,
            "But marqué":self.__numb_but,
            "Passe décisive":self.__pass_de,
            "Carton jaune reçu":self.__cart_jaune,
            "Carton rouge reçu":self.__cart_rouge
        }

class Equipe:
    def __init__(self, nom):
        self.__name = nom
        self.__liste_joueurs = []

    def ajouterJoueur(self,Joueur):
        self.__liste_joueurs.append(Joueur.afficherStatistiques())

    def AfficherStatistiquesJoueurs(self):
        return self.__liste_joueurs

    def mettreAJourStatistiquesJoueur(self,Joueur):
        i=self.search_object_in_list(Joueur)

    def search_object_in_list(self, object):
        i = 0
        for tache in self.__liste_joueurs:
            if tache["Titre"] == object.afficherStatistiques():
                return i
            i += 1
