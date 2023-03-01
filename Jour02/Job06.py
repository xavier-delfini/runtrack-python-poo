import random
#TODO:Ajouter un plat à la commande, annuler une commande
#calculer total d'une commande (avec calcul TVA)

class Commande :
    def __init__(self):
        self.__numero_commande = random.randint(1, 9999)
        self.__plats_commander =[]
        self.__status_commande = "En cours"
        self.__TVA = 1.20

    def add_meal(self, meal, price):
        commande = {
            "Nom du plat": meal,
            "Prix du plat": price,
            "Status de la commande": "En cours"
        }
        self.__plats_commander.append(commande)

    def __get_meals(self):
        return self.__plats_commander

    def get_command_status(self):
        return self.__status_commande
    def __calc_total(self):
        total=0
        for meal in self.__plats_commander:
            if meal["Status de la commande"]!="Annulée":
                total += meal["Prix du plat"]
        return total
    def __calc_TVA(self):
        return self.__calc_total() * self.__TVA
    def show_total_command(self):
        print("Numéro de commande: "+str(self.__numero_commande))
        print(self.__get_meals())
        print(self.__calc_TVA())
    def cancel_order(self,nom_plat):
        for meal in self.__plats_commander:
            if meal["Nom du plat"]== nom_plat:
                meal["Status de la commande"]="Annulée"


meal1=Commande()
meal1.add_meal("Pâtes boloniaise", 15)
meal1.add_meal("Lasagnes", 20)
meal1.cancel_order("Lasagnes")
print(meal1.show_total_command())
