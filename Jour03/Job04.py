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
        self.__liste_joueurs[i]=Joueur.afficherStatistiques()

    def search_object_in_list(self, object):
        i = 0
        for tache in self.__liste_joueurs:
            if tache["Nom"] == object.afficherStatistiques()["Nom"]:
                return i
            i += 1

#OM
Lopez=Joueur("Lopez",16,"GRD")
Tavares=Joueur("Tavares",30,"MD")
Bailly=Joueur("Bailly",3,"DG")
Under=Joueur("Under",17,"BU")
OM=Equipe("OM")
OM.ajouterJoueur(Lopez)
OM.ajouterJoueur(Tavares)
OM.ajouterJoueur(Bailly)
OM.ajouterJoueur(Under)
print(OM.AfficherStatistiquesJoueurs())

#PSG
Donnarumma=Joueur("Donnarumma",99,"GRD")
Ramos=Joueur("Ramos",4,"DD")
Messi=Joueur("Messi",30,"BU")
Mbappé=Joueur("Mbappé",7,"BU")
PSG=Equipe("PSG")
PSG.ajouterJoueur(Donnarumma)
PSG.ajouterJoueur(Ramos)
PSG.ajouterJoueur(Messi)
PSG.ajouterJoueur(Mbappé)
print(PSG.AfficherStatistiquesJoueurs())

#Match
Bailly.effectuerUnePasseDecisive()
Under.marquerUnBut()
Bailly.recevoirUnCartonJaune()
Bailly.recevoirUnCartonRouge()
OM.mettreAJourStatistiquesJoueur(Bailly)
OM.mettreAJourStatistiquesJoueur(Under)
print(OM.AfficherStatistiquesJoueurs())
