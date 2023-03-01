class Tache:
    def __init__(self,titre,description,statut):
        self.__titre= titre
        self.__description = description
        self.__statut = statut
    def titre_get(self):
        return self.__titre
    def statut_get(self):
        return self.__statut
    def descrip_get(self):
        return self.__description
    def statut_set(self,new_statut):
        self.__statut=new_statut
    def get_tache_list(self):
        return {
           "Titre":self.titre_get(),
            "Description": self.descrip_get(),
            "Statut":self.statut_get()
        }

class ListeDeTaches:
    def __init__(self):
        self.__tache_liste=[]
    def ajouterTache(self,new_tache):
        self.__tache_liste.append(new_tache)
    def supprimerTache(self,tache_to_remove):
        i = self.search_object_in_list(tache_to_remove)
        del self.__tache_liste[i]
    def search_object_in_list(self,object):
        i=0
        for tache in self.__tache_liste:
            if tache["Titre"] == object.titre_get():
                return i
            i+=1

    def marquerCommeFinie(self,tache_object):
        i=self.search_object_in_list(tache_object)
        self.__tache_liste[i]["Statut"]="Terminer"
    def afficherListe(self):
        return self.__tache_liste
    def filterListe(self,filtre):
        filtred_list = []
        i = 0
        for tache in self.__tache_liste:
            if tache["Statut"] == filtre:
                filtred_list.append(tache)
            i += 1
        return filtred_list

Courses=Tache("Courses","Faire les courses", "à faire")
Lessive=Tache("Lessive","Faire la lessive", "à faire")
Code=Tache("Code","S'entrainer au code", "Terminer")
Liste=ListeDeTaches()
Liste.ajouterTache(Courses.get_tache_list())
Liste.ajouterTache(Lessive.get_tache_list())
Liste.ajouterTache(Code.get_tache_list())
Liste.marquerCommeFinie(Lessive)
print(Liste.filterListe("Terminer"))
print(Liste.afficherListe())
Liste.supprimerTache(Courses)
print(Liste.afficherListe())

