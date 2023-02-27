class Animal:
    def __init__(self):
        self.age = 0
        self.name = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, new_name):
        self.name = new_name


Pet = Animal()
print("L'age de l'animal est de " + str(Pet.age) + " ans")
Pet.vieillir()
Pet.nommer("Croquette")

print("L'age de l'animal est de " + str(Pet.age) + " ans")
print("L'animal se nomme " + str(Pet.name))
