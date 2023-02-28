class Livre:
    def verif_num_pages(self,num_page):
        if num_page>0:
            return 1
        else:
            print("Veuillez entrer un nombre de page positif")
    def __init__(self,nom,auteur,num_page):

        self.__nom= nom
        self.__auteur= auteur
        if self.verif_num_pages(num_page)==1:
            self.__num_page= num_page

    def get_name(self):
        return self.__nom
    def set_name(self,new_name):
        self.__nom= new_name
    def get_autor(self):
        return self.__auteur
    def set_autor(self,new_autor):
        self.__auteur= new_autor

    def get_numb_pages(self):
        return self.__num_page

    def set_numb_pages(self, new_num_page):
        if self.verif_num_pages(new_num_page)==1:
            self.__num_page = new_num_page
Book1=Livre("Windows pour les nuls","Herger",350)
Book1.set_name("Linux pour les nuls")
print(Book1.get_name())
Book1.set_autor("Pinguin sympa")
print(Book1.get_autor())
Book1.set_numb_pages(-500)
Book1.set_numb_pages(550)
print(Book1.get_numb_pages())




