class Student:

    def __init__(self,nom,prenom,carte_etu,credit):
        def __studentEval(credit):
            if credit >= 90:
                return "Excellent"
            elif credit >= 80:
                return "Très bien"
            elif credit >= 70:
                return "Bien"
            elif credit >= 60:
                return "Passable"
            elif credit < 60:
                return "Insuffisant"
        self.__nom = nom
        self.__prenom = prenom
        self.__carte_etu = carte_etu
        if not credit or not isinstance(credit, int):
            self.__credit = 0
        else:
            self.__credit = credit
        self.__level= __studentEval(self.__credit)
    def add_credits(self,credit_count):
        if credit_count > 0:
            self.__credit += credit_count
        else:
            print("Veuillez entrer un nombre supérieur a zero")
    def get_credits(self):
        #print("Le nombre de crédits de "+self.__prenom+" "+self.__nom+" est de "+str(self.__credit) +" points")
        return self.__credit
    def get_Fname(self):
        return self.__nom
    def get_Lname(self):
        return self.__prenom
    def get_student_card(self):
        return self.__carte_etu
    def get_level(self):
        return self.__level
    def studentInfo(self):
        infos = {
            "Nom": self.get_Fname(),
            "Prénom": self.get_Lname(),
            "Carte étudiante": self.get_student_card(),
            "Niveau étudiant": self.get_level()
        }
        return infos


Stu1 = Student("Doe", "John", "1111111111", 145)
Stu1.add_credits(50)
Stu1.add_credits(50)
Stu1.add_credits(50)
print(Stu1.get_credits())
print(Stu1.studentInfo())

Stu2 = Student("Xavier","Delfini","2222222222", 61)

print(Stu2.studentInfo())

